import duckdb

def init_db():
    # Connect to local DuckDB file
    conn = duckdb.connect("app_data.db")

    # Create users table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT,
            password TEXT,
            role TEXT CHECK(role IN ('admin', 'user'))
        )
    """)

    # Create devices table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            service_tag TEXT PRIMARY KEY,
            employee_id TEXT,
            device_type TEXT,
            memory TEXT
        )
    """)

    return conn
