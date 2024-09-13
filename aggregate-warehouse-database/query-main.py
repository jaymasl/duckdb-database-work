import duckdb

# Connect to the DuckDB database
con = duckdb.connect('warehouse.ddb')

# Execute the query to get the fulfillment percentage, including warehouses with 0% fulfillment
result = con.execute("""
    SELECT 
        Warehouse.warehouse_id, 
        CONCAT(Warehouse.state, ': ', Warehouse.warehouse_alias) AS warehouse_name, 
        COUNT(Orders.order_id) AS number_of_orders, 
        ROUND(COUNT(Orders.order_id) * 100.0 / NULLIF((SELECT COUNT(*) FROM Orders), 0), 2) || '%' AS fulfillment_percentage
    FROM Warehouse 
    LEFT JOIN Orders ON Orders.warehouse_id = Warehouse.warehouse_id 
    GROUP BY Warehouse.warehouse_id, warehouse_name 
    ORDER BY ROUND(COUNT(Orders.order_id) * 100.0 / NULLIF((SELECT COUNT(*) FROM Orders), 0), 2) DESC
""").fetchall()

# Print the results in a formatted way
print(f"{'Warehouse ID':<15} {'Warehouse Name':<40} {'Number of Orders':<20} {'Fulfillment %':<15}")
for row in result:
    print(f"{row[0]:<15} {row[1]:<40} {row[2]:<20} {row[3]:<15}")

con.close()
