# Calendar Factory

A Python tool to generate high-resolution calendar wallpapers for any year with multiple elegant color themes.

## Features

- Generate 4K resolution calendar wallpapers (3840x2160)
- Support for multiple years (command-line argument)
- Three elegant background colors: Light Gray, Ivory, and Taupe
- Customizable fonts and layouts
- Modular code structure for easy maintenance

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd calendar-factory
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Generate calendar for the current year (2026):

```bash
python main.py
```

Generate calendar for a specific year:

```bash
python main.py 2027
```

### Command Line Options

- `year`: Year for the calendar (default: 2026)
- `--output-dir`: Output directory (default: target)
- `--help`: Show help message

### Examples

```bash
# Generate 2028 calendar
python main.py 2028

# Generate with custom output directory
python main.py 2029 --output-dir output
```

## Output

The tool generates three PNG files in the `target/` directory:

- `2026_calendar_gray.png` - Light gray background
- `2026_calendar_ivory.png` - Ivory background
- `2026_calendar_taupe.png` - Taupe background

Each image is a full-year calendar with:

- Large year number at the top
- 12 months arranged in 2 rows of 6
- Color-coded days (red for Sundays, blue for Saturdays)

## Configuration

Edit `config.py` to customize:

- Image dimensions and margins
- Font paths and sizes
- Color schemes
- Month names (for internationalization)

## Requirements

- Python 3.6+
- Pillow (PIL)

## Project Structure

```
calendar-factory/
├── main.py                 # CLI entry point
├── calendar_generator.py   # Core generation logic
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Packaging configuration
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── target/               # Generated images (ignored by git)
```

## Development

To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details.
