# DataWave

DataWave is a versatile data transfer tool and library built on the powerful libcurl. Supporting a wide range of protocols including HTTP, FTP, MQTT, and more, DataWave makes it easy to transfer data using simple URL syntax.

## Features

- **Multiple Protocols**: Supports DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, LDAP, MQTT, POP3, RTMP, RTSP, SCP, SFTP, SMB, SMTP, TELNET, TFTP, WS, and WSS.
- **User-Friendly Interface**: Simple command-line interface to transfer data.
- **Extensible**: Easily extendable to support additional protocols.

## Getting Started

### Prerequisites

- [libcurl](https://curl.se/libcurl/)
- Python 3.x (or your preferred language)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akaday/DataWave.git
DataWave/
│
├── src/
│   ├── datawave/
│   │   ├── __init__.py
│   │   ├── httpget.py
│   │   ├── protocols.py
│   │   └── utils.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_httpget.py
│   │   └── test_protocols.py
│   └── main.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── setup.py
