import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# Graph 1 - Room Occupancy Rate Over Time

class Graphs:
    
    def graph1():

        conn1 = sqlite3.connect('hotel.db')

        # Query data from SQLite database for the second graph
        query1 = "SELECT arrival_year, arrival_month, arrival_date, lead_time FROM Bookings"
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
            rate = num_occupied / len(df1)*100
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
        query2 = "SELECT room_type_reserved, COUNT(*) AS num_bookings FROM Bookings GROUP BY room_type_reserved"
        df = pd.read_sql_query(query2, conn2)

        # Plot data in a bar chart
        plt.figure(figsize=(10, 6))
        bars=plt.bar(df['room_type_reserved'], df['num_bookings'])
        plt.xlabel('Room Type')
        plt.ylabel('Number of Bookings')
        plt.title('Number of Bookings by Room Type')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        
        # Add annotations for each bar
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, yval, ha='center', va='bottom')


        # Display the plot
        plt.show()

        conn2.close()



    # Graph 3 - Current Occupany
    def graph3():

        conn3 = sqlite3.connect('hotel.db')

        # Query data from SQLite database to get the number of occupied and vacant rooms
        query_occupied = "SELECT SUM(num_bookings) FROM (SELECT COUNT(*) AS num_bookings FROM Bookings GROUP BY room_type_reserved)"
        occupied_rooms_str = conn3.execute(query_occupied).fetchone()[0]
        occupied_rooms = int(occupied_rooms_str) if occupied_rooms_str else 0
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
        
        query4 = "SELECT arrival_year, arrival_month, arrival_date, lead_time, room_type_reserved FROM Bookings"
        df4 = pd.read_sql_query(query4, conn4)

        # Convert check_in_date and check_out_date columns to datetime format
        check_in_date = pd.to_datetime(df4['arrival_year'].astype(str) + '-' + df4['arrival_month'].astype(str) + '-' + df4['arrival_date'].astype(str))
        check_out_date = check_in_date + pd.to_timedelta(df4['lead_time'], unit='D')

        # Calculate the length of stay for each booking
        df4['length_of_stay'] = (check_out_date - check_in_date).dt.days

        # Calculate the average length of stay for each room type
        average_stays = df4.groupby('room_type_reserved')['length_of_stay'].mean()

        # Plot the data as a bar chart
        plt.figure(figsize=(10, 6))
        bars = plt.bar(average_stays.index, average_stays.values)
        plt.xlabel('Room Type')
        plt.ylabel('Average Length of Stay (days)')
        plt.title('Average Length of Stay by Room Type')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Add the average values as text on top of each bar
        for bar, avg in zip(bars, average_stays.values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{avg:.2f}', ha='center', va='bottom')

        plt.show()

        conn4.close()

