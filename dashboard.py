import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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


class HotelBookingGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hotel Room Booking System")
        self.geometry("1000x700")
        self.create_widgets()
        self.create_dashboard_placeholder()
        self.create_room_details_section()
        self.create_room_status_section()
        self.create_bookings_section()

    def create_widgets(self):
        search_btn = ttk.Button(self, text="Search Rooms", command=self.open_search_popup)
        search_btn.pack(pady=20)

    def open_search_popup(self):
        popup = SearchPopup(self)
        popup.grab_set()

    def create_dashboard_placeholder(self):
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.set_title('Visualization Placeholder')
        plot.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_room_details_section(self):
        room_details_frame = ttk.LabelFrame(self, text="Room Details")
        room_details_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_details_frame, text="Price:").grid(row=0, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_details_frame, text="Capacity:").grid(row=1, column=0)
        ttk.Entry(room_details_frame, state='readonly').grid(row=1, column=1)

    def create_room_status_section(self):
        room_status_frame = ttk.LabelFrame(self, text="Room Status")
        room_status_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(room_status_frame, text="Occupied:").grid(row=0, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=0, column=1)
        ttk.Label(room_status_frame, text="Available:").grid(row=1, column=0)
        ttk.Entry(room_status_frame, state='readonly').grid(row=1, column=1)

    def create_bookings_section(self):
        bookings_frame = ttk.LabelFrame(self, text="Current Bookings")
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


if __name__ == "__main__":
    app = HotelBookingGUI()
    app.mainloop()

