# Projects Utilizing DuckDB for Database Management

## 1. Movies Database
- **Description**: A straightforward process to create and query a database containing a single table.

## 2. Aggregate Warehouse Database
- **Description**: This project processes two CSV files to create a database with two tables.
- **Files**:
  - `create-database.py`: Creates the database with two tables, `Orders` and `Warehouse`.
  - `query-main.py`: Joins the tables by `warehouse_id` and formats a list of warehouses along with their corresponding orders.

## 3. National Store Chain
- **Description**: This project takes three CSV files to create a database with three tables.
- **Files**:
  - `create-database.py`: Creates the database with three tables: `Inventory`, `Products`, and `Sales`.
  - `query-top-ten.py`: Returns a formatted table displaying stores, their best-selling products, and associated profits.