#!/bin/bash

# Find and ignore files larger than 10MB
find . -type f -size +10M > large_files.txt

# Create or append to .gitignore
while read -r file; do
    echo "$file" >> .gitignore
done < large_files.txt

# Clean up
rm large_files.txt

