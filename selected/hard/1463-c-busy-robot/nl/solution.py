def count_successful_commands(test_cases):
    results = []
    for case in test_cases:
        n, commands = case
        successful_count = 0
        current_position = 0
        current_time = 0
        target_position = 0
        target_time = 0
        moving = False

        for i in range(n):
            t_i, x_i = commands[i]

            if not moving:
                # Start moving towards the new target
                target_position = x_i
                target_time = t_i
                moving = True

            # Calculate the time to reach the current target
            time_to_target = abs(target_position - current_position)

            # Check if the robot can reach the target before the next command
            if current_time + time_to_target <= t_i:
                # Robot reaches the target
                current_position = target_position
                current_time += time_to_target
                moving = False

                # Check if the command is successful
                if current_position == x_i and current_time >= t_i:
                    successful_count += 1

                # Start moving towards the new target
                target_position = x_i
                target_time = t_i
                moving = True
            else:
                # Calculate the position of the robot at time t_i
                if target_position > current_position:
                    current_position += t_i - current_time
                else:
                    current_position -= t_i - current_time
                current_time = t_i

                # Check if the command is successful
                if current_position == x_i:
                    successful_count += 1

        # Check if the last command is successful
        if moving:
            time_to_target = abs(target_position - current_position)
            if current_time + time_to_target >= target_time:
                if current_position == target_position:
                    successful_count += 1

        results.append(successful_count)
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    commands = []
    for _ in range(n):
        t_i = int(data[index])
        x_i = int(data[index + 1])
        commands.append((t_i, x_i))
        index += 2
    test_cases.append((n, commands))

# Process each test case
results = count_successful_commands(test_cases)

# Output results
for result in results:
    print(result)