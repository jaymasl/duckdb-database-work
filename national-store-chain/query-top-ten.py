import duckdb
from prettytable import PrettyTable

# Configurable constants
TOP_N = 10  # Number of top stores to fetch

# Connect to the DuckDB database using context manager for automatic resource management
with duckdb.connect('national-store-chain.ddb') as conn:
    
    # Query to get the top stores by total sales, their most sold product, unit price, product cost, and profit
    query = f"""
        WITH StoreSales AS (
            SELECT 
                i.StoreName, 
                SUM(s.UnitPrice * s.Quantity) AS TotalSales,
                s.ProductId,
                SUM(s.Quantity) AS TotalQuantity
            FROM Sales s
            JOIN Inventory i ON s.StoreId = i.StoreId
            GROUP BY i.StoreName, s.ProductId
        ),
        RankedSales AS (
            SELECT 
                StoreName, 
                TotalSales, 
                ProductId,
                TotalQuantity,
                ROW_NUMBER() OVER (PARTITION BY StoreName ORDER BY TotalQuantity DESC) AS rn
            FROM StoreSales
        )
        SELECT 
            rs.StoreName, 
            ROUND(rs.TotalSales, 2) AS TotalSales, 
            p.ProductName,
            ROUND(AVG(s.UnitPrice), 2) AS UnitPrice,  -- Calculate average unit price
            ROUND(p.ProductCost, 2) AS ProductCost
        FROM RankedSales rs
        JOIN Products p ON rs.ProductId = p.ProductId
        JOIN Sales s ON rs.ProductId = s.ProductId
        WHERE rs.rn = 1
        GROUP BY rs.StoreName, rs.TotalSales, p.ProductName, p.ProductCost
        ORDER BY rs.TotalSales DESC
        LIMIT {TOP_N}
    """
    result = conn.execute(query).fetchall()

    # Query to find the date range in the dataset
    start_date, end_date = conn.execute("SELECT MIN(Date), MAX(Date) FROM Sales").fetchone() or (None, None)

# Prepare and display the table
table = PrettyTable(["Store Name", "Total Sales ($)", "Most Sold Product", "Unit Price ($)", "Product Cost ($)", "Profit ($)"])

for row in result:
    store_name, total_sales, most_sold_product, unit_price, product_cost = row
    # Calculate profit, guard against division by zero
    profit = (unit_price - product_cost) * (total_sales / unit_price) if unit_price else 0
    table.add_row([
        store_name, 
        f"${total_sales:,.2f}", 
        most_sold_product, 
        f"${unit_price:,.2f}", 
        f"${product_cost:,.2f}", 
        f"${profit:,.2f}"
    ])

# Print the results
print(table)
if start_date and end_date:
    print(f"Dataset spans from {start_date} to {end_date}.")
else:
    print("No sales data available.")
