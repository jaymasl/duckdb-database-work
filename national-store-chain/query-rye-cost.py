import duckdb

# Connect to the DuckDB database
conn = duckdb.connect('national-store-chain.ddb')

# Query to get the cost of "Flour - Rye"
cost_query = conn.execute("""
    SELECT DISTINCT s.UnitPrice
    FROM Sales s
    JOIN Products p ON s.ProductId = p.ProductId
    WHERE p.ProductName = 'Flour - Rye'
""").fetchone()

# Extract the cost
cost_of_flour_rye = cost_query[0] if cost_query else None

# Print the result
if cost_of_flour_rye is not None:
    print(f"The cost of 'Flour - Rye' is: ${cost_of_flour_rye:.2f}")
else:
    print("The product 'Flour - Rye' is not found in the dataset.")

# Close the connection
conn.close()
