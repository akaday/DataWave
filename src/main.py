from datawave.httpget import DataWave

if __name__ == "__main__":
    datawave = DataWave()
    response = datawave.fetch_url("https://example.com")
    if response:
        print("HTTP Response:", response)
