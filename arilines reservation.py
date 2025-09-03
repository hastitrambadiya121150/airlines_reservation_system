import os
import csv

FILE_NAME = "Airlines_Reservation.csv"

def add_passenger(Receipt_No, Name, Email, Age, From, To, Date, Gender, Nationality, Airlines, Class):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == Receipt_No:
                    print("Record already added, add a new Receipt_no.")
                    return
    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Receipt_No, Name, Email, Age, From, To, Date, Gender, Nationality, Airlines, Class])
        
    print("Record added successfully.")

def display_passenger():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    max_name_length = 0
    # First pass to find the max length of the name
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 11:
                max_name_length = max(max_name_length, len(row[1]))

    # Print header with space after name column
    #print(f"Receipt_No\tName{' ' * (max_name_length - 4)}\tEmail\tAge\tFrom\tTo\tDate\tGender\tNationality\tAirlines\tClass")
    #print("-" * (8 + max_name_length + 10))  # Adjust separator based on name length

    
    # Second pass to display the students
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            #if len(row) == 11:
                #Receipt_No, Name, Email, Age, From, To, Date, Gender, Nationality, Airlines, Class = row
                 #Print name column with dynamic spaces based on longest name
                print(f"Receipt_No: {row[0]}\nName: {row[1]}\nEmail: {row[2]}\nAge: {row[3]}\nFrom: {row[4]}\nTo: {row[5]}\nDate: {row[6]}\nGender: {row[7]}\nNationality: {row[8]}\nAirlines: {row[9]}\nClass: {row[10]}\n")
                print("-" * 35)
 
def delete_passenger(Reciept_No):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    rows = []
    found = False  # Flag to check if the record is found
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check if the record exists and filter out the student
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == Receipt_No:
                found = True  # Mark as found if record is deleted
            else:
                writer.writerow(row)
    
    if found:
        print("Record deleted.")
    else:
        print("Record not found.")

def update_passenger(Receipt_No):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    
    rows = []
    updated = False  # Flag to check if record is updated
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check if the record exists before asking for new details
    for row in rows:
        if row[0] == Receipt_No:
            updated = True
            break  # Exit the loop as record is found
    
    if not updated:
        print("Record not found.")
        return  # Exit the function early if the record is not found

    # If record is found, ask for new details
    new_name = input("Enter New Name: ")
    new_email = input("Enter New Email: ")
    new_age = input("Enter New Age: ")
    new_from = input("Enter New From: ")
    new_to = input("Enter New To: ")
    new_date = input("Enter New Date: ")
    new_gender = input("Enter New Gender: ")
    new_nationality = input("Enter New Nationality: ")
    new_airlines = input("Enter New Airlines: ")
    new_class = input("Enter New Class: ")

    # Update the record
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == Receipt_No:
                writer.writerow([Receipt_No, new_name, new_email, new_age, new_from, new_to, new_date, new_gender, new_nationality, new_airlines, new_class])
            else:
                writer.writerow(row)
    print("Record updated successfully.")

def search_passenger(Receipt_No):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == Receipt_No:
                print(f"Receipt_No: {row[0]}\nName: {row[1]}\nEmail: {row[2]}\nAge: {row[3]}\nFrom: {row[4]}\nTo: {row[5]}\nDate: {row[6]}\nGender: {row[7]}\nNationality: {row[8]}\nAirlines: {row[9]}\nClass: {row[10]}\n")
                print("-" * 35)
                return
    print("Passenger record not found.")

def search_passenger_by_name(Name):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == Name:
                print(f"Receipt_No: {row[0]}\nName: {row[1]}\nEmail: {row[2]}\nAge: {row[3]}\nFrom: {row[4]}\nTo: {row[5]}\nDate: {row[6]}\nGender: {row[7]}\nNationality: {row[8]}\nAirlines: {row[9]}\nClass: {row[10]}\n")
                print("-" * 35)
                return
    print("Passenger record not found.")

def count_passengers_by_airline():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    airline_count = {}
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if len(row) == 11:
                airline = row[9]
                if airline in airline_count:
                    airline_count[airline] += 1
                else:
                    airline_count[airline] = 1

    print("Passenger Count per Airline:")
    print("-" * 35)
    for airline, count in airline_count.items():
        print(f"{airline}: {count} passenger(s)")

def count_total_passengers():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        total = sum(1 for _ in reader)
    print(f"Total number of passengers: {total}")


def clear_all_records():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Receipt_No", "Name", "Email", "Age", "From", "To", "Date", "Gender", "Nationality", "Airlines", "Class"])  # Writing the header again
    print("All records have been cleared.")


def initialize_file():
    # Check if file exists, if not, create it with header
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Receipt_No", "Name", "Email", "Age", "From", "To", "Date", "Gender", "Nationality", "Airlines", "Class"])  # Writing the header

# Initialize file with header if it doesn't exist
initialize_file()

while True:
    print("\n1. Add Passenger\n2. Display Passenger\n3. Delete Passenger\n4. Update Passenger\n5. Search Passenger\n6. Search Passenger By Name\n7. Count Passengers by Airlines\n8. Count Total Passengers\n9. Clear All Records\n10. Exit")
    print("-" * 35)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        Receipt_No = input("Enter Receipt_No: ")
        Name = input("Enter Name: ")
        Email = input("Enter Email: ")
        Age = input("Enter Age: ")
        From = input("Enter From: ")
        To = input("Enter To: ")
        Date = input("Enter Date: ")
        Gender = input("Enter Gender: ")
        Nationality = input("Enter Nationality: ")
        Airlines = input("Enter Airlines: ")
        Class = input("Enter Class: ")
        add_passenger(Receipt_No, Name, Email, Age, From, To, Date, Gender, Nationality, Airlines, Class)
    elif choice == "2":
        display_passenger()
    elif choice == "3":
        Receipt_No = input("Enter Receipt_No to delete: ")
        delete_passenger(Receipt_No)
    elif choice == "4":
        Receipt_No = input("Enter Receipt_No to update: ")       
        update_passenger(Receipt_No)
    elif choice == "5":
        Receipt_No = input("Enter Receipt_No to search: ")
        search_passenger(Receipt_No)
    elif choice == "6":
        Name = input("Enter Name to search: ")
        search_passenger_by_name(Name)
    elif choice == "7":
        count_passengers_by_airline()
    elif choice == "8":
        count_total_passengers()
    elif choice == "9":
        clear_all_records()  # Clear all records
    elif choice == "10":
        break
    else:
        print("Invalid choice, please try again.")
