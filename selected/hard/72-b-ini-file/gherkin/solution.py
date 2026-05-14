import sys
from collections import defaultdict

def format_ini_file(lines):
    sections = defaultdict(dict)
    current_section = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
            if current_section not in sections:
                sections[current_section] = {}
        else:
            if '=' in line:
                key, value = map(str.strip, line.split('=', 1))
                if current_section is None:
                    sections[None][key] = value
                else:
                    sections[current_section][key] = value

    output = []
    if None in sections:
        for key in sorted(sections[None]):
            output.append(f"{key}={sections[None][key]}")

    for section in sorted(k for k in sections if k is not None):
        output.append(f"[{section}]")
        for key in sorted(sections[section]):
            output.append(f"{key}={sections[section][key]}")

    return output

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    n = int(input_lines[0])
    lines = input_lines[1:n+1]
    formatted_lines = format_ini_file(lines)
    for line in formatted_lines:
        print(line)

if __name__ == "__main__":
    main()