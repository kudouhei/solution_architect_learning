#!/usr/bin/env python3
"""
Final script to analyze markdown files and remove duplicate questions.
This script properly handles choice extraction and creates a clean consolidated markdown file.
"""

import re
import os
from typing import Dict, List, Set, Tuple


def extract_question_content(markdown_text: str) -> List[Dict[str, str]]:
    """
    Extract questions and their content from markdown text.
    
    Args:
        markdown_text: Raw markdown text
        
    Returns:
        List of question dictionaries with content and metadata
    """
    questions = []
    
    # Split by question sections
    question_sections = re.split(r'## Question \d+', markdown_text)
    
    for i, section in enumerate(question_sections[1:], 1):  # Skip first empty section
        lines = section.strip().split('\n')
        
        # Extract question type
        question_type = ""
        question_text = ""
        choices = []
        correct_choices = set()
        
        in_choices_section = False
        
        for line in lines:
            line = line.strip()
            if line.startswith('**Type:**'):
                question_type = line.replace('**Type:**', '').strip()
            elif line.startswith('**Question:**'):
                question_text = line.replace('**Question:**', '').strip()
            elif line.startswith('**Choices:**'):
                in_choices_section = True
            elif line.startswith('-') and in_choices_section:
                # Extract choice text and check if it's correct
                choice_text = line.replace('- ', '')
                
                # Check if this choice is marked as correct
                is_correct = '✅' in choice_text
                
                # Clean up the choice text - remove letter prefix and formatting
                choice_text = re.sub(r'^[A-Z]\.\s*', '', choice_text)  # Remove "A. ", "B. ", etc.
                choice_text = re.sub(r'\*\*[A-Z]\.\s*', '', choice_text)  # Remove "**A. ", "**B. ", etc.
                choice_text = re.sub(r'\*\*', '', choice_text)  # Remove remaining **
                choice_text = re.sub(r'✅', '', choice_text)  # Remove ✅
                choice_text = choice_text.strip()
                
                if choice_text and not choice_text.startswith('---'):
                    choices.append(choice_text)
                    if is_correct:
                        correct_choices.add(len(choices) - 1)  # Store index of correct choice
        
        if question_text:  # Only add if we have a valid question
            questions.append({
                'number': i,
                'type': question_type,
                'text': question_text,
                'choices': choices,
                'correct_choices': correct_choices,
                'full_content': section.strip()
            })
    
    return questions


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison by removing extra whitespace and special characters.
    
    Args:
        text: Text to normalize
        
    Returns:
        Normalized text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters that might differ between versions
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()


def find_duplicates(questions: List[Dict[str, str]]) -> List[Tuple[int, int]]:
    """
    Find duplicate questions based on normalized question text.
    
    Args:
        questions: List of question dictionaries
        
    Returns:
        List of tuples with indices of duplicate questions
    """
    duplicates = []
    normalized_texts = {}
    
    for i, question in enumerate(questions):
        normalized_text = normalize_text(question['text'])
        
        if normalized_text in normalized_texts:
            duplicates.append((normalized_texts[normalized_text], i))
        else:
            normalized_texts[normalized_text] = i
    
    return duplicates


def create_consolidated_markdown(unique_questions: List[Dict[str, str]], output_file: str) -> None:
    """
    Create a consolidated markdown file with unique questions.
    
    Args:
        unique_questions: List of unique question dictionaries
        output_file: Path to output markdown file
    """
    markdown_content = []
    
    # Add header
    markdown_content.append("# Azure Practice Questions (Consolidated)\n")
    markdown_content.append("*Generated from multiple sources with duplicates removed*\n")
    markdown_content.append("---\n")
    
    # Process each unique question
    for i, question in enumerate(unique_questions, 1):
        markdown_content.append(f"## Question {i}\n")
        markdown_content.append(f"**Type:** {question['type']}\n")
        markdown_content.append(f"**Question:** {question['text']}\n")
        
        # Add choices
        if question['choices']:
            markdown_content.append("**Choices:**\n")
            for j, choice in enumerate(question['choices']):
                choice_letter = chr(65 + j)  # A, B, C, etc.
                # Check if this choice is correct
                if j in question['correct_choices']:
                    markdown_content.append(f"- **{choice_letter}. {choice}** ✅\n")
                else:
                    markdown_content.append(f"- {choice_letter}. {choice}\n")
        
        markdown_content.append("---\n")
    
    # Write consolidated markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(markdown_content)


def process_markdown_files(file_paths: List[str], output_file: str = "final_consolidated_questions.md") -> None:
    """
    Process multiple markdown files and create a consolidated version without duplicates.
    
    Args:
        file_paths: List of markdown file paths to process
        output_file: Path to output consolidated markdown file
    """
    all_questions = []
    
    # Read and extract questions from all files
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File '{file_path}' not found, skipping...")
            continue
        
        print(f"Processing: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        questions = extract_question_content(content)
        print(f"  Found {len(questions)} questions")
        all_questions.extend(questions)
    
    print(f"\nTotal questions found: {len(all_questions)}")
    
    # Find duplicates
    duplicates = find_duplicates(all_questions)
    print(f"Found {len(duplicates)} duplicate pairs")
    
    # Show duplicate information
    for dup1, dup2 in duplicates:
        q1 = all_questions[dup1]
        q2 = all_questions[dup2]
        print(f"  Duplicate: Question {q1['number']} and Question {q2['number']}")
        print(f"    Text: {q1['text'][:100]}...")
    
    # Create list of unique questions (keep first occurrence)
    seen_texts = set()
    unique_questions = []
    
    for question in all_questions:
        normalized_text = normalize_text(question['text'])
        if normalized_text not in seen_texts:
            seen_texts.add(normalized_text)
            unique_questions.append(question)
    
    print(f"\nUnique questions: {len(unique_questions)}")
    print(f"Duplicates removed: {len(all_questions) - len(unique_questions)}")
    
    # Create consolidated markdown file
    create_consolidated_markdown(unique_questions, output_file)
    print(f"\nConsolidated markdown saved to: {output_file}")


def main():
    """Main function to run the script."""
    # Markdown files to process
    markdown_files = ["final_consolidated_questions.md", "08.md", "09.md"]
    
    # Check if files exist
    existing_files = [f for f in markdown_files if os.path.exists(f)]
    
    if not existing_files:
        print("Error: No markdown files found.")
        print("Please make sure the markdown files are in the same directory as this script.")
        return
    
    print(f"Processing {len(existing_files)} markdown files...")
    
    # Process the files
    process_markdown_files(existing_files)


if __name__ == "__main__":
    main() 