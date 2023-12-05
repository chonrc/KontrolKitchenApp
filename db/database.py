import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('restaurante.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Example: Insert data into the 'users' table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('john_doe', 'john@example.com'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
