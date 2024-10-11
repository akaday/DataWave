# src/datawave/httpget.py
import requests

class DataWave:
    def fetch_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

if __name__ == "__main__":
    datawave = DataWave()
    response = datawave.fetch_url("https://example.com")
    if response:
        print("HTTP Response:", response)
