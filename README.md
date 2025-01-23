# AIORTC Raspberry Pi 4 SDP Offer Generator

This application is a Python-based WebRTC offer generator designed for the Raspberry Pi 4. It uses the `aiortc` library to create an SDP offer for one-way video and audio streaming. The video is captured from the Raspberry Pi Camera Module, and audio is captured from a USB microphone.

## Features
- Streams video from the official Raspberry Pi Camera Module.
- Streams audio from a USB microphone.
- Generates an SDP offer for one-way WebRTC connections on startup.
- Logs the SDP offer for use with a WebRTC-compatible client.

## Requirements
- Raspberry Pi 4 with Raspberry Pi OS installed.
- Raspberry Pi Camera Module (enabled via `raspi-config`).
- USB Microphone.
- Python 3.8 or newer.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Enable the Raspberry Pi Camera Module:
   ```bash
   sudo raspi-config
   ```
   - Navigate to **Interface Options > Camera** and enable it.
   - Reboot the Raspberry Pi.

## Usage
Run the application:
```bash
python aiortc_rpi4_sdp.py
```

### Output
The application will generate an SDP offer and log it to the console. Example:
```
SDP Offer created:
v=0
o=- 4611737206668326983 2 IN IP4 127.0.0.1
s=-
t=0 0
m=video 9 UDP/TLS/RTP/SAVPF 96
...
```
Copy the SDP offer and use it with a WebRTC-compatible client to establish a connection.

## Troubleshooting
- **No video output**: Ensure the Raspberry Pi Camera Module is properly connected and enabled.
- **No audio output**: Verify the USB microphone is connected and detected using `lsusb`.
- **Dependencies error**: Ensure Python 3.8 or newer is installed.

## License
This project is licensed under the MIT License.
