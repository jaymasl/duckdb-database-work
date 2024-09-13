import duckdb

# Connect to your DuckDB database
conn = duckdb.connect('movies-database.ddb')

# Run a query
result = conn.execute("""
SELECT Movie_Title, 
    strftime('%Y-%m-%d', Release_Date) AS Release 
FROM movies 
WHERE Release_Date 
    BETWEEN DATE '2015-01-01' AND DATE '2015-08-01' 
    AND Genre = 'Comedy'
    AND CAST(Budget AS FLOAT) > 50000000
ORDER BY Release ASC;
""").fetchall()

# Print the results
for row in result:
    print(row)

# Close the connection
conn.close()
