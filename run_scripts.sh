#!/bin/bash


echo "Running the first script (scraping)..."
python3 scrape.py


echo "Running the second script (extracting text)..."
python3 htmlextract.py

echo "Scripts have been executed successfully."
