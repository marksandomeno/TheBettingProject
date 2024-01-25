#!/bin/bash

# Run the first Python script
echo "Running the first script (scraping)..."
python3 scrape.py

# Run the second Python script
echo "Running the second script (extracting text)..."
python3 htmlextract.py

echo "Scripts have been executed successfully."
