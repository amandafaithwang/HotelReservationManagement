import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Graph 1 - Room Occupancy Rate Over Time

def graph1(database_filename):

    conn1 = sqlite3.connect('hotel.db')

    # Query data from SQLite database for the second graph
    query2 = "SELECT check_in_date, check_out_date FROM bookings"
    df2 = pd.read_sql_query(query2, conn1)

    # Convert check_in_date and check_out_date columns to datetime format for the second graph
    df2['check_in_date'] = pd.to_datetime(df2['check_in_date'])
    df2['check_out_date'] = pd.to_datetime(df2['check_out_date'])

    # Create a date range for the desired time period for the second graph
    start_date = df2['check_in_date'].min()
    end_date = df2['check_out_date'].max()
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate occupancy rate per day for the second graph
    occupancy_rate = []
    for date in date_range:
        num_occupied = ((df2['check_in_date'] <= date) & (df2['check_out_date'] > date)).sum()
        rate = num_occupied / len(df2)
        occupancy_rate.append(rate)

    root = tk.Tk()
    root.title("Room Occupancy Rate Over Time")

    frame2 = ttk.Frame(root)
    frame2.pack(fill=tk.BOTH, expand=1)

    # Plot the data as a histogram for the second graph
    fig2, ax2 = plt.subplots()
    ax2.hist(df2['stay_duration'], bins=20, edgecolor='black')
    ax2.set_xlabel('Stay Duration (days)')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Histogram of Stay Durations')

    # Embed the plot in the tkinter GUI for the second graph
    canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
    conn1.close()



# Graph 2 - Number of Bookings by Room Type

def graph2(database_filename):

    conn2 = sqlite3.connect('hotel.db')

    query = "SELECT room_type, COUNT(*) AS num_bookings FROM bookings GROUP BY room_type"
    df = pd.read_sql_query(query, conn2)

    root = tk.Tk()
    root.title("Number of Bookings by Room Type")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    # plot data in bar chart
    fig, ax = plt.subplots()
    ax.bar(df['room_type'], df['num_bookings'])
    ax.set_xlabel('Room Type')
    ax.set_ylabel('Number of Bookings')
    ax.set_title('Number of Bookings by Room Type')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
    conn2.close()




# Graph 3 - Current Occupany
    
def graph3(database_filename):

    conn3 = sqlite3.connect('hotel.db')

    # Query data from SQLite database to get the number of occupied and vacant rooms
    query_occupied = "SELECT COUNT(*) FROM bookings WHERE check_in_date <= DATE('now') AND check_out_date >= DATE('now')"
    query_total_rooms = "SELECT COUNT(*) FROM rooms"
    occupied_rooms = conn3.execute(query_occupied).fetchone()[0]
    total_rooms = conn3.execute(query_total_rooms).fetchone()[0]
    vacant_rooms = total_rooms - occupied_rooms

    # Create a tkinter GUI
    root = tk.Tk()
    root.title("Current Occupancy of the Hotel")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    # Plot the data as a pie chart
    fig, ax = plt.subplots()
    ax.pie([occupied_rooms, vacant_rooms], labels=['Occupied', 'Vacant'], autopct='%1.1f%%', startangle=90)
    ax.set_title('Current Occupancy of the Hotel')

    # Embed the plot in the tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
    conn3.close()



# Graph 4 - Average Stay Duration
def graph4(database_filename):

    conn4 = sqlite3.connect('hotel.db')

    query = "SELECT check_in_date, check_out_date FROM bookings"
    df = pd.read_sql_query(query, conn4)

    # Convert check_in_date and check_out_date columns to datetime format
    df['check_in_date'] = pd.to_datetime(df['check_in_date'])
    df['check_out_date'] = pd.to_datetime(df['check_out_date'])

    # Calculate stay duration for each booking
    df['stay_duration'] = (df['check_out_date'] - df['check_in_date']).dt.days

    root = tk.Tk()
    root.title("Average Stay Duration")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    # Plot data in histogram
    fig, ax = plt.subplots()
    ax.hist(df['stay_duration'], bins=20, edgecolor='black')
    ax.set_xlabel('Stay Duration (days)')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Stay Durations')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
    conn4.close()
