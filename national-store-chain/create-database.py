import duckdb
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

csv_files = {
    'Sales': 'Sales.csv',
    'Inventory': 'Inventory.csv',
    'Products': 'Products.csv'
}

def table_exists(conn, table_name):
    """Check if a table exists in the DuckDB database."""
    result = conn.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{table_name}'").fetchone()
    return result[0] > 0

# Connect to the DuckDB database using a context manager
try:
    with duckdb.connect('national-store-chain.ddb') as conn:
        # Iterate through each table and CSV file pair, creating tables if they don't exist
        for table_name, csv_file in csv_files.items():
            # Check if the table already exists
            if not table_exists(conn, table_name):
                # Attempt to create the table from the CSV
                logging.info(f"Loading {csv_file} into {table_name} table.")
                conn.execute(f"""
                    CREATE TABLE {table_name} AS 
                    SELECT * FROM read_csv_auto('{csv_file}', nullstr='NA')
                """)
                logging.info(f"Table '{table_name}' created successfully.")
            else:
                logging.info(f"Table '{table_name}' already exists. Skipping.")
except Exception as e:
    logging.error(f"Error occurred: {e}")
