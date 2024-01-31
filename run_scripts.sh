#!/bin/bash


echo "Scrape 🚜..."
python3 scrape.py

echo "OCR 🔬..."
python3 ocrparse.py

echo "Scripts have been executed successfully."
