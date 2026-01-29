"""

This module extracts documentation from AI project folders
for building a Digital Twin knowledge base.

Author: Apurva Billuri
Purpose: Learning professional Python while building RAG system
"""

from pathlib import Path
from typing import List


def find_readme_files(projects_dir: Path) -> List[Path]:
    """
    Find all README.md files in project subdirectories.
    
    Args:
        projects_dir: Path to the parent directory containing projects
        
    Returns:
        List of Path objects pointing to README.md files
        
    Example:
        >>> projects = Path("/Users/apurva/Projects/AI_Agents")
        >>> readmes = find_readme_files(projects)
        >>> print(len(readmes))
        2
    """
    pattern = "*/README.md"
    return list(projects_dir.glob(pattern))


def find_docs_files(projects_dir: Path) -> List[Path]:
    """
    Find all markdown files in docs/ subdirectories.
    
    Args:
        projects_dir: Path to the parent directory containing projects
        
    Returns:
        List of Path objects pointing to .md files in docs folders
    """
    pattern = "*/docs/*.md"
    return list(projects_dir.glob(pattern))


def read_file_with_stats(file_path: Path) -> dict:
    """
    Read a file and return its content with statistics.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        Dictionary containing:
            - content: Full text content
            - word_count: Number of words
            - char_count: Number of characters
            - preview: First 100 characters
            
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        return {
            'content': content,
            'word_count': len(content.split()),
            'char_count': len(content),
            'preview': content[:100]
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def display_file_preview(file_path: Path, stats: dict) -> None:
    """
    Print a formatted preview of a file's statistics.
    
    Args:
        file_path: Path to the file
        stats: Statistics dictionary from read_file_with_stats()
    """
    # Build relative path for display
    if file_path.name == "README.md":
        display_path = f"{file_path.parent.name}/README.md"
    else:
        display_path = f"{file_path.parent.parent.name}/{file_path.parent.name}/{file_path.name}"
    
    print(f"\n📄 {display_path}")
    print(f"   Words: {stats['word_count']:,}")
    print(f"   Preview: {stats['preview']}...")


def main() -> None:
    """Main execution function."""
    # Configuration
    projects_folder = Path("/Users/apurva/Projects/AI_Agents")
    
    # Step 1: Find all documentation files
    print("🔍 Finding README files...")
    readme_files = find_readme_files(projects_folder)
    print(f"   Found {len(readme_files)} README files\n")
    
    print("🔍 Finding documentation files...")
    docs_files = find_docs_files(projects_folder)
    print(f"   Found {len(docs_files)} doc files\n")
    
    # Step 2: Combine lists
    all_docs = readme_files + docs_files
    print(f"📊 Total files to process: {len(all_docs)}\n")
    
    # Step 3: Preview first 3 files
    print("=" * 60)
    print("Preview of first 3 files:")
    print("=" * 60)
    
    for doc_file in all_docs[:3]:
        try:
            stats = read_file_with_stats(doc_file)
            display_file_preview(doc_file, stats)
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")


# Professional Python pattern: only run if executed directly
if __name__ == "__main__":
    main()