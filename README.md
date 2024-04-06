# Hotel Reservation Management System

Welcome to the Hotel Reservation Management System! A Tkinter-based GUI application for efficiently managing room reservations in hotels.
This system provides a usable interface for managing hotel bookings efficiently. Below you will find information about how to use the system, its functionalities, and more.

A noteworthy aspect is that we named our hotel "ACKA Hospitality" after the names of the members involved in this Persistence Form Project.

---

## Log In

This first feature of the system is a log in portal.

The widget features an image logo we created for our "ACKA Hospitality" hotel, entry fields for the username and password, and a "Log In" button.

The log in portal only accepts designated credentials and features error prevention in the form of a "Login Failed" widget that pops up in cases of unsuccessful log in. The "Login Failed" widget notifies the user that the input is invalid and features an "OK" button which destroys the widget and returns the user to the Log In portal.

To access the system, use the following credentials:

- **Username:** admin
- **Password:** cct211

---

## Features

### 1. Dashboard

The **Dashboard** tab overviews the hotel's status and bookings. It displays information such as room details, room status, and current bookings. The dashboard provides visualizations and key stats for the hotel's operations. It includes sections for room details, room status, and current bookings. The room details section displays information like price and capacity. The room status section shows the number of rooms occupied and available. The current bookings section lists the booking ID, room type, length of stay, check-in date, and check-out date for the current bookings.



### 2. Rooms

The **Rooms** tab showcases various room types. An image and a description accompany each room type. Images are retrieved from RIU's official website as a reference.

**Room Types Available:**
1. Type 1: Queen
2. Type 2: King
3. Type 3: Twins
4. Type 4: Double-double
5. Type 5: Jr. Suite
6. Type 6: Executive Suite

**Room Images:**  
Room images are provided by the RIU hotel chain. Visit the following links to explore more room options:

- [Hotel Riu Cancun](https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-cancun/#rooms-grid)
- [Hotel Riu Caribe](https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-caribe/#rooms-grid)

*References*:
- Riu. (n.d.). Hotel Riu Cancun. Retrieved from [https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-cancun/#rooms-grid](https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-cancun/#rooms-grid)
- Riu. (n.d.). Hotel Riu Caribe. Retrieved from [https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-caribe/#rooms-grid](https://www.riu.com/en/hotel/mexico/cancun/hotel-riu-caribe/#rooms-grid)

### 3. Bookings

The **Bookings** tab allows users to manage bookings efficiently. Users can search for bookings, view current bookings, and perform CRUD (Create, Read, Update, Delete) operations.

Search Bookings: Clicking the "Search Bookings" button opens a popup window where users can search for bookings based on criteria such as Booking ID and Room Type.

Display Bookings: The tab displays bookings in a table format using a Treeview widget. Each row represents a booking and includes columns for Booking ID, Number of Adults, Number of Children, Room Type, Lead Time, Arrival Year, Arrival Month, Arrival Date, Average Price of Room, and Number of Special Requests. The table is fixed to display 50 bookings per page.

Booking Pages: The tab includes functionality with "Previous Page" and "Next Page" buttons to navigate through the booking pages.

CRUD Operations:

Create Booking: Clicking the "Create Booking" button opens a popup window where users can enter details for a new booking. The new booking is then added to the database.
Read data: Displays the existing bookings in a table format using the Treeview widget. 
Update Booking: Selecting a booking in the table and clicking the "Update Booking" button opens a popup window pre-filled with the booking details. Users can edit the booking details and save the changes, which are then updated in the database.
Delete Booking: Selecting a booking in the table and clicking the "Delete Booking" button deletes the booking from the database and removes it from the table.

Explanation of each Class:

1. LoginWindow

2. SearchPopup

3. Dashboard

4. Rooms

5. Bookings

6. Charts

8. GUI

9. CreateBookingPopup

10. UpdateBookingPopup

---

## Getting Started

1. Log in using the provided credentials.
2. Explore different tabs to manage bookings, view room options, and access visualizations.

---

### 5. Search Popup

Explanation of each def function:

1. def create_widgets(self): Creates the UI elements (labels, entry fields, combobox, and search button) for the search filters. Each widget is placed in a specific row and column using the grid method.

### 6. Charts

The **Charts** tab provides visualizations of hotel data, including room occupancy rate over time, number of bookings by room type, current occupancy, and average stay duration, while leveraging the matplotlib library and pandas.

The first graph shows the 'Room Occupancy Rate Over Time' in a line plot graph. The purpose of this graph is to track the room occupancy rate over time (daily, monthly, yearly). This helps in identifying peak seasons, planning for high demand, and optimizing room rates.

The second graph shows the 'Number of Bookings by Room Type' through a bar chart. The purpose of this graph is to show the distribution of bookings across different room types (e.g., single, double, suite). This can guide room renovation and marketing strategies.

The third graph shows the 'Current Occupancy of the Hotel' in a pie chart, and the percentage of occupation is also shown. The purpose of the graph is to provide hotel management employees with a quick and visual representation of the current occupancy status of the hotel.

The fourth graph shows the 'Average Length of Stay by Room Type' using a histogram. The purpose of this graph is to understand the distribution of stay durations among guests. This can inform staffing needs, check-in/check-out procedures, and promotions for longer stays.

---

## Contributors

- Camila R. Flores Diaz
- Anja Radin
- Amanda Faith Wang
- Kiley Kailai Zheng

---

Thank you for using our system! We hope you have a pleasant experience.
