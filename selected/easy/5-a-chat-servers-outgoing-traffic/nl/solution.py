def calculate_traffic(commands):
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
                total_traffic += len(message) * len(participants)

    return total_traffic
