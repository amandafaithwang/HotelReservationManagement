import csv
import sqlite3

# this file is comparable to the models.py file in the demo repo

# note we should consider if we're gonna use CSV or .db: I JUST ADDED THE DATABASE CODE TO THE REPO - Cami
# the demo uses .db and there are a lot of complexities with CSVs (refer to quiz)
# if we use .db we have to include some conversion code here from CSV to .db
# have to figur eout where to reference the file (FILENAME = "project_data.db") OR (FILENAME = "project_data.csv") and read with pandas dataframe

class Room:
    def __init__(self, room_number, guests, available=True):
        self.room_number = room_number
        self.guests = guests
        self.available = available

    def __str__(self):
        return f"Room Number {self.room_number}, Guests: {self.guests}, Available: {self.available}"

    def confirm(self, update):
        self.available = update


class Booking:
    def __init__(self, name, room_number, check_in, check_out):
        self.name = name
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self):
        return f"Reservation under {self.name}, Room: {self.room_number}, Check-In Date: {self.check_in}, Check-Out Date: {self.check_out}"


class User:
    def __init__(self, username, pw, type='guest'):
        self.username = username.upper()
        self.pw = pw
        self.type = type.upper()  

    def __str__(self):
        return f"User: {self.username}, Type: {type.role}"

    def correct(self, try_pw):
        return self.pw == try_pw

    def business_side(self):
        return self.type == 'staff'


class Authenticate:
    def __init__(self, users):
        self.users = users

    def login(self, username, pw):
        for user in self.users:
            if user.username == username:
                if user.authenticate(password):
                    return user
                else:
                    return None
        return None


# test cases
if __name__ == "__main__":
    users = [
        User("guest1", "password1"),
        User("guest2", "password2"),
        User("staff1", "password3", "staff"),
        User("staff2", "password4", "staff"),
    ]
  
    if Authenticate(users).login("guest1", "password1"):
        print("Welcome Valued Customer!")
    else:
        print("Incorrect username or password")

    if Authenticate(users).login("staff1", "password3") and Authenticate(users).login("staff1", "password3").business_side():
        print("Welcome Valued Staff Member!")
    else:
        print("Incorrect username or password")
