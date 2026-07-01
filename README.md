# Python Projects

This repository is a collection of my Python code from various projects. It centralizes all my Python scripts and tools into one convenient location.

## Included Projects

### OT Firmware Vulnerability Detection
This directory contains Python scripts used for analyzing OT firmware and detecting vulnerabilities.

* `yara-rules/time_cal.py`: Collects firmware paths and uses YARA rules for automated scanning or time calculation.
* `ghidra-tools/automate_cfg_count.py`: Automates Ghidra headless analysis to extract control flow graphs (CFG) from a list of test firmwares.
* `ghidra-tools/extract_cfg.py`: A Ghidra script designed to extract the control flow graph of a specific function ("extractForm").
* `ghidra-tools/runbinv3.py`: A utility that prompts for a firmware path and microcontroller type (like STM32, ESP8266, etc.) to initiate Ghidra headless analysis.
* `ghidra-tools/extract_all_cfg.py`: A Ghidra script that extracts the control flow graphs for all functions within an ELF binary.
* `ghidra-tools/comparision_updated.py`: Contains functions to convert address-based edges in a graph to abstract node labels, useful for comparing control flow graphs.

### 1-Wire Decoder Analysis
This folder contains code for decoding 1-Wire protocol data.

* `decode_1wire.py`: Reads 1-Wire protocol signal data from a CSV file and decodes it into binary format.

## Purpose
The main goal of this repository is to keep the essential code parts of my previous work organized and easily accessible for future reference or reuse.
