#!/bin/bash


echo "Scrape 🚜..."
python3 scrape.py

echo "OCR 🔬..."
python3 ocr_parse.py

echo "Scripts have been executed successfully."
