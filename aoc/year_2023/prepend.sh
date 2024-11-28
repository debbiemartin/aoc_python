#!/bin/bash

# Define the prefix you want to add
prefix="day_"

# Loop through all files matching the pattern
for file in *.py; do
  # Check if the file exists to avoid errors
  if [ -e "$file" ]; then
    # Rename the file by prepending the prefix
    mv "$file" "${prefix}${file}"
  fi
done
