# Configuration for calendar generator

# Image dimensions
WIDTH = 3840
HEIGHT = 2160

# Margins
LEFT_MARGIN = 50
RIGHT_MARGIN = 50
TOP_MARGIN = 200
BOTTOM_MARGIN = 200

# Font paths and sizes
FONT_PATH_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_PATH_REGULAR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_SIZE_TITLE = 60
FONT_SIZE_YEAR = 100
FONT_SIZE_DAYS = 35

# Colors
BACKGROUND_COLORS = [
    (245, 245, 245),  # Light Gray
    (255, 248, 220),  # Ivory
    (157, 148, 136),  # Taupe
]
COLOR_NAMES = ["gray", "ivory", "taupe"]

# Text colors
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
RED = (220, 20, 60)  # Crimson for Sundays
BLUE = (70, 130, 180)  # SteelBlue for Saturdays

# Month names
MONTHS = [
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

# Output directory
OUTPUT_DIR = "target"
