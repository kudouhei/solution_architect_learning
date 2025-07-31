# JSON UserChoice Removal Scripts

This directory contains Python scripts to remove all `userChoice` fields from JSON files.

## Scripts

### 1. `remove_user_choice.py` - Basic Script
A simple script that processes a single JSON file named `01.json` in the current directory.

**Usage:**
```bash
python remove_user_choice.py
```

**Features:**
- Automatically looks for `01.json` in the current directory
- Creates output file with `_cleaned` suffix
- Provides progress feedback
- Handles errors gracefully

### 2. `remove_user_choice_advanced.py` - Advanced Script
A feature-rich script with command-line arguments for flexible processing.

**Usage Examples:**

```bash
# Process a single file
python remove_user_choice_advanced.py 01.json

# Process with custom output filename
python remove_user_choice_advanced.py 01.json -o cleaned.json

# Process all JSON files in current directory
python remove_user_choice_advanced.py --directory . --pattern "*.json"

# Overwrite existing output files
python remove_user_choice_advanced.py 01.json --overwrite

# Show help
python remove_user_choice_advanced.py --help
```

**Features:**
- Command-line argument support
- Process single files or entire directories
- Custom output filenames
- Overwrite protection
- Size reduction reporting
- Error handling and progress feedback

## What the Scripts Do

Both scripts:
1. Read JSON files (supports both single objects and arrays of objects)
2. Recursively search for and remove all `userChoice` fields
3. Preserve the original structure and formatting
4. Save the cleaned data to a new file
5. Provide feedback on the processing results

## File Structure

The scripts expect JSON files with the following structure:
```json
[
  {
    "question": { ... },
    "userChoice": [ ... ],  // This will be removed
    "correctChoice": [ ... ]
  },
  ...
]
```

## Output

- **Basic script**: Creates `01_cleaned.json`
- **Advanced script**: Creates `{filename}_cleaned.json` by default, or custom filename if specified

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Error Handling

The scripts handle common errors:
- File not found
- Invalid JSON format
- Permission issues
- General processing errors

## Example Output

```
Reading JSON file: 01.json
Removing 'userChoice' fields...
Writing cleaned data to: 01_cleaned.json
Successfully processed 01.json
Cleaned data saved to: 01_cleaned.json
Size reduction: 26,037 bytes (10.2%)
``` 