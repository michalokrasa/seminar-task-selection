def restore_address(s):
    # Determine the protocol
    if s.startswith("http"):
        protocol = "http"
        s = s[4:]
    elif s.startswith("ftp"):
        protocol = "ftp"
        s = s[3:]
    else:
        return "Invalid input"

    # Find the position of ".ru"
    ru_pos = s.find("ru")
    if ru_pos == -1:
        return "Invalid input"

    # Extract domain and context
    domain = s[:ru_pos]
    context = s[ru_pos + 2:]

    # Construct the result
    if context:
        result = f"{protocol}://{domain}.ru/{context}"
    else:
        result = f"{protocol}://{domain}.ru"

    return result

import sys
input = sys.stdin.read().strip()
print(restore_address(input))