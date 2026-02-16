"""
Simple Port Scanner
-------------------
Scans a target host for open TCP ports.

Usage:
    python port_scanner.py
"""

import socket

def scan_port(host, port):
    """Attempt to connect to a port and return whether it is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return True
        return False

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False


def main():
    print("=== Simple Port Scanner ===")
    host = input("Enter target host (e.g., 192.168.1.1): ")

    print(f"\nScanning host: {host}\n")

    for port in range(1, 1025):
        if scan_port(host, port):
            print(f"[OPEN] Port {port}")
    
    print("\nScan complete.")


if __name__ == "__main__":
    main()