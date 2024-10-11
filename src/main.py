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
    
    # SMTP Example
    datawave.send_email("smtp.example.com", 465, "user@example.com", "password", "recipient@example.com", "Test Subject", "Email body")
    
    # SFTP Example
    sftp_response = datawave.fetch_sftp("sftp.example.com", 22, "user", "password", "/path/to/remote/file")
    if sftp_response:
        print("SFTP Response:", sftp_response)
    
    datawave.close()
