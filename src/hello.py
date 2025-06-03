import duckdb
import os

def init_duckdb():
    # Create data_files directory if it doesn't exist
    os.makedirs('data_files', exist_ok=True)
    
    # Initialize DuckDB with PostgreSQL
    conn = duckdb.connect()
    
    # Execute initialization commands
    conn.execute("INSTALL ducklake;")
    conn.execute("INSTALL postgres;")
    conn.execute("ATTACH 'ducklake:postgres:dbname=ducklake host=db user=postgres password=postgres' AS my_ducklake (DATA_PATH 'data_files/');")
    conn.execute("USE my_ducklake;")
    
    # Create a sample table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS my_ducklake.sample_table (
            id INTEGER,
            name VARCHAR,
            value DOUBLE
        );
    """)
    
    # Insert sample data
    conn.execute("""
        INSERT INTO my_ducklake.sample_table VALUES 
        (1, 'Item 1', 10.5),
        (2, 'Item 2', 20.7),
        (3, 'Item 3', 15.3);
    """)
    
    # Query and display the data
    result = conn.execute("SELECT * FROM my_ducklake.sample_table").fetchall()
    print("\nSample Table Contents:")
    for row in result:
        print(row)
    
    # List all tables in the ducklake database
    print("\nAll Tables in DuckLake Database:")
    tables = conn.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """).fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f"\nContents of {table_name}:")
        try:
            table_data = conn.execute(f"SELECT * FROM __ducklake_metadata_my_ducklake.{table_name}").fetchall()
            for row in table_data:
                print(row)
        except Exception as e:
            print(f"Error reading table {table_name}: {str(e)}")
    
    conn.close()
    print("\nDuckDB initialization and data loading completed successfully!")

if __name__ == "__main__":
    init_duckdb()
    print("Hello from playwithducklake!")
