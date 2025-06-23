# Nmap Scan Report Parser

This is a simple Python script to parse an Nmap scan output saved as a text file. It extracts and displays all open ports along with their corresponding services.

## Features

- Reads an Nmap report from a `.txt` file
- Parses each line to extract port, state, and service
- Filters and displays only open ports
- Can be easily extended for more features (e.g., output to CSV, XML parsing)

## Requirements

- Python 3.x
- A text file containing the output of an Nmap scan

## How to Generate the Nmap Report

You can generate a report by running:

```bash
nmap scanme.namp.org > nmap-scan.txt

