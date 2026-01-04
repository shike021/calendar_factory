import calendar
from PIL import Image, ImageDraw, ImageFont
import os
from config import *


def load_fonts():
    """Load fonts with fallback to default."""
    try:
        font = ImageFont.truetype(FONT_PATH_BOLD, FONT_SIZE_TITLE)
        large_font = ImageFont.truetype(FONT_PATH_BOLD, FONT_SIZE_YEAR)
        small_font = ImageFont.truetype(FONT_PATH_REGULAR, FONT_SIZE_DAYS)
    except:
        font = ImageFont.load_default()
        large_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    return font, large_font, small_font


def draw_month(draw, x, y, month, year, font, small_font, black, gray, red, blue):
    """Draw a single month calendar."""
    # Draw month border
    draw.rectangle(
        [
            x + 5,
            y + 5,
            x + (WIDTH - LEFT_MARGIN - RIGHT_MARGIN) // 6 - 5,
            y + (HEIGHT - TOP_MARGIN - BOTTOM_MARGIN) // 2 - 5,
        ],
        outline=black,
        width=2,
    )

    month_width = (WIDTH - LEFT_MARGIN - RIGHT_MARGIN) // 6
    month_height = (HEIGHT - TOP_MARGIN - BOTTOM_MARGIN) // 2

    # Month title
    title = MONTHS[month - 1]
    bbox = draw.textbbox((0, 0), title, font=font)
    title_width = bbox[2] - bbox[0]
    draw.text(
        (x + (month_width - title_width) // 2, y + 20), title, fill=black, font=font
    )

    # Days of the week
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_y = y + 120
    cell_width = (month_width - 10) // 7
    for i, day in enumerate(days):
        color = red if day == "Sun" else blue if day == "Sat" else black
        draw.text(
            (x + 5 + i * cell_width + cell_width // 2 - 15, day_y),
            day,
            fill=color,
            font=small_font,
        )

    # Get calendar
    cal = calendar.monthcalendar(year, month)

    # Draw grid
    cell_height = 100
    start_y = day_y + 80
    for week in cal:
        for i, day in enumerate(week):
            if day != 0:
                color = red if i == 6 else blue if i == 5 else black
                text_x = x + 5 + i * cell_width + cell_width // 2 - 10
                draw.text((text_x, start_y), str(day), fill=color, font=small_font)
        draw.line(
            [x + 5, start_y + cell_height, x + month_width - 5, start_y + cell_height],
            fill=gray,
            width=1,
        )
        start_y += cell_height

    # Vertical lines
    for i in range(8):
        line_x = x + 5 + i * cell_width
        draw.line([line_x, day_y, line_x, start_y - cell_height], fill=gray, width=1)


def generate_calendar(year):
    """Generate calendar images for the given year."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i, bg_color in enumerate(BACKGROUND_COLORS):
        image = Image.new("RGB", (WIDTH, HEIGHT), bg_color)
        draw = ImageDraw.Draw(image)

        font, large_font, small_font = load_fonts()

        # Draw year
        year_text = str(year)
        bbox = draw.textbbox((0, 0), year_text, font=large_font)
        year_width = bbox[2] - bbox[0]
        year_height = bbox[3] - bbox[1]
        year_x = (WIDTH - year_width) // 2
        year_y = (TOP_MARGIN - year_height) // 2
        draw.text((year_x, year_y), year_text, fill=BLACK, font=large_font)

        # Draw months
        for row in range(2):
            for col in range(6):
                month = row * 6 + col + 1
                x = col * ((WIDTH - LEFT_MARGIN - RIGHT_MARGIN) // 6) + LEFT_MARGIN
                y = row * ((HEIGHT - TOP_MARGIN - BOTTOM_MARGIN) // 2) + TOP_MARGIN
                draw_month(
                    draw, x, y, month, year, font, small_font, BLACK, GRAY, RED, BLUE
                )

        # Save
        filename = f"{OUTPUT_DIR}/{year}_calendar_{COLOR_NAMES[i]}.png"
        image.save(filename)
        print(f"Wallpaper generated: {filename}")
