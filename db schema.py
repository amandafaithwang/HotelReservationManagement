import csv
import sqlite3

# defining global variables before use
global conn # connection
global cursor # cursor


# Connect to the sqlite database or create a new one if it doesn't exist
def connect_database():
    global conn, cursor
    # create a new one
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()


# Create rooms table if doesn't exist
# note: rooms show available rooms, includes only room id, room type, and average price per room
def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rooms (
            room_id INTEGER PRIMARY KEY,
            room_type TEXT NOT NULL,
            avg_price_per_room REAL NOT NULL
        )
    ''')

    # Create bookings table if doesn't exist
    # note: bookings can be edited, with add and delete booking
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            booking_id TEXT PRIMARY KEY,
            no_of_adults INTEGER NOT NULL,
            no_of_children INTEGER NOT NULL,
            room_type_reserved TEXT NOT NULL,
            lead_time INTEGER NOT NULL,
            arrival_year INTEGER NOT NULL,
            arrival_month INTEGER NOT NULL,
            arrival_date INTEGER NOT NULL,
            avg_price_per_room REAL NOT NULL,
            no_of_special_requests INTEGER NOT NULL
        )
    ''')

    # Use csv data, filter it, and insert into rooms and bookings tables
    # need to filter csv data because csv has a lot of columns/data we are excluding
    with open('small data set.csv', 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Rooms table
            cursor.execute('''
                INSERT INTO Rooms (room_type, avg_price_per_room)
                VALUES (?, ?)''', (row['room_type_reserved'],
                                   float(row['avg_price_per_room'])))

            # Bookings table
            booking_data = (
                row['Booking_ID'],
                int(row['no_of_adults']),
                int(row['no_of_children']),
                row['room_type_reserved'],
                int(row['lead_time']),  # lead time is duration of stay in days
                int(row['arrival_year']),
                int(row['arrival_month']),
                int(row['arrival_date']),
                float(row['avg_price_per_room']),
                int(row['no_of_special_requests'])
            )
            cursor.execute('''
                INSERT INTO Bookings (
                    booking_id,
                    no_of_adults, 
                    no_of_children, 
                    room_type_reserved, 
                    lead_time, 
                    arrival_year, 
                    arrival_month, 
                    arrival_date, 
                    avg_price_per_room, 
                    no_of_special_requests)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', booking_data)


# Commit the changes and close the connection
def close_database():
    conn.commit()
    conn.close()


# Run it
if __name__ == '__main__':
    connect_database()
    create_database()
    close_database()
