These are my projects using solely duckdb to create, manipulate, and query databases. 

movies-database:
a basic process to create and query a database with a single table. 

aggregate-warehouse-database:
takes two .csv files and creates a database with two tables.
create-database.py creates the database with two tables, Orders.csv and Warehouse.csv.
query-main.py joins by warehouse_id and formats list of the warehouses and their orders.
