import requests
import pycurl
from io import BytesIO

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

    def close(self):
        self.curl.close()

