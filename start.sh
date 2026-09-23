#!/bin/sh
set -e

echo "=== Running advent of code 2025 ==="

for dir in day*/; do
    echo "--- Entering $dir ---"
    cd "$dir"
    
    for file in *.py; do
        echo "Running $file"
        python3 "$file"
    done
    
    cd ..
done

echo "=== all puzzles complete ==="
