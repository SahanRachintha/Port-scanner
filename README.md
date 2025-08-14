
# Simple Port Scanner

## About
This **Simple Port Scanner** is a Python-based tool designed to scan open TCP ports on a target device, such as a local machine or a device on the same network (e.g., a mobile phone connected via hotspot). The project aims to help beginners understand the basics of port scanning, socket programming, and network security. By identifying open ports, users can detect potential security vulnerabilities and take steps to secure their devices.

**Disclaimer**: This tool is for **educational purposes only**. Unauthorized port scanning is illegal and unethical. Always obtain explicit permission before scanning any network or device.

## Features
- Scans a predefined list of TCP ports (e.g., 22, 80, 443, 8080, 5555) on a specified IP address.
- Uses Python’s `socket` module to check if ports are open or closed.
- Includes basic error handling for network issues and timeouts.
- Lightweight and beginner-friendly, with clear code for learning purposes.

## Limitations
- Requires manual editing of the IP address and ports in the source code.
- Supports only TCP scanning (no UDP).
- Scans ports sequentially (no multithreading for speed).

## Requirements
- Python 3.x
- No external libraries required (uses built-in `socket` module)
