#!/usr/bin/env python3
# This script is intended to batch-convert notes with their tags in Logseq format, to standard YAML frontmatter.
# It will skip any files that lack Logseq tags, as well as any files that are alread using frontmatter.

import re
import sys
from pathlib import Path

def needs_conversion(content):
    """Check if the file needs conversion by looking for :: syntax before any bullet points."""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('-'):
            return False
        if '::' in line:
            return True
    return False

def has_frontmatter(content):
    """Check if the file already has YAML frontmatter."""
    return content.startswith('---\n')

def extract_metadata(content):
    """Extract metadata from Logseq format."""
    metadata = {}
    lines = content.split('\n')
    content_lines = []
    in_metadata = True
    
    for line in lines:
        if line.strip().startswith('-') or line.strip().startswith('#'):
            in_metadata = False
        
        if in_metadata:
            if '::' in line:
                key, value = line.split('::', 1)
                key = key.strip()
                value = value.strip()
                metadata[key] = value
        if not in_metadata or not '::' in line:
            content_lines.append(line)
    
    return metadata, '\n'.join(content_lines).strip()

def create_frontmatter(metadata):
    """Convert metadata dict to YAML frontmatter string."""
    if not metadata:
        return ''
    
    lines = ['---']
    for key, value in metadata.items():
        lines.append(f'{key}: {value}')
    lines.append('---\n')
    
    return '\n'.join(lines)

def convert_file(file_path):
    """Convert a single file from Logseq format to YAML frontmatter."""
    content = file_path.read_text()
    
    # Skip if file already has frontmatter
    if has_frontmatter(content):
        print(f"Skipping {file_path} - already has frontmatter")
        return
    
    # Skip if file doesn't need conversion
    if not needs_conversion(content):
        print(f"Skipping {file_path} - no metadata to convert")
        return
    
    # Extract metadata and content
    metadata, remaining_content = extract_metadata(content)
    
    

    # Create new content with frontmatter
    new_content = create_frontmatter(metadata)
    if remaining_content:
        new_content += "\n" + remaining_content

    # Write back to file
    file_path.write_text(new_content)
    print(f"Converted {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_logseq.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        sys.exit(1)
    
    # Process all markdown files in the directory
    for file_path in directory.glob('*.md'):
        try:
            convert_file(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    main()
