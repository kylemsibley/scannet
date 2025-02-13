# Ping Scan Network

A simple Python script to scan a network for active hosts using ICMP ping requests. I made this to replicate part of nmap's functionality in an environment where nmap is not allowed by policy. The script leverages the [ping3](https://github.com/kyan001/ping3) library to send pings to each host within a specified network range (in CIDR notation).

## Features

- **Network Scanning:** Scans a given network (CIDR notation, e.g., `192.168.1.0/24`) to identify active hosts.
- **Customizable Timeout:** Specify a timeout (in seconds) for each ping.
- **Verbose Mode:** Includes a verbose flag (currently prints a placeholder message).

## Prerequisites

- Python 3.6 or later
- [ping3](https://pypi.org/project/ping3/) library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies:**

   Install the required Python package using pip:

   ```bash
   pip install ping3
   ```

## Usage

Run the script from the command line. The script requires you to specify the network to scan in CIDR notation. You can also provide an optional timeout and enable verbose mode.

```bash
python script_name.py <network> [-t TIMEOUT] [-v]
```

### Arguments

- `<network>`: **(Required)** Network to scan (in CIDR notation, e.g., `192.168.1.0/24`).
- `-t, --timeout`: **(Optional)** Timeout in seconds for each ping (default is `1`).
- `-v, --verbose`: **(Optional)** Enable verbose output.

### Example

```bash
python script_name.py 192.168.1.0/24 -t 2 -v
```

## How It Works

1. **Argument Parsing:** Uses Python's `argparse` to handle command-line arguments.
2. **Network Validation:** Validates the input network using the `ipaddress` module.
3. **Scanning:** Iterates over each host in the network, pings it using the `ping3` library, and prints the IP address if the host is active.
4. **Output:** Displays a list of active hosts and a total count at the end.
