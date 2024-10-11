# src/main.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datawave.httpget import DataWave

if __name__ == "__main__":
    datawave = DataWave()
    
    # HTTP Example
    response = datawave.fetch_url("https://example.com")
    if response:
        print("HTTP Response:", response)
    
    # FTP Example
    ftp_response = datawave.fetch_ftp("ftp://example.com", "user", "password")
    if ftp_response:
        print("FTP Response:", ftp_response)
    
    datawave.close()
