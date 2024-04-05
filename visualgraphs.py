import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Graph 1 - Room Occupancy Rate Over Time

def graph1():

    conn1 = sqlite3.connect('hotel.db')

    # Query data from SQLite database for the second graph
    query1 = "SELECT arrival_year, arrival_month, arrival_date FROM bookings"
    df1 = pd.read_sql_query(query1, conn1)

    # Calculate check-in and check-out dates for each booking using the lead_time column
    # Handles the conversion of dates, including handling cases where the addition of days might result in a new month or year
    check_in_date = pd.to_datetime(df1['arrival_year'].astype(str) + '-' + df1['arrival_month'].astype(str) + '-' + df1['arrival_date'].astype(str))
    check_out_date = check_in_date + pd.to_timedelta(df1['lead_time'], unit='D')

    # Create a date range for the desired time period
    start_date = check_in_date.min()
    end_date = check_out_date.max()
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate occupancy rate per day
    occupancy_rate = []
    for date in date_range:
        num_occupied = ((check_in_date <= date) & (check_out_date > date)).sum()
        rate = num_occupied / len(df1)
        occupancy_rate.append(rate)

    # Plot the data as a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(date_range, occupancy_rate, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Occupancy Rate')
    plt.title('Room Occupancy Rate Over Time')
    plt.grid(True)
    plt.show()

    conn1.close()


# Graph 2 - Number of Bookings by Room Type

def graph2():

    conn2 = sqlite3.connect('hotel.db')

    # Query data from the database
    query2 = "SELECT room_type_reserved, COUNT(*) AS num_bookings FROM bookings GROUP BY room_type"
    df = pd.read_sql_query(query2, conn2)

    # Plot data in a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['room_type_reserved'], df['num_bookings'])
    plt.xlabel('Room Type')
    plt.ylabel('Number of Bookings')
    plt.title('Number of Bookings by Room Type')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the plot
    plt.show()
    conn2.close()


# Graph 3 - Current Occupany
    
def graph3():

    conn3 = sqlite3.connect('hotel.db')

    # Query data from SQLite database to get the number of occupied and vacant rooms
    query_occupied = "SELECT COUNT(*) FROM bookings WHERE check_in_date <= DATE('now') AND check_out_date >= DATE('now')"
    occupied_rooms = conn3.execute(query_occupied).fetchone()[0]
    total_rooms = 100  # Fixed total number of rooms is 100
    vacant_rooms = total_rooms - occupied_rooms

    # Calculate occupancy rate
    occupancy_rate = occupied_rooms / total_rooms * 100

    # Plot the data as a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie([occupied_rooms, vacant_rooms], labels=['Occupied', 'Vacant'], autopct='%1.1f%%', startangle=90)
    plt.title(f'Current Occupancy of the Hotel: {occupancy_rate:.1f}%')

    # Display the plot
    plt.show()

    conn3.close()



# Graph 4 - Average Stay Duration

def graph4():
    conn4 = sqlite3.connect('hotel.db')

    query4 = "SELECT lead_time FROM bookings"
    df = pd.read_sql_query(query4, conn4)

    # Calculate the average length of stay
    average_stay = df['lead_time'].mean()

    # Plot the data as a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(['Average Stay'], [average_stay])
    plt.ylabel('Length of Stay (days)')
    plt.title('Average Length of Stay')
    plt.show()

    conn4.close()



# Graph 5 - Cancelltion Rate
# REMOVE IF NOT NEEDED !!!

def graph5():
    conn5 = sqlite3.connect('hotel.db')
    
    # Query data from the database
    query = "SELECT booking_status, COUNT(*) as count FROM bookings GROUP BY booking_status"
    df = pd.read_sql_query(query, conn5)

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(df['count'], labels=df['booking_status'], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Cancellation Rate')
    plt.show()
    
    conn5.close()