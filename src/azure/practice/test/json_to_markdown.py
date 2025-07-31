#!/usr/bin/env python3
"""
Script to convert JSON quiz data to markdown format.
This script reads the cleaned JSON file and converts it to a markdown file
that displays questions, choices, and marks correct answers.
"""

import json
import os
import re
from typing import Any, Dict, List


def clean_html_tags(text: str) -> str:
    """
    Remove HTML tags from text while preserving content.
    
    Args:
        text: Text that may contain HTML tags
        
    Returns:
        Cleaned text without HTML tags
    """
    if not text:
        return ""
    
    # Remove common HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode common HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    
    return text.strip()


def get_question_type(question_data: Dict[str, Any]) -> str:
    """
    Determine the question type based on the question data.
    
    Args:
        question_data: Question object from JSON
        
    Returns:
        Question type string
    """
    question_type = question_data.get("type", "Unknown")
    
    if question_type == "SingleSelect":
        return "Single Choice"
    elif question_type == "MultiSelect":
        return "Multiple Choice"
    else:
        return question_type


def format_question_text(text: str) -> str:
    """
    Format question text for markdown display.
    
    Args:
        text: Raw question text
        
    Returns:
        Formatted question text
    """
    # Clean HTML tags
    text = clean_html_tags(text)
    
    # Replace newlines with proper markdown formatting
    text = text.replace('\n\n', '\n\n')
    text = text.replace('\n', ' ')
    
    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def get_correct_choice_ids(correct_choices: List[Dict[str, Any]]) -> set:
    """
    Extract IDs of correct choices.
    
    Args:
        correct_choices: List of correct choice objects
        
    Returns:
        Set of correct choice IDs
    """
    return {choice.get("id") for choice in correct_choices}


def convert_choice_to_markdown(choice: Dict[str, Any], correct_ids: set, choice_letter: str) -> str:
    """
    Convert a choice to markdown format.
    
    Args:
        choice: Choice object from JSON
        correct_ids: Set of correct choice IDs
        choice_letter: Letter identifier for the choice (A, B, C, etc.)
        
    Returns:
        Markdown formatted choice string
    """
    choice_text = clean_html_tags(choice.get("text", ""))
    choice_id = choice.get("id")
    is_correct = choice_id in correct_ids
    
    # Format the choice with correct answer indicator
    if is_correct:
        return f"**{choice_letter}. {choice_text}** ✅"
    else:
        return f"{choice_letter}. {choice_text}"


def convert_json_to_markdown(json_file: str, output_file: str = None) -> None:
    """
    Convert JSON quiz data to markdown format.
    
    Args:
        json_file: Path to the input JSON file
        output_file: Path to the output markdown file (optional)
    """
    # Generate output filename if not provided
    if output_file is None:
        base_name = os.path.splitext(json_file)[0]
        output_file = f"{base_name}.md"
    
    try:
        # Read the JSON file
        print(f"Reading JSON file: {json_file}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("Error: Expected JSON array")
            return
        
        # Generate markdown content
        print("Converting to markdown format...")
        markdown_content = []
        
        # Add header
        markdown_content.append("# Azure Practice Questions\n")
        markdown_content.append(f"*Generated from {os.path.basename(json_file)}*\n")
        markdown_content.append("---\n")
        
        # Process each question
        for i, item in enumerate(data, 1):
            question_data = item.get("question", {})
            correct_choices = item.get("correctChoice", [])
            
            # Get question text and type
            question_text = format_question_text(question_data.get("text", ""))
            question_type = get_question_type(question_data)
            
            # Get correct choice IDs
            correct_ids = get_correct_choice_ids(correct_choices)
            
            # Add question header
            markdown_content.append(f"## Question {i}\n")
            markdown_content.append(f"**Type:** {question_type}\n")
            markdown_content.append(f"**Question:** {question_text}\n")
            
            # Add choices
            choices = question_data.get("choices", [])
            if choices:
                markdown_content.append("**Choices:**\n")
                for j, choice in enumerate(choices):
                    choice_letter = chr(65 + j)  # A, B, C, etc.
                    choice_markdown = convert_choice_to_markdown(choice, correct_ids, choice_letter)
                    markdown_content.append(f"- {choice_markdown}\n")
            
            # Add separator
            markdown_content.append("---\n")
        
        # Write markdown file
        print(f"Writing markdown file: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"Successfully converted {len(data)} questions to markdown")
        print(f"Output saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file}': {e}")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """Main function to run the script."""
    # Default input file
    input_file = "02_cleaned.json"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please make sure the cleaned JSON file is in the same directory as this script.")
        return
    
    # Convert to markdown
    convert_json_to_markdown(input_file)


if __name__ == "__main__":
    main() 