#!/usr/bin/env python3
"""
Script to convert JSON quiz data to markdown format.
This script handles the questionnaires structure and converts it to a markdown file
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


def convert_choice_to_markdown(choice: Dict[str, Any], choice_letter: str) -> str:
    """
    Convert a choice to markdown format.
    
    Args:
        choice: Choice object from JSON
        choice_letter: Letter identifier for the choice (A, B, C, etc.)
        
    Returns:
        Markdown formatted choice string
    """
    choice_text = clean_html_tags(choice.get("text", ""))
    is_correct = choice.get("isCorrect", False)
    
    # Format the choice with correct answer indicator
    if is_correct:
        return f"**{choice_letter}. {choice_text}** ✅"
    else:
        return f"{choice_letter}. {choice_text}"


def extract_questions_from_json(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract all questions from the JSON structure.
    
    Args:
        data: JSON data object
        
    Returns:
        List of question objects
    """
    questions = []
    
    # Handle the questionnaires structure
    if "questionnaires" in data:
        for questionnaire in data["questionnaires"]:
            if "questions" in questionnaire:
                questions.extend(questionnaire["questions"])
    # Handle direct questions array
    elif "questions" in data:
        questions = data["questions"]
    # Handle direct array of questions
    elif isinstance(data, list):
        questions = data
    
    return questions


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
        
        # Extract questions from the JSON structure
        questions = extract_questions_from_json(data)
        
        if not questions:
            print("Error: No questions found in the JSON file")
            return
        
        # Generate markdown content
        print(f"Converting {len(questions)} questions to markdown format...")
        markdown_content = []
        
        # Add header
        markdown_content.append("# Azure Practice Questions\n")
        markdown_content.append(f"*Generated from {os.path.basename(json_file)}*\n")
        markdown_content.append("---\n")
        
        # Process each question
        for i, question in enumerate(questions, 1):
            # Get question text and type
            question_text = format_question_text(question.get("text", ""))
            question_type = get_question_type(question)
            
            # Add question header
            markdown_content.append(f"## Question {i}\n")
            markdown_content.append(f"**Type:** {question_type}\n")
            markdown_content.append(f"**Question:** {question_text}\n")
            
            # Add choices
            choices = question.get("choices", [])
            if choices:
                markdown_content.append("**Choices:**\n")
                for j, choice in enumerate(choices):
                    choice_letter = chr(65 + j)  # A, B, C, etc.
                    choice_markdown = convert_choice_to_markdown(choice, choice_letter)
                    markdown_content.append(f"- {choice_markdown}\n")
            
            # Add separator
            markdown_content.append("---\n")
        
        # Write markdown file
        print(f"Writing markdown file: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(markdown_content)
        
        print(f"Successfully converted {len(questions)} questions to markdown")
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
    input_file = "07.json"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please make sure the JSON file is in the same directory as this script.")
        return
    
    # Convert to markdown
    convert_json_to_markdown(input_file)


if __name__ == "__main__":
    main() 