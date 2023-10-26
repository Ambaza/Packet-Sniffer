# Packet Sniffer

The Packet Sniffer is a Python application that allows you to capture and analyze network packets to identify and save POST requests containing specific filter data. It consists of two main files: `track.py` and `ui.py`.

## Features

- **Packet Capture:** The application captures network packets and monitors for POST requests.
- **Filtering:** You can specify an IP address, port, path, and filter data to capture specific POST requests.
- **Save POST Requests:** The application allows you to save captured POST requests to a file for later analysis.

## Components

### `track.py`

`track.py` is responsible for packet sniffing and POST request tracking. It utilizes the Scapy library to capture network packets and identify POST requests. Key components of `track.py` include:

- `PostDisplay`: A class for displaying and saving captured POST requests.
- `display_packet`: A function to display packets matching the target site and port and filter data.
- `start_sniffing`: A function to start sniffing packets based on specified criteria.
- `stop_sniffing`: A function to stop the packet capture.

### `ui.py`

`ui.py` is the user interface of the Packet Sniffer application, built using the Tkinter library. It provides an interface for users to set the IP address, port, path, and filter data for packet capture. Key features of `ui.py` include:

- Entry fields for specifying IP, port, path, and filter data.
- Start, stop, and save buttons to control packet capture and save POST requests.

## Prerequisites

Before using the Packet Sniffer application, ensure you have the following dependencies:

- Python 3.x
- Scapy library
- Tkinter (Python's standard GUI library)

## Usage

1. Start the Packet Sniffer application by executing `ui.py`:

   ```bash
   python ui.py
   ```

2. In the GUI window, provide the following information:

   - IP Address: The target site's IP address.
   - Port: The port to monitor.
   - Path: The path to capture (optional).
   - Filter: Data to filter POST requests (optional).

3. Click the "Start" button to begin packet capture.

4. To stop packet capture, click the "Stop" button.

5. To save captured POST requests, click the "Save" button, specify a file location, and click "Save."

## Known Issues

- Currently, there are no known issues.

## Author

- AMBAZA KIMANUKA Armand

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

The Packet Sniffer application is a handy tool for network administrators and developers who need to monitor and analyze network traffic for specific POST requests. It provides a user-friendly interface and robust packet capture capabilities.
