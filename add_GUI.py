import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Log In to the Hotel Reservation Management System")

        window_width = 400
        window_height = 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        ttk.Label(master, text="Username:").pack()
        self.entry_username = ttk.Entry(master)
        self.entry_username.pack()

        ttk.Label(master, text="Password:").pack()
        self.entry_password = ttk.Entry(master, show="*")
        self.entry_password.pack()

        ttk.Button(master, text="Log In", command=self.login).pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username.isalnum() and password.isalnum():
            messagebox.showinfo("Login Successful", "Welcome to the Hotel Reservation Management System!")
            self.master.destroy()
            main_app_window = tk.Tk()
            app_gui = GUI(main_app_window)
            main_app_window.mainloop()
        else:
            messagebox.showinfo("Login Failed", "Invalid username or password. Please try again.")


class Dashboard:
    def __init__(self, master):
        self.master = master

    def update_data(self):
        pass


class GUI:
    def __init__(self, master):
        self.master = master
        self.dashboard = Dashboard(master)
        master.title("Hotel Reservation Management System")
        master.geometry("1000x750")

        self.fullscreen = False
        self.toggle_fullscreen()
        self.master.bind("<Escape>", self.toggle_fullscreen)

        self.notebook = ttk.Notebook(master)
        self.dashboard_frame = ttk.Frame(self.notebook)
        self.room_frame = ttk.Frame(self.notebook)
        self.bookings_frame = ttk.Frame(self.notebook)
        self.charts_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.dashboard_frame, text="Dashboard")
        self.notebook.add(self.room_frame, text="Rooms")
        self.notebook.add(self.bookings_frame, text="Bookings")
        self.notebook.add(self.charts_frame, text="Charts")

        self.notebook.pack(expand=True, fill='both')
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.bookings_initialized = False
        self.charts_initialized = False  # New flag for charts initialization

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes("-fullscreen", self.fullscreen)

    def on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Bookings" and not self.bookings_initialized:
            self.create_bookings_display()
            self.bookings_initialized = True
        elif tab_text == "Charts" and not self.charts_initialized:
            self.create_charts_section()
            self.charts_initialized = True  # Ensure charts section is initialized once

    def create_bookings_display(self):
        ttk.Button(self.bookings_frame, text="Search Bookings", command=self.open_search_window).pack(pady=10)

        self.current_page = 0
        self.bookings = [("Booking ID", "Room Type", "Stay Length", "Check-in", "Check-out")] * 200

        self.bookings_display = ttk.Treeview(self.bookings_frame, columns=(1, 2, 3, 4, 5), show="headings")
        self.bookings_display.pack(fill='both', expand=True)
        for col in self.bookings_display['columns']:
            self.bookings_display.heading(col, text=col)

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
        ttk.Button(crud_frame, text="Create Booking", command=self.create_booking).pack(side='left', padx=5)

        # Update button
        ttk.Button(crud_frame, text="Update Booking", command=self.update_booking).pack(side='left', padx=5)

        # Delete button
        ttk.Button(crud_frame, text="Delete Booking", command=self.delete_booking).pack(side='left', padx=5)

        self.update_bookings_display()

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


if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
