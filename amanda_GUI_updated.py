"""This file contains the code for creating Tkinter GUI elements, such as windows, forms, buttons, etc."""
import tkinter as tk
import sqlite3
from tkinter import ttk, \
    messagebox  # ttk is the themed tk module for widgets that look like the OS, and messagebox is for displaying alerts
from tkinter import Tk
from PIL import ImageTk, Image  # Import the ImageTk and Image modules from the PIL package for working with images
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LoginWindow:  # Class for the Log In Window to enter username and password to access the main GUI
    def __init__(self, master):
        self.master = master
        self.master.title("Log In to the Hotel Reservation Management System")
        self.master.configure(bg="white")  # Set the background color of the window to white

        # Calculate the coordinates for the top left corner of the window to center it
        window_width = 400
        window_height = 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)  # Calculate the top position
        position_right = int(screen_width / 2 - window_width / 2)  # Calculate the right position

        # Set the geometry of the window using the calculated coordinates at the center of the screen
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create the widgets for the Log In Window
        logo = Image.open("logo.png")  # Load the logo image
        logo = logo.resize((250, 150), Image.LANCZOS)  # Resize the logo image
        logo = ImageTk.PhotoImage(logo)  # Load the logo image
        logo_widget = ttk.Label(master, image=logo)  # Create a label widget to display the logo
        logo_widget.image = logo  # Keep a reference to the image to prevent garbage collection
        logo_widget.pack()

        self.label_username = ttk.Label(master, text="Username:", background="white")
        self.label_username.pack()

        self.entry_username = ttk.Entry(master)
        self.entry_username.pack()

        self.label_password = ttk.Label(master, text="Password:", background="white")
        self.label_password.pack()

        self.entry_password = ttk.Entry(master,
                                        show="*")  # Show * instead of the actual password to resemble a password field
        self.entry_password.pack()

        self.button = ttk.Button(master, text="Log In", command=self.login)
        self.button.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print("Username: " + username)
        print("Password: " + password)

        # Check if username and password are alphanumeric
        if username.isalnum() and password.isalnum():
            messagebox.showinfo("Login Successful", "Welcome to the Hotel Reservation Management System!")
            print("Login successful")
            self.master.destroy()  # Close the Log In Window after successful login and open the main window
            root = Tk()
            my_gui = GUI(root)  # Open the main GUI  after successful login
            root.mainloop()  # Start the main GUI
        else:
            messagebox.showinfo("Login failed", "Invalid username or password. Please try again.")


class SearchPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Search Filters")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Arrival Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
        self.arrival_date = ttk.Entry(self)
        self.arrival_date.grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Length of Stay (days):").grid(row=1, column=0, sticky="w")
        self.length_of_stay = ttk.Entry(self)
        self.length_of_stay.grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="Number of Adults:").grid(row=2, column=0, sticky="w")
        self.no_of_adults = ttk.Entry(self)
        self.no_of_adults.grid(row=2, column=1, sticky="ew")

        ttk.Label(self, text="Number of Children:").grid(row=3, column=0, sticky="w")
        self.no_of_children = ttk.Entry(self)
        self.no_of_children.grid(row=3, column=1, sticky="ew")

        ttk.Label(self, text="Room Type:").grid(row=4, column=0, sticky="w")
        self.room_type = ttk.Combobox(self, values=["Single", "Double", "Suite"])
        self.room_type.grid(row=4, column=1, sticky="ew")

        ttk.Button(self, text="Search", command=self.search_rooms).grid(row=5, column=0, columnspan=2, pady=5)

    def search_rooms(self):
        # This method will be updated to perform the actual search
        print("Searching for rooms...")
        self.destroy()


class Dashboard:  # So far this class contains Amanda's code for the dashboard.py
    def __init__(self, master):
        self.master = master

        # Create widgets similar to dashboard amanda.py
        self.create_widgets()
        self.create_dashboard_placeholder()
        self.create_room_details_section()
        self.create_room_status_section()
        self.create_bookings_section()

    def create_widgets(self):
        search_btn = ttk.Button(self.master, text="Search Rooms", command=self.open_search_popup)
        search_btn.pack(pady=20)

    def open_search_popup(self):
        popup = SearchPopup(self.master)
        popup.grab_set()

    def create_dashboard_placeholder(self):
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.set_title('Visualization Placeholder')
        plot.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_room_details_section(self):
        room_details_frame = ttk.LabelFrame(self.master, text="Room Details")
        room_details_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_details_frame, text="Price:").grid(row=0, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_details_frame, text="Capacity:").grid(row=1, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=1, column=1)

    def create_room_status_section(self):
        room_status_frame = ttk.LabelFrame(self.master, text="Room Status")
        room_status_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_status_frame, text="Occupied:").grid(row=0, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_status_frame, text="Available:").grid(row=1, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=1, column=1)

    def create_bookings_section(self):
        bookings_frame = ttk.LabelFrame(self.master, text="Current Bookings")
        bookings_frame.pack(fill="both", expand=True, padx=20, pady=10)
        columns = ("booking_id", "room_type", "stay_length", "check_in", "check_out")
        self.bookings_table = ttk.Treeview(bookings_frame, columns=columns, show="headings")
        for col in columns:
            self.bookings_table.heading(col, text=col.replace("_", " ").title())
            self.bookings_table.column(col, anchor="center")
        self.bookings_table.pack(fill="both", expand=True)

        # Placeholder for sample booking data
        sample_data = [("B001", "Suite", "3", "2023-10-01", "2023-10-04"),
                       ("B002", "Double", "2", "2023-10-02", "2023-10-04")] * 5  # Multiplied to exceed 10 entries

        # Insert only the first 10 entries
        for booking in sample_data[:10]:
            self.bookings_table.insert("", "end", values=booking)


class Rooms:  # This class contains the code for the Rooms section of the GUI
    def __init__(self, master):
        self.master = master

    def create_rooms_display(self):
        """This method should contain the code to create and display the rooms section."""
        pass


class Bookings:  # This class contains the code for the Bookings section of the GUI to manage bookings
    def __init__(self, master):
        self.master = master
        self.bookings_frame = ttk.Frame(master)  # Create a frame to hold the bookings section
        self.bookings_frame.pack(fill='both', expand=True)  # Pack the frame to fill the window

    def create_bookings_display(self):
        # this is the search bookings button
        ttk.Button(self.bookings_frame, text="Search Bookings", command=self.open_search_window).pack(pady=10)
        # setting the page to zero
        self.current_page = 0

        # Access db and select and fetch all of the data
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        # select everything from the bookings table
        cursor.execute("SELECT * FROM bookings")
        # fetch all the selected data
        data = cursor.fetchall()
        # Close the database
        conn.close()
        print(data)

        self.bookings = data

        # using Treeview to make and populate table
        # defining columns
        #self.bookings = ["1", "2", "3", "4"] *200
        self.bookings_display = ttk.Treeview(self.bookings_frame, columns=("Booking ID", "# of Adults", "# of Children", "Room Type", "Lead Time", "Arrival Year", "Arrival Month", "Arrival Date", "Average Price of Room", "# of Special Requests"), show="headings")
        self.bookings_display.pack(fill='both', expand=True)
        for col in self.bookings_display['columns']:
            self.bookings_display.heading(col, text=col)

        # formats the columns to fit to the page by setting the width
        self.bookings_display.column("#0", width=0, stretch=tk.NO)
        self.bookings_display.column("Booking ID", anchor=tk.CENTER, width=90)
        self.bookings_display.column("# of Adults", anchor=tk.CENTER, width=100)
        self.bookings_display.column("# of Children", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Room Type", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Lead Time", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Arrival Year", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Arrival Month", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Arrival Date", anchor=tk.CENTER, width=100)
        self.bookings_display.column("Average Price of Room", anchor=tk.CENTER, width=110)
        self.bookings_display.column("# of Special Requests", anchor=tk.CENTER, width=100)


        # Pack Treeview
        #self.bookings_display.pack(expand=True, fill=tk.BOTH)

        # Run Tkinter event loop
        #tk.Tk.mainloop()


        # next/previous page buttons
        pagination_frame = ttk.Frame(self.bookings_frame)
        pagination_frame.pack(fill='x', expand=False)
        ttk.Button(pagination_frame, text="<<", command=self.prev_page).pack(side='left')
        self.page_number_label = ttk.Label(pagination_frame, text=f"Page {self.current_page + 1}")
        self.page_number_label.pack(side='left', padx=10)
        ttk.Button(pagination_frame, text=">>", command=self.next_page).pack(side='left')

        # CRUD buttons frame
        crud_frame = ttk.Frame(self.bookings_frame)
        crud_frame.pack(fill='x', pady=5)

        # Create button
        top_frame = ttk.Frame(self.bookings_frame)
        top_frame.pack(fill='x', side='top')
        ttk.Button(top_frame, text="Create Booking", command=self.create_booking).pack(side='right', padx=5)

        # Update button
        action_frame = ttk.Frame(self.bookings_frame)
        action_frame.pack(fill='x', side='bottom', pady=5)
        self.update_btn = ttk.Button(action_frame, text="Update Booking", state='normal', command=self.update_booking)
        self.update_btn.pack(side='left', padx=5)
        self.delete_btn = ttk.Button(action_frame, text="Delete Booking", state='normal', command=self.delete_booking)
        self.delete_btn.pack(side='left', padx=5)
        self.bookings_display.bind('<<TreeviewSelect>>', self.on_item_selected)

        self.update_bookings_display()

    def on_item_selected(self, event):
        selected = self.bookings_display.selection()
        if selected:  # If an item is selected, enable the update and delete buttons
            self.update_btn['state'] = 'normal'
            self.delete_btn['state'] = 'normal'
        else:  # No selection disables the buttons
            self.update_btn['state'] = 'normal'
            self.delete_btn['state'] = 'normal'

    def delete_booking(self):
        selected_item = self.bookings_display.selection()
        if selected_item:  # Ensure there's a selected item
            # Fetch the item's details
            item = self.bookings_display.item(selected_item[0], 'values')
            booking_id = item[0]  # Assuming the first column is the booking ID
            print(f"Deleting booking ID: {booking_id}")
            # Add your logic here to delete the booking from your data store using the booking_id
            # ===================================================================================================================================NEW CODE HERE
            conn = sqlite3.connect('hotel.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Bookings WHERE booking_id= ?", booking_id)
            conn.commit()
            conn.close()
            # Then delete the item from the Treeview
            self.bookings_display.delete(selected_item[0])
            messagebox.showinfo("Success", f"Booking ID {booking_id} deleted")
        else:
            messagebox.showinfo("Error", "No booking selected")

    def open_search_window(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Search Bookings")
        self.search_window.geometry("300x200")  # Adjust size as needed

        # Example search filters: Booking ID and Room Type
        ttk.Label(self.search_window, text="Booking ID:").pack(pady=5)
        self.search_booking_id = ttk.Entry(self.search_window)
        self.search_booking_id.pack(pady=5)

        ttk.Label(self.search_window, text="Room Type:").pack(pady=5)
        self.search_room_type = ttk.Combobox(self.search_window, values=["Single", "Double", "Suite"])
        self.search_room_type.pack(pady=5)

        ttk.Button(self.search_window, text="Search", command=self.execute_search).pack(pady=10)

    def execute_search(self):
        booking_id = self.search_booking_id.get()
        room_type = self.search_room_type.get()
        print(f"Searching for Booking ID: {booking_id}, Room Type: {room_type}")
        self.search_window.destroy()
        # =================================================================================NEW
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()

        # search bookings by booking_id
        search_query = """
            SELECT * FROM Bookings
            WHERE booking_id = ?
        """

        # execute the query
        cursor.execute(search_query, (booking_id,))
        # actually get the result
        booking = cursor.fetchone()
        conn.close()

        return booking  # NOTE I THINK WE NEED TO DISPLAY THIS SOMEWHERE????

    def update_bookings_display(self):
        for item in self.bookings_display.get_children():
            self.bookings_display.delete(item)
        start = self.current_page * 50
        end = start + 50
        for booking in self.bookings[start:end]:
            self.bookings_display.insert('', 'end', values=booking)
        self.page_number_label.config(text=f"Page {self.current_page + 1}")

    def next_page(self):
        max_page = len(self.bookings) // 50
        if self.current_page < max_page:
            self.current_page += 1
            self.update_bookings_display()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_bookings_display()

    def create_booking(self):
        create_popup = CreateBookingPopup(self.master, self.handle_create_booking)
        create_popup.grab_set()
        print("Create booking button clicked")

    def handle_create_booking(self, booking_data):
        print("New Booking Data:", booking_data)
        #======================================================================NEW CODE HERE
        # Connect to the sqLite database
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        # note booking_data is the values for the new booking
        # Insert new booking
        cursor.execute("""
            INSERT INTO Bookings (
            no_of_adults, 
            no_of_children, 
            room_type_reserved,
            lead_time,
            arrival_year,
            arrival_month,
            arrival_date,
            avg_price_per_room,
            no_of_special_requests)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, booking_data)
        # Commit the transaction and close
        conn.commit()
        conn.close()

    def update_booking(self):
        print("Update booking button clicked")
        selected_item = self.bookings_display.selection()[0]  # Get selected item
        booking_data = self.bookings_display.item(selected_item, 'values')  # Fetch item data
        update_popup = UpdateBookingPopup(self.master, booking_data)
        update_popup.grab_set()  # Modal window
        # ===========================================================================================NEW CODE HERE
        booking_id = booking_data[0]  # get booking id from the selection
        # connect to db
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()

        # update the bookings table, set all columns
        update_query = """
            UPDATE Bookings
            SET (no_of_adults, 
            no_of_children, 
            room_type_reserved,
            lead_time,
            arrival_year,
            arrival_month,
            arrival_date,
            avg_price_per_room,
            no_of_special_requests) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            WHERE CustomerID = ?
        """

        # execute the query
        cursor.execute(update_query, booking_id)

        # commit and close
        conn.commit()
        conn.close()



class Charts:  # This class contains the code for the Charts section of the GUI to display data visualizations
    def __init__(self, master):
        self.master = master
        self.charts_frame = ttk.Frame(master)  # Create a frame to hold the charts section
        self.charts_frame.pack(fill='both', expand=True)  # Pack the frame to fill the window

    def create_charts_section(self):
        # Visualization type selection
        ttk.Label(self.charts_frame, text="Select Visualization:").pack(side='top', pady=5)
        self.vis_type = ttk.Combobox(self.charts_frame, values=["Room Occupancy Rate Over Time",
                                                                "Number of Bookings by Room Type",
                                                                "Current Occupancy",
                                                                "Average Stay Duration"])
        self.vis_type.pack(side='top', pady=5)
        self.vis_type.bind('<<ComboboxSelected>>', self.update_filters)

        self.filters_frame = ttk.Frame(self.charts_frame)
        self.filters_frame.pack(fill='x', padx=10, pady=5)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.plot = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.charts_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_filters(self, event):
        for widget in self.filters_frame.winfo_children():
            widget.destroy()

        selected_vis = self.vis_type.get()
        if selected_vis == "Room Occupancy Rate Over Time":
            # Example: Filter by date range
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))

            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("occupancy")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Number of Bookings by Room Type":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Current Occupancy":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

        elif selected_vis == "Average Stay Duration":
            ttk.Label(self.filters_frame, text="Start Date:").pack(side='left', padx=(0, 10))
            start_date_entry = ttk.Entry(self.filters_frame)
            start_date_entry.pack(side='left', padx=(0, 10))

            ttk.Label(self.filters_frame, text="End Date:").pack(side='left', padx=(0, 10))
            end_date_entry = ttk.Entry(self.filters_frame)
            end_date_entry.pack(side='left', padx=(0, 10))
            ttk.Button(self.filters_frame, text="Update Chart", command=lambda: self.update_chart("bookings")).pack(
                side='left', padx=(10, 0))

    def update_chart(self, chart_type):
        # Placeholder function for updating the chart
        print(f"Updating chart: {chart_type}")
        self.plot.clear()
        if chart_type == "occupancy":
            # Generate occupancy rate over time plot
            pass  # Replace with actual plotting code
        elif chart_type == "bookings":
            # Generate number of bookings by room type plot
            pass  # Replace with actual plotting code
        self.canvas.draw()


class GUI:
    """Responsible for the general GUI set up and layout, and instantiating the above mentioned classes to ensure the
    principle of Single-Responsibility that ensures efficient organization of the code"""

    def __init__(self, master):
        self.master = master
        master.title("CCT211: Project 2: Hotel Reservation Management System")

        # Set the window to fullscreen
        self.fullscreen = False
        self.toggle_fullscreen()  # Call the function to toggle fullscreen

        # Bind Escape key to toggle fullscreen mode
        self.master.bind("<Escape>", self.toggle_fullscreen)

        # Create the main menu (tabs) for the GUI using ttk.Notebook which will hold the tabs
        self.notebook = ttk.Notebook(master)

        # Frames for each tab
        self.dashboard_frame = ttk.Frame(self.notebook)
        self.room_frame = ttk.Frame(self.notebook)
        self.bookings_frame = ttk.Frame(self.notebook)
        self.charts_frame = ttk.Frame(self.notebook)

        # Add the tabs to the notebook
        self.notebook.add(self.dashboard_frame, text="Dashboard")  # Add the dashboard tab
        self.notebook.add(self.room_frame, text="Rooms")  # Add the rooms tab
        self.notebook.add(self.bookings_frame, text="Bookings")  # Add the bookings tab
        self.notebook.add(self.charts_frame, text="Charts")  # Add the charts tab

        # Pack the notebook
        self.notebook.pack(expand=True, fill='both')

        # Initialize the sections for each tab using the respective classes
        self.dashboard = Dashboard(self.dashboard_frame)
        self.rooms = Rooms(self.room_frame)
        self.bookings = Bookings(self.bookings_frame)
        self.bookings.create_bookings_display()
        self.charts = Charts(self.charts_frame)
        self.charts.create_charts_section()

    # Function to toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes("-fullscreen", self.fullscreen)

        if not self.fullscreen:  # If exiting fullscreen mode set the window size to 1000x750
            # Calculate the coordinates for the top left corner of the window to center it
            window_width = 1000
            window_height = 750
            screen_width = self.master.winfo_screenwidth()  # Get the screen width
            screen_height = self.master.winfo_screenheight()  # Get the screen height
            position_top = int(screen_height / 2 - window_height / 2)
            position_right = int(screen_width / 2 - window_width / 2)

            # Set the geometry of the window using the calculated coordinates
            self.master.geometry(
                f"{window_width}x{window_height}+{position_right}+{position_top}")  # Set the window size and position to center it

    def on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Bookings" and not self.bookings_initialized:
            self.create_bookings_display()
            self.bookings_initialized = True
        elif tab_text == "Charts" and not self.charts_initialized:
            self.create_charts_section()
            self.charts_initialized = True  # Ensure charts section is initialized once


class UpdateBookingPopup(tk.Toplevel):
    def __init__(self, parent, booking_data):
        super().__init__(parent)
        self.title("Update Booking")
        self.geometry("300x200")
        self.booking_data = booking_data  # Expected to be a tuple or list of booking details
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Room Type:").grid(row=0, column=0)
        self.room_type = ttk.Entry(self)
        self.room_type.grid(row=0, column=1)
        self.room_type.insert(0, self.booking_data[1])

        ttk.Label(self, text="Number of Adults:").grid(row=1, column=0)
        self.no_of_adults = ttk.Entry(self)
        self.no_of_adults.grid(row=1, column=1)
        self.no_of_adults.insert(0, self.booking_data[2])

        ttk.Label(self, text="Number of Children:").grid(row=2, column=0)
        self.no_of_children = ttk.Entry(self)
        self.no_of_children.grid(row=2, column=1)
        self.no_of_children.insert(0, self.booking_data[3])

        ttk.Label(self, text="Lead Time:").grid(row=3, column=0)
        self.lead_time = ttk.Entry(self)
        self.lead_time.grid(row=3, column=1)
        self.lead_time.insert(0, self.booking_data[4])

        ttk.Label(self, text="Arrival Year:").grid(row=4, column=0)
        self.arrival_year = ttk.Entry(self)
        self.arrival_year.grid(row=4, column=1)
        self.arrival_year.insert(0, self.booking_data[5])

        ttk.Label(self, text="Arrival Month:").grid(row=5, column=0)
        self.arrival_month = ttk.Entry(self)
        self.arrival_month.grid(row=5, column=1)
        self.arrival_month.insert(0, self.booking_data[6])

        ttk.Label(self, text="Arrival Date:").grid(row=6, column=0)
        self.arrival_date = ttk.Entry(self)
        self.arrival_date.grid(row=6, column=1)
        self.arrival_date.insert(0, self.booking_data[7])

        ttk.Button(self, text="Commit Changes", command=self.commit_changes).grid(row=7, column=0, columnspan=2, pady=10)

    def commit_changes(self):
        updated_data = (
            self.room_type.get(),
            self.no_of_adults.get(),
            self.no_of_children.get(),
            self.lead_time.get(),
            self.arrival_year.get(),
            self.arrival_month.get(),
            self.arrival_date.get(),
        )
        print("Updated Booking Data:", updated_data)
        # send the updated data back to data store
        self.destroy()


class CreateBookingPopup(tk.Toplevel):
    def __init__(self, parent, create_callback):
        super().__init__(parent)
        self.title("Create New Booking")
        self.geometry("400x350")  # Adjust size as needed
        self.create_callback = create_callback
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Booking ID:").grid(row=0, column=0)
        self.booking_id = ttk.Entry(self)
        self.booking_id.grid(row=0, column=1)

        ttk.Label(self, text="Number of Adults:").grid(row=1, column=0)
        self.no_of_adults = ttk.Entry(self)
        self.no_of_adults.grid(row=1, column=1)

        ttk.Label(self, text="Number of Children:").grid(row=2, column=0)
        self.no_of_children = ttk.Entry(self)
        self.no_of_children.grid(row=2, column=1)

        ttk.Label(self, text="Room Type Reserved:").grid(row=3, column=0)
        self.room_type_reserved = ttk.Combobox(self, values=["Single", "Double", "Suite"])
        self.room_type_reserved.grid(row=3, column=1)

        ttk.Label(self, text="Lead Time:").grid(row=4, column=0)
        self.lead_time = ttk.Entry(self)
        self.lead_time.grid(row=4, column=1)

        ttk.Label(self, text="Arrival Year:").grid(row=5, column=0)
        self.arrival_year = ttk.Entry(self)
        self.arrival_year.grid(row=5, column=1)

        ttk.Label(self, text="Arrival Month:").grid(row=6, column=0)
        self.arrival_month = ttk.Entry(self)
        self.arrival_month.grid(row=6, column=1)

        ttk.Label(self, text="Arrival Date:").grid(row=7, column=0)
        self.arrival_date = ttk.Entry(self)
        self.arrival_date.grid(row=7, column=1)

        ttk.Label(self, text="Avg. Price per Room:").grid(row=8, column=0)
        self.avg_price_per_room = ttk.Entry(self)
        self.avg_price_per_room.grid(row=8, column=1)

        ttk.Button(self, text="Create Booking", command=self.create_booking).grid(row=9, column=0, columnspan=2, pady=10)

    def create_booking(self):
        new_booking_data = {
            "booking_id": self.booking_id.get(),
            "no_of_adults": self.no_of_adults.get(),
            "no_of_children": self.no_of_children.get(),
            "room_type_reserved": self.room_type_reserved.get(),
            "lead_time": self.lead_time.get(),
            "arrival_year": self.arrival_year.get(),
            "arrival_month": self.arrival_month.get(),
            "arrival_date": self.arrival_date.get(),
            "avg_price_per_room": self.avg_price_per_room.get(),
        }
        # call a callback function to handle the creation logic,
        # updating database/internal data structure
        self.create_callback(new_booking_data)
        self.destroy()


root = Tk()
login_window = LoginWindow(root)

root.mainloop()