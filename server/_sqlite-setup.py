import sys
import sqlite3
from config.sqlite import DB_FILENAME

def execute_sql_file(sql_file_path):
    """
    Loads SQL commands from a file and executes them in a SQLite database.

    Args:
        sql_file_path (str): The path to the file containing SQL commands.
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        cursor = conn.cursor()

        with open(sql_file_path, 'r') as f:
            sql_script = f.read()

        cursor.executescript(sql_script)
        conn.commit()
        print(f"SQL commands from '{sql_file_path}' executed successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except FileNotFoundError:
        print(f"Error: SQL file not found at '{sql_file_path}'")
    finally:
        if conn:
            conn.close()



if __name__ == "__main__":
    execute_sql_file("migrations/sqlite-setup.sql")
