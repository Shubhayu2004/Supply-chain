import sqlite3
import os

def create_database():
    # Create database connection
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Create detection_results table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detection_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            detected_classes TEXT,
            result_image_path TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create inventory_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            quantity INTEGER DEFAULT 0,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database created successfully!")
    print("Tables created: detection_results, inventory_items")

if __name__ == "__main__":
    create_database() 