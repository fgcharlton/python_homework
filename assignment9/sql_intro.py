import sqlite3 

# Task 3: Populate Tables with Data
def add_publishers(cursor, publisher_id, name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_id, name) VALUES (?,?)", (publisher_id, name))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazines(cursor, magazine_id, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (magazine_id, name, publisher_id) VALUES (?,?,?)", (magazine_id, name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscribers(cursor, subscriber_id, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (subscriber_id, name, address) VALUES (?,?,?)", (subscriber_id, name, address))
    except sqlite3.IntegrityError:
        print(f"{name} and {address} is already in the database.")

def add_subscriptions(cursor, subscription_id, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscription_id, subscriber_id, magazine_id, expiration_date) VALUES (?,?,?,?)", (subscription_id, subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print(f"{subscription_id} is already in the database.")

# Task 1: Create a New SQLite Database
try:
    with sqlite3.connect("db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor=conn.cursor()

        # Task 2: Define Database Structure
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                UNIQUE (name, address)
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            )
            """)

        print("Tables created successfully.")

        # Insert Data
        # Publishers table
        add_publishers(cursor, 1, "People Inc.")
        add_publishers(cursor, 2, "Forbes")
        add_publishers(cursor, 3, "National Geographic Society")

        # Magazines table
        add_magazines(cursor, 1, "People", 1)
        add_magazines(cursor, 2, "Travel + Leisure", 1)
        add_magazines(cursor, 3, "Forbes Magazine", 2)
        add_magazines(cursor, 4, "National Geographic Magazine", 3)
        add_magazines(cursor, 5, "National Geographic Traveler", 3)

        # Subscribers
        add_subscribers(cursor, 1, "Parker Robles", "101 Main Street")
        add_subscribers(cursor, 2, "Mason Gutierrez", "202 Main Street")
        add_subscribers(cursor, 3, "Liliana Wilkins", "303 Main Street")
        add_subscribers(cursor, 4, "Simone Abbott", "404 Main Street")

        # Subscriptions
        add_subscriptions(cursor, 1, 1, 1, "10/01/2027")
        add_subscriptions(cursor, 2, 1, 3, "10/01/2027")
        add_subscriptions(cursor, 3, 2, 2, "11/01/2027")
        add_subscriptions(cursor, 4, 2, 5, "11/01/2027")
        add_subscriptions(cursor, 5, 3, 4, "12/01/2027")
        add_subscriptions(cursor, 6, 4, 3, "01/01/2028")
        add_subscriptions(cursor, 7, 4, 1, "01/01/2028")

        conn.commit()
except Exception as e:
    print(f"Exception caught: {e}")

# Task 4: Write SQL Queries
# Retrieve all information from the subscribers table
cursor.execute("SELECT * FROM subscribers")
result = cursor.fetchall()
print("-------------Subscriberts Table-------------")
for row in result:
    print(row)

# Retrieve all magazines sorted by name
cursor.execute("SELECT * FROM magazines ORDER BY name")
result2 = cursor.fetchall()
print("-------------Magazines Table sorted by Magazine Name-------------")
for row2 in result2:
    print(row2)

# Retrieve magazines for a particular publishers, one of the publishers created
cursor.execute("SELECT m.name FROM publishers p JOIN magazines m on p.publisher_id = m.publisher_id WHERE p.name = 'National Geographic Society'")
result3 = cursor.fetchall()
print("-------------Magazines for National Geographic Society Publisher-------------")
for row3 in result3:
    print(row3)
