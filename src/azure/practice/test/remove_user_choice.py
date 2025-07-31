#!/usr/bin/env python3
"""
Script to remove all 'userChoice' fields from JSON data.
This script reads a JSON file, removes all 'userChoice' entries from each object,
and saves the modified data to a new file.
"""

import json
import os
from typing import Any, Dict, List


def remove_user_choice_from_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove 'userChoice' field from a single object.
    
    Args:
        obj: Dictionary object that may contain 'userChoice' field
        
    Returns:
        Dictionary with 'userChoice' field removed
    """
    if isinstance(obj, dict):
        # Remove 'userChoice' if it exists
        if 'userChoice' in obj:
            del obj['userChoice']
        
        # Recursively process nested dictionaries
        for key, value in obj.items():
            if isinstance(value, dict):
                obj[key] = remove_user_choice_from_object(value)
            elif isinstance(value, list):
                obj[key] = [remove_user_choice_from_object(item) if isinstance(item, dict) else item for item in value]
    
    return obj


def process_json_file(input_file: str, output_file: str = None) -> None:
    """
    Process JSON file to remove all 'userChoice' fields.
    
    Args:
        input_file: Path to the input JSON file
        output_file: Path to the output JSON file (optional, defaults to input_file with '_cleaned' suffix)
    """
    # Generate output filename if not provided
    if output_file is None:
        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_cleaned{ext}"
    
    try:
        # Read the JSON file
        print(f"Reading JSON file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process the data
        print("Removing 'userChoice' fields...")
        if isinstance(data, list):
            # If data is a list, process each item
            processed_data = [remove_user_choice_from_object(item) for item in data]
        else:
            # If data is a single object, process it directly
            processed_data = remove_user_choice_from_object(data)
        
        # Write the processed data to output file
        print(f"Writing cleaned data to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=4, ensure_ascii=False)
        
        print(f"Successfully processed {input_file}")
        print(f"Cleaned data saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{input_file}': {e}")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """Main function to run the script."""
    # Default input file path
    input_file = "01.json"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please make sure the JSON file is in the same directory as this script.")
        return
    
    # Process the file
    process_json_file(input_file)


if __name__ == "__main__":
    main() 