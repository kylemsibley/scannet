import ping3
import argparse
import ipaddress

def is_up(host, timeout):
    response = ping3.ping(host, timeout=timeout)
    return response is not None

def main():
    parser = argparse.ArgumentParser(
        description="Ping scan a network using ping3. Specify the network in CIDR notation (e.g., 192.168.1.0/24) and a timeout in seconds."
    )
    parser.add_argument("network", help="Network to scan (CIDR notation, e.g., 192.168.1.0/24)")
    parser.add_argument("-t", "--timeout", type=int, default=1, help="Timeout in seconds for each ping")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
    args = parser.parse_args()

    counter = 0

    if args.verbose:
        print(f"No verbose for you!!\n\n")

    try:
        net = ipaddress.ip_network(args.network, strict=False)
    except ValueError as e:
        print(f"invalid network: {e}")
        return

    print(f"Scanning for active hosts...\n\n")
    print(f"Active Hosts:")

    try:
        for ip in net.hosts():
            ip_str = str(ip)
            if is_up(ip_str, args.timeout):
                print(f"{ip_str}")
                counter = counter + 1
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        return

    print(f"\nTotal active hosts: {counter}\n")

if __name__ == "__main__":
    main()
