# System Monitoring Program

## Overview
This script is a simple system monitoring tool that logs CPU, memory, and disk usage data to a file. It can also display real-time system usage in the terminal.

## Version
**v1.0.0**

## Creator
**Ilonczai András**

## Features
- Logs system information (CPU usage, memory usage, disk usage) to a file.
- Allows specification of the duration for data logging.
- Displays system information directly in the terminal.
- Provides version and creator information.
- Supports command-line arguments for flexible usage.

## Installation
To run this script, you need Python and the `psutil` library. If `psutil` is not installed, you can install it using:

```bash
pip install psutil
```

## Usage

# Display help message
- python script.py -h
- python script.py --help

# Show creator information
- python script.py -creator

# Show version information
- python script.py -v
- python script.py --version

# Log system data to file for a specified duration (in seconds)
- python script.py -make_data <duration>

# Log system data to file for a default duration
- python script.py -make_data

# Log system data for a duration of 1800 seconds (30 minutes)
- python script.py -make_data 1800

# Display system data in the terminal
- python script.py -stdout
