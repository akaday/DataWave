# httpget.py
import pycurl
from io import BytesIO

class DataWave:
    def __init__(self):
        self.buffer = BytesIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buffer.write)

    def fetch_url(self, url):
        self.buffer.seek(0)
        self.buffer.truncate()
        self.curl.setopt(pycurl.URL, url)
        self.curl.perform()
        body = self.buffer.getvalue().decode('utf-8')
        return body

    def close(self):
        self.curl.close()

if __name__ == "__main__":
    url = "https://example.com"
    datawave = DataWave()
    response = datawave.fetch_url(url)
    print(response)
    datawave.close()
