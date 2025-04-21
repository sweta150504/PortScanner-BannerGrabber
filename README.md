# Port Scanner with Banner Grabbing

A simple yet powerful Python tool to scan ports on a target machine and grab service banners to identify potential vulnerabilities.

## :mag: What It Does

This project scans a range of ports on a given IP address or domain to identify:
- Which ports are open
- What services are running on those ports (using banner grabbing)

Banner grabbing helps in identifying:
- Service names (e.g., HTTP, FTP, SSH)
- Software versions
- Operating system details

## :lock: Why It Matters (Cyber Security Relevance)

This is a crucial step in the **reconnaissance phase** of ethical hacking. It helps identify vulnerable services before an attacker does, aiding in proactive security measures.

---

## :gear: How It Works

1. Takes input for the target IP and port range
2. Tries to connect to each port in the range
3. If a port is open, it attempts to grab the banner
4. Displays and saves the results to a file (`scan_results.txt`)

---

## :computer: Technologies Used

- **Python 3**
- `socket` module (for network connections)
- `sys`, `datetime` (for handling user input and logging)

---

## :rocket: How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/sweta150504/PortScanner-BannerGrabber.git
   cd PortScanner-BannerGrabbe
