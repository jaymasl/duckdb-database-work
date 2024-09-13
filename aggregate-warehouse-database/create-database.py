import duckdb

# Create a DuckDB database and load CSV files
con = duckdb.connect('warehouse.ddb')
con.execute("""
    CREATE TABLE Orders AS SELECT * FROM read_csv_auto('Orders.csv');
    CREATE TABLE Warehouse AS SELECT * FROM read_csv_auto('Warehouse.csv');
""")
con.close()
