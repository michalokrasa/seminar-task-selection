def calculate_outgoing_traffic(commands):
    participants = set()
    total_traffic = 0

    for command in commands:
        if command.startswith('+'):
            name = command[1:]
            participants.add(name)
        elif command.startswith('-'):
            name = command[1:]
            participants.discard(name)
        else:
            sender, message = command.split(':', 1)
            if sender in participants:
                message_length = len(message)
                total_traffic += message_length * len(participants)

    return total_traffic

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    commands = input().strip().split('\n')
    print(calculate_outgoing_traffic(commands))