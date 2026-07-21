# python-ioc-scanner
A Python-based IOC scanner that detects suspicious IP addresses by comparing log data against threat intelligence indicators

## Overview

A lightweight Python security tool designed to identify suspicious IP addresses by comparing observed network indicators against a known malicious IP list.

This project demonstrates basic SOC analyst workflows:
* IOC matching
* Threat intelligence usage
* Automated alert generation
* Security event triage

## Features

* Reads IP addresses from log files
* Compares against malicious IOC list
* Generates alerts when matches are found
* Provides alert count summary

## Example Output

IOC Scan Started

[HIGH] Suspicious IP detected: 185.220.101.5

[HIGH] Suspicious IP detected: 45.33.32.156

Total alerts: 2



