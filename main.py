#!/usr/bin/env python3
"""
Calendar Wallpaper Generator

Generates high-resolution calendar wallpapers for a given year with multiple color themes.
"""

import argparse
from calendar_generator import generate_calendar


def main():
    parser = argparse.ArgumentParser(description="Generate calendar wallpapers.")
    parser.add_argument(
        "year",
        type=int,
        nargs="?",
        default=2026,
        help="Year for the calendar (default: 2026)",
    )
    parser.add_argument(
        "--output-dir", default="target", help="Output directory (default: target)"
    )

    args = parser.parse_args()

    # Validate year
    if not (1900 <= args.year <= 2100):
        print("Error: Year must be between 1900 and 2100")
        return

    print(f"Generating calendar for year {args.year}...")
    generate_calendar(args.year)
    print("Done!")


if __name__ == "__main__":
    main()
