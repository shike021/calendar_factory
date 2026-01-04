import calendar
from PIL import Image, ImageDraw, ImageFont
import os

# Set up the calendar for 2026
year = 2026

# Create a new image with high resolution (e.g., 3840x2160 for 4K)
width, height = 3840, 2160
# Use a light gray background for better visual effect
bg_color = (245, 245, 245)  # Light Gray
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Try to load a font, fallback to default if not available
try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60
    )
    small_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35
    )
except:
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Colors
black = (0, 0, 0)
gray = (169, 169, 169)
red = (220, 20, 60)  # Crimson for Sundays
blue = (70, 130, 180)  # SteelBlue for Saturdays

# Month names
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Margins: larger top/bottom, narrower left/right
left_margin = 50
right_margin = 50
top_margin = 200
bottom_margin = 200

# Calculate inner area
inner_width = width - left_margin - right_margin
inner_height = height - top_margin - bottom_margin

# Calculate positions for 2 rows, 6 months each within inner area
month_width = inner_width // 6
month_height = inner_height // 2


# Function to draw a month
def draw_month(x, y, month, year):
    # Draw month border
    draw.rectangle(
        [x + 5, y + 5, x + month_width - 5, y + month_height - 5],
        outline=black,
        width=2,
    )

    # Month title
    title = f"{months[month-1]}"
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

    # Get calendar for the month
    cal = calendar.monthcalendar(year, month)

    # Draw the calendar grid
    cell_height = 100
    start_y = day_y + 80
    for week in cal:
        for i, day in enumerate(week):
            if day != 0:
                color = (
                    red if i == 6 else blue if i == 5 else black
                )  # Sun red, Sat blue
                # Center the text in the cell
                text_x = x + 5 + i * cell_width + cell_width // 2 - 10
                draw.text((text_x, start_y), str(day), fill=color, font=small_font)
        # Draw horizontal line
        draw.line(
            [
                x + 5,
                start_y + cell_height,
                x + month_width - 5,
                start_y + cell_height,
            ],
            fill=gray,
            width=1,
        )
        start_y += cell_height

    # Draw vertical lines
    for i in range(8):
        line_x = x + 5 + i * cell_width
        draw.line([line_x, day_y, line_x, start_y - cell_height], fill=gray, width=1)


# Draw all months
for row in range(2):
    for col in range(6):
        month = row * 6 + col + 1
        x = col * month_width + left_margin
        y = row * month_height + top_margin
        draw_month(x, y, month, year)

# Save the image
image.save("2026_calendar_wallpaper.png")
print("Wallpaper generated: 2026_calendar_wallpaper.png")
