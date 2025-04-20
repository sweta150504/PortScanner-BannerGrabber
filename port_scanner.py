import socket

target = input("Enter the target IP address: ")

print(f"\nScanning target {target}...\n")

for port in [80, 135, 139, 443, 445, 3389]: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.3)
    print(f"Scanning port {port}...", end="\r")
    result = s.connect_ex((target, port))

    if result == 0:
        try:
            s.send(b'Hello\r\n')
            banner = s.recv(1024).decode().strip()
            print(f"Port {port} is open - Banner: {banner}")
            with open("scan_results.txt", "a") as f:
                f.write(f"Port {port} is open - Banner: {banner}\n")
        except:
            print(f"Port {port} is open - Banner not available")
    s.close()
