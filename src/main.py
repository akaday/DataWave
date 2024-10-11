# src/main.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datawave.httpget import DataWave

if __name__ == "__main__":
    datawave = DataWave()
    response = datawave.fetch_url("https://example.com")
    if response:
        print("HTTP Response:", response)
