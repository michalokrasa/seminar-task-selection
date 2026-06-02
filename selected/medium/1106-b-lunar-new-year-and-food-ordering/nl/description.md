# Lunar New Year and Food Ordering

## Goal

Determine the total cost charged to each customer at a restaurant with limited stock and a cheapest-available fallback rule.

## Rules

- The restaurant has `n` food types; type `i` has `a_i` dishes remaining and costs `c_i` per dish.
- Customers are served one at a time. For each dish a customer requests of type `t`:
  1. If type `t` has stock, serve one dish of type `t` (cost `c_t`, stock decreases by 1).
  2. If type `t` is out of stock, serve one dish of the **cheapest available** type; ties broken by smallest index.
  3. If **no food remains at all**, the customer **leaves angrily** — their total cost is 0 regardless of dishes already served.
- Output the total cost for each customer in order.

## Input / Output

- **Input**: line 1 — `n m`; line 2 — `a_1 … a_n` (quantities); line 3 — `c_1 … c_n` (costs); next `m` lines — `t_j d_j` (type and dish count for customer `j`).
- **Output**: `m` lines; line `j` is the cost charged to customer `j`.
