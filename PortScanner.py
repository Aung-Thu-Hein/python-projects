import socket

def scan_port(host, start_port, end_port):
    opened_ports = []
    closed_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:
            opened_ports.append(port)
        else:
            closed_ports.append(port)

        sock.close()

    return opened_ports, closed_ports

def main():
    host = input("Enter host: ")
    start_port = input("Enter start port: ")
    end_port = input("Enter end port: ")

    opened_ports, closed_ports = scan_port(host, int(start_port), int(end_port))

    if not opened_ports:
        print("No open ports are found!")
    else:
        print("Open ports= ", ", ".join(map(str, opened_ports)))

    if not closed_ports:
        print("No close ports are found!")
    else:
        print("Close ports= ", ", ".join(map(str, closed_ports)))


if __name__ == '__main__':
    main()
