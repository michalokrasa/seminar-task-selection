def restore_internet_address(s):
    # Try to split the string into protocol, domain, and context
    for i in range(3, 5):  # protocol can be "http" (4) or "ftp" (3)
        protocol = s[:i]
        if protocol == "http" or protocol == "ftp":
            for j in range(i + 1, len(s) - 2):  # domain must be at least 1 character
                domain = s[i:j]
                if j < len(s) - 1:
                    context = s[j:]
                    # Construct the address
                    address = f"{protocol}://{domain}.ru/{context}"
                else:
                    address = f"{protocol}://{domain}.ru"
                print(address)
                return

import sys
input = sys.stdin.read
s = input().strip()
restore_internet_address(s)