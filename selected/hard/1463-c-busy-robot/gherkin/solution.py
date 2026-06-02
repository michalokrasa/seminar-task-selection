def count_successful_commands(test_cases):
    results = []
    for commands in test_cases:
        current_position = 0
        current_time = 0
        target_position = None
        target_time = None
        successful_count = 0

        for time, target in commands:
            if target_position is None:
                # Start moving towards the new target
                target_position = target
                target_time = time
            else:
                # Calculate where the robot would be at the current command time
                time_elapsed = time - current_time
                if current_position < target_position:
                    current_position = min(target_position, current_position + time_elapsed)
                else:
                    current_position = max(target_position, current_position - time_elapsed)

                current_time = time

                # Check if the robot has reached the target
                if current_position == target_position:
                    successful_count += 1
                    target_position = None
                    target_time = None

            # If the robot is not moving or has reached the target, accept the new command
            if target_position is None:
                target_position = target
                target_time = time

        # Final check for the last target
        if target_position is not None:
            time_elapsed = commands[-1][0] - current_time
            if current_position < target_position:
                current_position = min(target_position, current_position + time_elapsed)
            else:
                current_position = max(target_position, current_position - time_elapsed)

            if current_position == target_position:
                successful_count += 1

        results.append(successful_count)
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    test_cases = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        commands = []
        for _ in range(n):
            time, target = map(int, data[index].split())
            commands.append((time, target))
            index += 1
        test_cases.append(commands)

    results = count_successful_commands(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()