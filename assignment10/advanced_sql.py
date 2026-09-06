import sqlite3

# Task 1: Complex JOINs with Aggregation
# Connect lesson database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Find the total price of each of the first 5 orders
query = """
SELECT o.order_id, SUM(l.quantity * p.price) AS total_price 
FROM orders AS o
JOIN line_items AS l
    ON o.order_id = l.order_id
JOIN products AS p 
    ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id 
LIMIT 5;
"""

cursor.execute(query)
print("Task 1: Complex JOINs with Aggregation")
for row in cursor.fetchall():
    print(f"Order {row[0]}: ${row[1]:.2f}")

conn.close()

# Task 2: Understanding Subqueries
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# For each customer, find the average price of their orders
query2 = """
SELECT c.customer_id, c.customer_name, AVG(sub.total_price) AS average_total_price
FROM customers AS c
JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(l.quantity * p.price) AS total_price 
    FROM orders AS o
    JOIN line_items AS l
    ON o.order_id = l.order_id
    JOIN products as p
    ON l.product_id = p.product_id
    GROUP BY o.order_id) AS sub 
    ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query2)
print("Task 2: Understanding Subqueries")
for customer_id, customer_name, average_total_price in cursor.fetchall():
    print(f"{customer_id}: {customer_name} - Average Price of Orders: {average_total_price}")

conn.close()

# Task 3: An Insert Transaction Based on Data 
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")

try:
    conn.execute("BEGIN TRANSACTION")
    # Retrieve customer_id
    cust_id = conn.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",),).fetchone()[0]

    # Retrieve employee_id
    emp_id = conn.execute("SELECT employee_id FROM employees WHERE last_name = ? AND first_name = ?", ("Harris", "Miranda",),).fetchone()[0]

    # Retrieve product_id of 5 least expensive products
    prod_ids = [row[0] for row in conn.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5").fetchall()]

    # Insert into results
    order_id = conn.execute("INSERT INTO orders (customer_id, employee_id) VALUES (?,?) RETURNING order_id", (cust_id, emp_id,),).fetchone()[0]

    for product_id in prod_ids:
        conn.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",(order_id, product_id, 10),)

    rows = conn.execute("SELECT l.line_item_id, l.quantity, p.product_name FROM line_items AS l JOIN products AS p ON p.product_id = l.product_id WHERE l.order_id = ?",(order_id,),).fetchall()

    # Print results
    print("Task 3: An Insert Transaction Based on Data ")
    for line_item_id, quantity, product_name in rows:
        print(f"line_item_id={line_item_id}, quantity={quantity}, product_name={product_name}")

    # Delete lines
    conn.execute("DELETE FROM line_items WHERE order_id = ?", (order_id,),)
    conn.execute("DELETE FROM orders WHERE order_id = ?", (order_id,),)

    conn.commit()
except Exception as e:
    conn.rollback()
    import traceback
    traceback.print_exc()
    print("Error: ", e)
finally:
    conn.close()

# Task 4: Aggregation with HAVING
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query4 = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o
ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;
"""

cursor.execute(query4)
print("Task 4: Aggregation with HAVING")
for employee_id, first_name, last_name, order_count in cursor.fetchall():
    print(employee_id, first_name, last_name, order_count)

conn.close()