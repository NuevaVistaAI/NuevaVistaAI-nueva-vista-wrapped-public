#!/usr/bin/env python3
"""
Nueva Vista Wrapped - Helper Utilities
Common utility functions used across the Nueva Vista Wrapped CLI tools.
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path

def clean_text(text: str) -> str:
    """
    Clean text for word counting by removing code blocks, URLs, and non-words.

    Args:
        text: Raw text content to clean

    Returns:
        Cleaned text suitable for word counting
    """
    if not text:
        return ""

    # Remove code blocks (``` enclosed content)
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)

    # Remove inline code (`enclosed content`)
    text = re.sub(r'`[^`]+`', ' ', text)

    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)

    # Remove markdown formatting
    text = re.sub(r'[#*_~`\[\](){}]', ' ', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def count_words(text: str) -> int:
    """
    Count words in text using regex to match word boundaries.

    Args:
        text: Text to count words in

    Returns:
        Number of words found
    """
    if not text:
        return 0

    cleaned = clean_text(text)
    words = re.findall(r'\b\w+\b', cleaned)
    return len(words)

def format_hours(hours: float) -> str:
    """
    Format hours into human-readable string.

    Args:
        hours: Number of hours as float

    Returns:
        Formatted hours string (e.g., "2.5 hours", "1 hour", "45 minutes")
    """
    if hours < 1:
        minutes = int(hours * 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''}"
    elif hours < 2:
        return "1 hour"
    else:
        return f"{hours:.1f} hours"

def format_percentage(value: float, total: float) -> str:
    """
    Format a value as a percentage of total.

    Args:
        value: The value to convert to percentage
        total: The total to calculate percentage against

    Returns:
        Formatted percentage string (e.g., "25.0%")
    """
    if total == 0:
        return "0.0%"
    return f"{(value / total * 100):.1f}%"

def parse_date(date_string: str) -> Optional[datetime]:
    """
    Parse ISO date strings from ChatGPT exports.

    Args:
        date_string: ISO formatted date string

    Returns:
        Parsed datetime object or None if parsing fails
    """
    try:
        # Handle various ISO formats
        if 'T' in date_string:
            if date_string.endswith('Z'):
                return datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            else:
                return datetime.fromisoformat(date_string)
        else:
            return datetime.fromisoformat(date_string)
    except (ValueError, TypeError):
        return None

def get_date_range(conversations: List[Dict]) -> Tuple[Optional[datetime], Optional[datetime]]:
    """
    Get the date range covered by conversations.

    Args:
        conversations: List of conversation dictionaries

    Returns:
        Tuple of (earliest_date, latest_date) or (None, None) if no valid dates
    """
    dates = []

    for conv in conversations:
        # Try conversation create_time
        if 'create_time' in conv:
            date = parse_date(conv['create_time'])
            if date:
                dates.append(date)

        # Try message dates within the conversation
        if 'mapping' in conv:
            for msg_data in conv['mapping'].values():
                if isinstance(msg_data, dict) and 'message' in msg_data:
                    msg = msg_data['message']
                    if 'create_time' in msg:
                        date = parse_date(msg['create_time'])
                        if date:
                            dates.append(date)

    if not dates:
        return None, None

    return min(dates), max(dates)

def calculate_time_span_days(start_date: datetime, end_date: datetime) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        start_date: Starting date
        end_date: Ending date

    Returns:
        Number of days between dates
    """
    return (end_date - start_date).days

def get_vocabulary_diversity(text: str) -> int:
    """
    Calculate vocabulary diversity by counting unique words.

    Args:
        text: Text to analyze

    Returns:
        Number of unique words
    """
    if not text:
        return 0

    cleaned = clean_text(text)
    words = re.findall(r'\b\w+\b', cleaned.lower())
    return len(set(words))

def get_average_response_length(messages: List[str]) -> float:
    """
    Calculate average response length across messages.

    Args:
        messages: List of message texts

    Returns:
        Average number of words per message
    """
    if not messages:
        return 0.0

    total_words = sum(count_words(msg) for msg in messages)
    return total_words / len(messages)

def validate_conversations_format(data: Any) -> bool:
    """
    Validate that the loaded data matches expected ChatGPT export format.

    Args:
        data: Loaded JSON data to validate

    Returns:
        True if format appears valid, False otherwise
    """
    if not isinstance(data, list):
        return False

    if len(data) == 0:
        return True  # Empty list is valid

    # Check first conversation has expected structure
    first_conv = data[0]
    if not isinstance(first_conv, dict):
        return False

    required_fields = ['id', 'title', 'mapping']
    if not all(field in first_conv for field in required_fields):
        return False

    return True

def load_conversations(file_path: str) -> List[Dict]:
    """
    Load and validate conversations from JSON file.

    Args:
        file_path: Path to the conversations JSON file

    Returns:
        List of conversation dictionaries

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file isn't valid JSON
        ValueError: If data format is invalid
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Conversations file not found: {file_path}")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in {file_path}: {e}")

    if not validate_conversations_format(data):
        raise ValueError(f"Invalid conversations format in {file_path}")

    return data

def print_header(title: str, subtitle: str = "") -> None:
    """
    Print a formatted header for CLI output.

    Args:
        title: Main title text
        subtitle: Optional subtitle text
    """
    print("\n" + "="*60)
    print(f"🔥 {title}")
    if subtitle:
        print(f"   {subtitle}")
    print("="*60)

def print_section(title: str) -> None:
    """
    Print a formatted section header.

    Args:
        title: Section title
    """
    print(f"\n📊 {title}")
    print("-" * (len(title) + 4))

def print_metric(label: str, value: str, emoji: str = "•") -> None:
    """
    Print a formatted metric line.

    Args:
        label: Metric label
        value: Metric value
        emoji: Optional emoji prefix
    """
    print(f"   {emoji} {label}: {value}")

def print_badge_tier(hours: float, tier: str, emoji: str) -> None:
    """
    Print badge tier information with formatting.

    Args:
        hours: Total hours calculated
        tier: Badge tier name
        emoji: Badge emoji
    """
    print(f"\n🏆 Your Nueva Vista Badge: {emoji} {tier}")
    print(f"   Based on {format_hours(hours)} of AI collaboration")

def save_results_json(results: Dict, output_file: str) -> None:
    """
    Save results to JSON file with proper formatting.

    Args:
        results: Dictionary of results to save
        output_file: Path to output JSON file
    """
    # Convert datetime objects to ISO strings for JSON serialization
    def datetime_handler(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=datetime_handler)

    print(f"\n💾 Results saved to: {output_file}")

def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in megabytes.

    Args:
        file_path: Path to file

    Returns:
        File size in MB
    """
    try:
        size_bytes = Path(file_path).stat().st_size
        return size_bytes / (1024 * 1024)
    except (OSError, FileNotFoundError):
        return 0.0

def create_confidence_message(metric_name: str, confidence_level: str = "moderate") -> str:
    """
    Create a confidence message for metrics.

    Args:
        metric_name: Name of the metric
        confidence_level: Confidence level ("high", "moderate", "low")

    Returns:
        Formatted confidence message
    """
    confidence_messages = {
        "high": "📈 High confidence in this metric",
        "moderate": "📊 Moderate confidence - based on standard assumptions", 
        "low": "📉 Lower confidence - limited data or assumptions"
    }

    return confidence_messages.get(confidence_level, confidence_messages["moderate"])

# Nueva Vista branding colors (for potential future terminal colorization)
NUEVA_VISTA_COLORS = {
    "volcanic_red": "#C72C48",
    "deep_ocean_blue": "#004D7A",
    "neutral_gray": "#6B7280",
    "success_green": "#10B981",
    "warning_yellow": "#F59E0B"
}

# Badge tier definitions (centralized for consistency)
BADGE_TIERS = {
    "AI Legend": {"min_hours": 500.0, "emoji": "🌟", "color": "volcanic_red"},
    "AI Pioneer": {"min_hours": 250.0, "emoji": "🚀", "color": "deep_ocean_blue"},
    "AI Explorer": {"min_hours": 100.0, "emoji": "🧭", "color": "success_green"},
    "AI Collaborator": {"min_hours": 25.0, "emoji": "🤝", "color": "warning_yellow"},
    "AI Curious": {"min_hours": 0.0, "emoji": "🔍", "color": "neutral_gray"}
}

def get_badge_tier(hours: float) -> Tuple[str, str]:
    """
    Get badge tier and emoji for given hours.

    Args:
        hours: Total collaboration hours

    Returns:
        Tuple of (tier_name, emoji)
    """
    for tier_name, tier_info in BADGE_TIERS.items():
        if hours >= tier_info["min_hours"]:
            return tier_name, tier_info["emoji"]

    # Fallback (should never reach here due to 0.0 min for AI Curious)
    return "AI Curious", "🔍"

if __name__ == "__main__":
    # Simple test when run directly
    print("Nueva Vista Wrapped - Helper Utilities")
    print("Testing basic functions...")

    # Test word counting
    test_text = "This is a test with 10 words total here."
    word_count = count_words(test_text)
    print(f"Word count test: {word_count} words (expected: 10)")

    # Test hour formatting
    test_hours = [0.5, 1.0, 2.5, 10.0]
    for hours in test_hours:
        formatted = format_hours(hours)
        print(f"Hours formatting: {hours} -> {formatted}")

    print("✅ Helper utilities test completed!")
