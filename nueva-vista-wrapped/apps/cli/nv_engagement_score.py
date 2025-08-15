#!/usr/bin/env python3
"""
Nueva Vista Wrapped - AI Engagement Score
Analyze the quality and depth of your AI collaborations

Usage: python nv_engagement_score.py /path/to/conversations.json
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

def tokenize(text):
    """Basic word tokenizer"""
    if not text:
        return []

    # Strip code blocks and URLs
    text = re.sub(r"`.*?`", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)

    tokens = re.findall(r"[A-Za-z0-9'']+", text.lower())
    return tokens

def extract_message_text(msg):
    """Extract text from ChatGPT message format"""
    if not msg:
        return ""

    content = msg.get("content", {})
    parts = content.get("parts", [])

    if isinstance(parts, list):
        pieces = []
        for p in parts:
            if isinstance(p, str):
                pieces.append(p)
            elif isinstance(p, dict):
                pieces.append(p.get("text", ""))
        return "\n".join(pieces)

    return content.get("text", "")

def analyze_message_patterns(text):
    """Analyze patterns in user messages"""
    if not text:
        return {}

    text_lower = text.lower()

    patterns = {
        "questions": len(re.findall(r"\?", text)),
        "code_requests": len(re.findall(r"\b(code|function|script|program)\b", text_lower)),
        "creative_requests": len(re.findall(r"\b(create|write|generate|design|make)\b", text_lower)),
        "analysis_requests": len(re.findall(r"\b(analyze|explain|compare|evaluate)\b", text_lower)),
        "learning_requests": len(re.findall(r"\b(learn|teach|understand|how)\b", text_lower)),
    }

    return patterns

def calculate_engagement_score(conversations_data):
    """Calculate AI engagement score based on multiple factors"""

    total_conversations = 0
    total_user_words = 0
    total_ai_words = 0
    total_user_msgs = 0
    total_ai_msgs = 0

    conversation_lengths = []
    vocabulary_diversity = []
    interaction_patterns = defaultdict(int)

    conversations = conversations_data if isinstance(conversations_data, list) else [conversations_data]

    for conv in conversations:
        if not isinstance(conv, dict):
            continue

        total_conversations += 1
        conv_user_words = 0
        conv_ai_words = 0
        conv_user_msgs = 0
        conv_ai_msgs = 0
        conv_vocabulary = set()

        mapping = conv.get("mapping", {})

        for node in mapping.values():
            msg = node.get("message")
            if not msg:
                continue

            author = msg.get("author", {})
            role = author.get("role", "")
            text = extract_message_text(msg)
            tokens = tokenize(text)

            if role == "user":
                conv_user_words += len(tokens)
                conv_user_msgs += 1
                total_user_words += len(tokens)
                total_user_msgs += 1
                conv_vocabulary.update(tokens)

                # Analyze message patterns
                patterns = analyze_message_patterns(text)
                for pattern, count in patterns.items():
                    interaction_patterns[pattern] += count

            elif role == "assistant":
                conv_ai_words += len(tokens)
                conv_ai_msgs += 1
                total_ai_words += len(tokens)
                total_ai_msgs += 1

        if conv_user_msgs > 0 and conv_ai_msgs > 0:
            conversation_lengths.append(conv_user_msgs + conv_ai_msgs)
            vocabulary_diversity.append(len(conv_vocabulary))

    # Calculate scoring components
    scores = {}

    # 1. Conversation Depth (25 points)
    avg_conv_length = sum(conversation_lengths) / max(1, len(conversation_lengths))
    depth_score = min(25, (avg_conv_length / 20) * 25)  # 20 messages = full points
    scores["conversation_depth"] = depth_score

    # 2. Vocabulary Diversity (20 points)
    avg_vocabulary = sum(vocabulary_diversity) / max(1, len(vocabulary_diversity))
    vocab_score = min(20, (avg_vocabulary / 100) * 20)  # 100 unique words = full points
    scores["vocabulary_diversity"] = vocab_score

    # 3. Interaction Quality (25 points)
    total_interactions = sum(interaction_patterns.values())
    if total_interactions > 0:
        quality_ratio = total_interactions / max(1, total_user_msgs)
        quality_score = min(25, quality_ratio * 25)
    else:
        quality_score = 0
    scores["interaction_quality"] = quality_score

    # 4. Engagement Consistency (15 points)
    if total_conversations > 0:
        msg_per_conv = total_user_msgs / total_conversations
        consistency_score = min(15, (msg_per_conv / 10) * 15)  # 10 msgs/conv = full points
    else:
        consistency_score = 0
    scores["engagement_consistency"] = consistency_score

    # 5. Response Utilization (15 points)
    if total_user_msgs > 0:
        response_ratio = total_ai_msgs / total_user_msgs
        utilization_score = min(15, response_ratio * 10)  # Cap at reasonable ratio
    else:
        utilization_score = 0
    scores["response_utilization"] = utilization_score

    total_score = sum(scores.values())

    return {
        "total_score": total_score,
        "component_scores": scores,
        "stats": {
            "total_conversations": total_conversations,
            "avg_conversation_length": avg_conv_length,
            "avg_vocabulary_diversity": avg_vocabulary,
            "interaction_patterns": dict(interaction_patterns),
            "total_user_msgs": total_user_msgs,
            "total_ai_msgs": total_ai_msgs
        }
    }

def get_engagement_tier(score):
    """Get engagement tier description"""
    if score >= 80:
        return "🎯 AI Master", "Exceptional engagement across all areas"
    elif score >= 65:
        return "🚀 Advanced Collaborator", "Strong AI partnership skills"
    elif score >= 50:
        return "⭐ Quality Explorer", "Good depth and consistency"
    elif score >= 35:
        return "🌱 Active Learner", "Growing AI collaboration skills"
    elif score >= 20:
        return "👶 Curious Beginner", "Building AI interaction habits"
    else:
        return "🐣 Getting Started", "Early stage AI user"

def main():
    parser = argparse.ArgumentParser(
        description="Nueva Vista Wrapped - AI Engagement Score Analysis"
    )
    parser.add_argument("conversations_json", help="Path to conversations.json from ChatGPT export")
    parser.add_argument("--detailed", "-d", action="store_true", help="Show detailed breakdown")

    args = parser.parse_args()

    try:
        with open(args.conversations_json, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {args.conversations_json}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON file: {args.conversations_json}")
        sys.exit(1)

    # Calculate engagement score
    result = calculate_engagement_score(data)

    score = result["total_score"]
    tier_emoji, tier_desc = get_engagement_tier(score)

    # Display results
    print("\n" + "="*60)
    print("⚡ NUEVA VISTA WRAPPED - AI ENGAGEMENT ANALYSIS")
    print("="*60)
    print()
    print(f"{tier_emoji}")
    print(f"AI Engagement Score: {score:.1f}/100")
    print(f"Tier: {tier_desc}")
    print()

    if args.detailed:
        print("📊 COMPONENT BREAKDOWN:")
        components = result["component_scores"]
        print(f"  • Conversation Depth: {components['conversation_depth']:.1f}/25")
        print(f"  • Vocabulary Diversity: {components['vocabulary_diversity']:.1f}/20")
        print(f"  • Interaction Quality: {components['interaction_quality']:.1f}/25")
        print(f"  • Engagement Consistency: {components['engagement_consistency']:.1f}/15")
        print(f"  • Response Utilization: {components['response_utilization']:.1f}/15")
        print()

        stats = result["stats"]
        print("📈 ENGAGEMENT STATS:")
        print(f"  • Average conversation length: {stats['avg_conversation_length']:.1f} messages")
        print(f"  • Average vocabulary per conversation: {stats['avg_vocabulary_diversity']:.0f} unique words")
        print(f"  • Questions asked: {stats['interaction_patterns'].get('questions', 0):,}")
        print(f"  • Creative requests: {stats['interaction_patterns'].get('creative_requests', 0):,}")
        print(f"  • Analysis requests: {stats['interaction_patterns'].get('analysis_requests', 0):,}")
        print()

    print("💡 ENGAGEMENT INSIGHTS:")

    stats = result["stats"]
    if stats["avg_conversation_length"] > 15:
        print("  ✅ You engage in deep, meaningful conversations with AI")
    elif stats["avg_conversation_length"] < 5:
        print("  💡 Try longer conversations for deeper insights")

    if result["component_scores"]["vocabulary_diversity"] > 15:
        print("  ✅ You explore diverse topics and use rich vocabulary")
    elif result["component_scores"]["vocabulary_diversity"] < 10:
        print("  💡 Consider exploring more varied topics with AI")

    if stats["interaction_patterns"].get("questions", 0) > stats["total_user_msgs"] * 0.3:
        print("  ✅ You're naturally curious and ask great questions")

    print()
    print("🔒 PRIVACY NOTE: This analysis runs entirely on your device.")
    print("   Your conversation data never leaves your computer.")
    print()
    print("="*60)
    print("Built with ❤️ by Nueva Vista Labs")
    print("🔗 https://github.com/nuevavistalabs/nueva-vista-wrapped")
    print("="*60)

if __name__ == "__main__":
    main()
