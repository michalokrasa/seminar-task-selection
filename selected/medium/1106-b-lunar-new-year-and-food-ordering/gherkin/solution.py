def process_orders(n, m, quantities, costs, orders):
    results = []
    food_items = list(zip(quantities, costs, range(n)))
    food_items.sort(key=lambda x: (x[1], x[2]))  # Sort by cost, then by index

    for order_type, order_count in orders:
        order_type -= 1  # Convert to 0-based index
        total_cost = 0
        remaining_order = order_count

        # Try to fulfill the order with the preferred type first
        if quantities[order_type] > 0:
            served = min(quantities[order_type], remaining_order)
            total_cost += served * costs[order_type]
            quantities[order_type] -= served
            remaining_order -= served

        # If the order is not fully fulfilled, use the cheapest available
        for qty, cost, idx in food_items:
            if remaining_order <= 0:
                break
            if quantities[idx] > 0:
                served = min(quantities[idx], remaining_order)
                total_cost += served * cost
                quantities[idx] -= served
                remaining_order -= served

        results.append(total_cost)

    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    quantities = list(map(int, data[2:n+2]))
    costs = list(map(int, data[n+2:2*n+2]))
    
    orders = []
    index = 2*n+2
    for _ in range(m):
        order_type = int(data[index])
        order_count = int(data[index+1])
        orders.append((order_type, order_count))
        index += 2
    
    results = process_orders(n, m, quantities, costs, orders)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()