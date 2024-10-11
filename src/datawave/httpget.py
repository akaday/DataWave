import requests
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
import paramiko
from ftplib import FTP

class DataWave:
    def fetch_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    def fetch_ftp(self, ftp_url, username, password):
        try:
            ftp = FTP(ftp_url)
            ftp.login(user=username, passwd=password)
            data = []
            ftp.retrlines('RETR ' + '/path/to/remote/file', data.append)
            ftp.quit()
            return '\n'.join(data)
        except Exception as e:
            print(f"Failed to fetch {ftp_url}: {e}")

    def send_email(self, smtp_server, port, username, password, to_email, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to_email
        try:
            with smtplib.SMTP_SSL(smtp_server, port) as server:
                server.login(username, password)
                server.sendmail(username, [to_email], msg.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def fetch_sftp(self, hostname, port, username, password, remote_path):
        try:
            transport = paramiko.Transport((hostname, port))
            transport.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            with sftp.open(remote_path, 'r') as file:
                data = file.read().decode('utf-8')
            sftp.close()
            transport.close()
            return data
        except Exception as e:
            print(f"Failed to fetch SFTP: {e}")

if __name__ == "__main__":
    datawave = DataWave()
    
    # HTTP Example
    response = datawave.fetch_url("https://example.com")
    if response:
        print("HTTP Response:", response)
    
    # FTP Example
    ftp_response = datawave.fetch_ftp("ftp.example.com", "user", "password")
    if ftp_response:
        print("FTP Response:", ftp_response)
    
    # SMTP Example
    datawave.send_email("smtp.example.com", 465, "user@example.com", "password", "recipient@example.com", "Test Subject", "Email body")
    
    # SFTP Example
    sftp_response = datawave.fetch_sftp("sftp.example.com", 22, "user", "password", "/path/to/remote/file")
    if sftp_response:
        print("SFTP Response:", sftp_response)
