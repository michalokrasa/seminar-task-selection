def process_ini_file(n, lines):
    import collections

    sections = collections.defaultdict(dict)
    current_section = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
        else:
            if '=' in line:
                key, value = map(str.strip, line.split('=', 1))
                sections[current_section][key] = value

    output = []
    if None in sections:
        global_keys = sorted(sections[None].items())
        for key, value in global_keys:
            output.append(f"{key}={value}")

    for section in sorted(k for k in sections if k is not None):
        output.append(f"[{section}]")
        section_keys = sorted(sections[section].items())
        for key, value in section_keys:
            output.append(f"{key}={value}")

    return '\n'.join(output)

# Read input
n = int(input().strip())
lines = [input().strip() for _ in range(n)]

# Process and print the result
print(process_ini_file(n, lines))