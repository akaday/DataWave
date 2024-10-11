import requests
import pycurl
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
import paramiko

class DataWave:
    def __init__(self):
        self.buffer = BytesIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buffer.write)

    def fetch_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    def fetch_ftp(self, ftp_url, username, password):
        self.buffer.seek(0)
        self.buffer.truncate()
        self.curl.setopt(pycurl.URL, ftp_url)
        self.curl.setopt(pycurl.USERNAME, username)
        self.curl.setopt(pycurl.PASSWORD, password)
        try:
            self.curl.perform()
            body = self.buffer.getvalue().decode('utf-8')
            return body
        except pycurl.error as e:
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

    def close(self):
        self.curl.close()
