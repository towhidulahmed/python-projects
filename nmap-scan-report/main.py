with open("nmap-scan.txt", "r") as file:
    lines = file.readlines()

for line in lines[1:]:  # Skip header
    line = line.strip()
    if line:
        parts = line.split()
        port = parts[0]
        state = parts[1]
        service = parts[2]

        if state == "open":
            print(f"Port: {port}, Service: {service}")
