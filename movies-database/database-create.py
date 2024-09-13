import duckdb

# Connect to your DuckDB database (this will create the file if it doesn't exist)
conn = duckdb.connect('movies-database.ddb')

# Create the movies table
conn.execute("""
CREATE TABLE movies (
    Movie_Title VARCHAR,
    Release_Date DATE,
    Wikipedia_URL VARCHAR,
    Genre VARCHAR,
    Director_1 VARCHAR,
    Director_2 VARCHAR,
    Cast_1 VARCHAR,
    Cast_2 VARCHAR,
    Cast_3 VARCHAR,
    Cast_4 VARCHAR,
    Cast_5 VARCHAR,
    Budget VARCHAR,
    Revenue VARCHAR
)
""")

# Import the CSV file into the database
conn.execute("COPY movies FROM 'movie-data.csv' (DELIMITER ',', HEADER TRUE)")

# Clean the Budget and Revenue columns to format them as floats
conn.execute("""
UPDATE movies
SET 
    Budget = REPLACE(REPLACE(Budget, '$', ''), ',', ''),
    Revenue = REPLACE(REPLACE(Revenue, '$', ''), ',', '')
""")

# Close the connection
conn.close()
