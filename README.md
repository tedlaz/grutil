# grutil

A Python utility library providing helper functions for working with Greek-specific formats, dates, numbers, and validators.

## Features

### 📅 Date & Time Utilities (`datetimes`)

Convert between ISO 8601 and Greek date formats, and perform datetime operations:

- **`iso2gr(iso_date_str)`** - Convert ISO date (YYYY-MM-DD) to Greek format (DD/MM/YYYY)
- **`gr2iso(gr_date)`** - Convert Greek date (DD/MM/YYYY) to ISO format (YYYY-MM-DD)
- **`date2gr(date_obj)`** - Convert Python date object to Greek format string
- **`gr2date(gr_date)`** - Convert Greek date string to Python date object
- **`iso2yearmonth(isodate)`** - Extract year-month from ISO date (2023-01-15 → 2023-01)
- **`is_greek_date(grdate)`** - Validate if string matches Greek date format
- **`delta_hours(date_from, date_to)`** - Calculate hours between two datetime objects
- **`round_half(hours)`** - Round hours to nearest half hour

### 🔢 Number Utilities (`numbers`)

Handle Greek number formatting (using comma as decimal separator and period as thousands separator):

- **`gr2float(gr_number_str)`** - Convert Greek-formatted number (1.234.567,89) to float
- **`float2gr(number, decimals=2)`** - Convert float to Greek-formatted string
- **`float2gr_empty_zero(number, decimals=2)`** - Convert float to Greek format, returns empty string for zero

### 📝 Text Utilities (`texts`)

Greek text processing utilities:

- **`grup(text)`** - Normalize Greek text by converting to uppercase and removing accents/diacritics for comparison

### ✅ Validators (`validators`)

Validate Greek identification numbers:

- **`is_valid_afm(afm)`** - Validate Greek VAT number (AFM - 9 digits)
- **`is_valid_amka(amka)`** - Validate Greek Social Security Number (AMKA - 11 digits)

## Installation

```bash
pip install grutil
```

Or using `uv`:

```bash
uv add grutil
```

## Usage Examples

### Date Conversions

```python
from grutil.datetimes import iso2gr, gr2iso, gr2date

# Convert ISO to Greek format
greek_date = iso2gr("2024-03-15")  # Returns: "15/03/2024"

# Convert Greek to ISO format
iso_date = gr2iso("15/03/2024")  # Returns: "2024-03-15"

# Convert Greek string to date object
date_obj = gr2date("15/03/2024")  # Returns: datetime.date(2024, 3, 15)
```

### Number Formatting

```python
from grutil.numbers import gr2float, float2gr

# Parse Greek-formatted number
value = gr2float("1.234.567,89")  # Returns: 1234567.89

# Format number as Greek
formatted = float2gr(1234567.89)  # Returns: "1.234.567,89"
formatted = float2gr(1234.5, decimals=3)  # Returns: "1.234,500"
```

### Text Processing

```python
from grutil.texts import grup

# Normalize Greek text for comparison
normalized = grup("Αθήνα")  # Returns: "ΑΘΗΝΑ"
normalized = grup("Ελλάδα")  # Returns: "ΕΛΛΑΔΑ"

# Useful for case-insensitive comparisons
if grup(user_input) == grup("ΑΘΉΝΑ"):
    print("Match!")
```

### Validators

```python
from grutil.validators import is_valid_afm, is_valid_amka

# Validate Greek VAT number (AFM)
is_valid_afm("123456789")  # Returns: True or False

# Validate Greek Social Security Number (AMKA)
is_valid_amka("12345678901")  # Returns: True or False
```

## Development

### Requirements

- Python >= 3.10
- pytest >= 9.0.1 (for development)

### Running Tests

```bash
pytest
```

## License

This project is maintained by Ted Lazaros (tedlaz@gmail.com).

## Version

Current version: 0.2.0
