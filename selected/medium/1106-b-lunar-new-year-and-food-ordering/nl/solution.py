def lunar_new_year_and_food_ordering(n, m, quantities, costs, orders):
    # Prepare a list of food types with their quantities and costs
    food = [(quantities[i], costs[i], i) for i in range(n)]
    # Sort food by cost, then by index to handle ties
    food.sort(key=lambda x: (x[1], x[2]))

    results = []

    for t, d in orders:
        total_cost = 0
        t -= 1  # Convert to zero-based index
        # Try to fulfill the order with the requested type first
        if quantities[t] > 0:
            served = min(quantities[t], d)
            total_cost += served * costs[t]
            quantities[t] -= served
            d -= served

        # If there are still dishes to serve, use the cheapest available
        for i in range(n):
            if d <= 0:
                break
            if quantities[food[i][2]] > 0:
                served = min(quantities[food[i][2]], d)
                total_cost += served * food[i][1]
                quantities[food[i][2]] -= served
                d -= served

        # If we couldn't serve all requested dishes, the customer leaves angrily
        if d > 0:
            total_cost = 0

        results.append(total_cost)

    return results

# Read input
n, m = map(int, input().split())
quantities = list(map(int, input().split()))
costs = list(map(int, input().split()))
orders = [tuple(map(int, input().split())) for _ in range(m)]

# Get results
results = lunar_new_year_and_food_ordering(n, m, quantities, costs, orders)

# Print results
for result in results:
    print(result)