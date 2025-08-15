#!/usr/bin/env python3
"""
Nueva Vista Wrapped - Quick Hours Analysis
Get your AI collaboration hours badge instantly

Usage: python nv_quick_hours.py /path/to/conversations.json
"""

import argparse
import json
import re
import sys
from datetime import datetime
from collections import Counter

# Constants
READING_WPM_DEFAULT = 220
WRITING_WPM_DEFAULT = 25
READING_WPM_LOW, READING_WPM_HIGH = 260, 180
WRITING_WPM_LOW, WRITING_WPM_HIGH = 35, 18

def tokenize(text):
    """Basic word tokenizer, strips code and URLs"""
    if not text:
        return []

    # Strip code blocks and URLs
    text = re.sub(r"`.*?`", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)

    # Extract word tokens
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

def parse_conversations(data):
    """Parse conversations from ChatGPT export format"""
    total_user_words = 0
    total_ai_words = 0
    total_user_msgs = 0
    total_ai_msgs = 0
    total_conversations = 0
    first_timestamp = None
    last_timestamp = None

    conversations = data if isinstance(data, list) else [data]

    for conv in conversations:
        if not isinstance(conv, dict):
            continue

        total_conversations += 1
        mapping = conv.get("mapping", {})

        for node_id, node in mapping.items():
            msg = node.get("message")
            if not msg:
                continue

            author = msg.get("author", {})
            role = author.get("role", "")
            text = extract_message_text(msg)
            timestamp = msg.get("create_time") or conv.get("create_time")

            if timestamp:
                if not first_timestamp or timestamp < first_timestamp:
                    first_timestamp = timestamp
                if not last_timestamp or timestamp > last_timestamp:
                    last_timestamp = timestamp

            word_count = len(tokenize(text))

            if role == "user":
                total_user_words += word_count
                total_user_msgs += 1
            elif role == "assistant":
                total_ai_words += word_count
                total_ai_msgs += 1

    return {
        "total_conversations": total_conversations,
        "total_user_msgs": total_user_msgs,
        "total_ai_msgs": total_ai_msgs,
        "total_user_words": total_user_words,
        "total_ai_words": total_ai_words,
        "first_timestamp": first_timestamp,
        "last_timestamp": last_timestamp
    }

def calculate_hours(user_words, ai_words, read_wpm=READING_WPM_DEFAULT, write_wpm=WRITING_WPM_DEFAULT):
    """Calculate total hours spent"""
    writing_minutes = user_words / max(1, write_wpm)
    reading_minutes = ai_words / max(1, read_wpm)
    total_minutes = writing_minutes + reading_minutes
    return total_minutes / 60.0

def get_badge_tier(hours):
    """Get badge tier based on hours"""
    if hours >= 500:
        return "🏆 AI Legend", "500+ hours"
    elif hours >= 250:
        return "🚀 AI Pioneer", "250+ hours"  
    elif hours >= 100:
        return "⭐ AI Explorer", "100+ hours"
    elif hours >= 50:
        return "🌱 AI Apprentice", "50+ hours"
    elif hours >= 10:
        return "👶 AI Curious", "10+ hours"
    else:
        return "🐣 AI Newcomer", "Getting started"

def format_timestamp(ts):
    """Format timestamp to readable date"""
    if not ts:
        return "Unknown"
    try:
        return datetime.utcfromtimestamp(float(ts)).strftime("%B %d, %Y")
    except:
        return "Unknown"

def main():
    parser = argparse.ArgumentParser(
        description="Nueva Vista Wrapped - Get your AI collaboration hours"
    )
    parser.add_argument("conversations_json", help="Path to conversations.json from ChatGPT export")
    parser.add_argument("--quiet", "-q", action="store_true", help="Minimal output")

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

    # Parse the data
    stats = parse_conversations(data)

    # Calculate hours
    hours_est = calculate_hours(stats["total_user_words"], stats["total_ai_words"])
    hours_low = calculate_hours(stats["total_user_words"], stats["total_ai_words"], 
                               read_wpm=READING_WPM_LOW, write_wpm=WRITING_WPM_LOW)
    hours_high = calculate_hours(stats["total_user_words"], stats["total_ai_words"],
                                read_wpm=READING_WPM_HIGH, write_wpm=WRITING_WPM_HIGH)

    # Get badge info
    badge_emoji, badge_desc = get_badge_tier(hours_est)

    if args.quiet:
        print(f"{hours_est:.1f}")
        return

    # Display results
    print("\n" + "="*60)
    print("🔥 NUEVA VISTA WRAPPED - YOUR AI JOURNEY")
    print("="*60)
    print()
    print(f"{badge_emoji}")
    print(f"Hours with AI: {hours_est:.1f} hrs (range {min(hours_low, hours_high):.1f}–{max(hours_low, hours_high):.1f})")
    print()
    print("📊 KEY STATS:")
    print(f"  • Conversations: {stats['total_conversations']:,}")
    print(f"  • Messages you wrote: {stats['total_user_msgs']:,}")
    print(f"  • AI replies read: {stats['total_ai_msgs']:,}")
    print(f"  • Words you wrote: {stats['total_user_words']:,}")
    print(f"  • Words you read from AI: {stats['total_ai_words']:,}")
    print()
    print("📅 TIMELINE:")
    print(f"  • First conversation: {format_timestamp(stats['first_timestamp'])}")
    print(f"  • Latest activity: {format_timestamp(stats['last_timestamp'])}")
    print()
    print("📋 SHAREABLE SUMMARY:")
    print(f"  {badge_emoji}")
    print(f"  I've spent {hours_est:.1f} hours building with AI!")
    print(f"  📊 {stats['total_conversations']:,} conversations • {stats['total_user_msgs']:,} messages • {stats['total_user_words']:,} words written")
    print(f"  #NuevaVistaWrapped")
    print()
    print("💡 NOTE: This analysis covers ChatGPT only.")
    print("   Your total AI collaboration time across all tools is likely 2-3x higher!")
    print()
    print("="*60)
    print("Built with ❤️ by Nueva Vista Labs")
    print("🔗 https://github.com/nuevavistalabs/nueva-vista-wrapped")
    print("="*60)

if __name__ == "__main__":
    main()
