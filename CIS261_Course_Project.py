"""
Emmanuela Mbe
CIS 261
Course Project Phase 4: User Authentication
"""

from datetime import datetime
from pathlib import Path

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def load_users(file_path):
    users = []
    if Path(file_path).exists():
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    user_id, password, auth = line.split("|")
                    users.append(Login(user_id, password, auth))
    return users

def user_exists(user_id, users):
    return any(user.user_id == user_id for user in users)

def register_users(file_path):
    users = load_users(file_path)

    print("\nUSER REGISTRATION")
    
    with open(file_path, "a") as f:
        while True:
            user_id = input("\nEnter user ID (or 'End' to finish): ").strip()
            if user_id.lower() == "end":
                break
            if user_exists(user_id, users):
                print("Error: User ID already exists. Please try again.")
                continue
            
            password = input("Enter password: ").strip()
            
            auth = input("Enter authorization code (Admin/User): ").strip()
            if auth not in ["Admin", "User"]:
                print("Error: Authorization must be 'Admin' or 'User'. Please try again.")
                continue
            
            f.write(f"{user_id}|{password}|{auth}\n")
            users.append(Login(user_id, password, auth))
            print(f"User '{user_id}' registered successfully.")
    return users

def display_users(users):
    if not users:
        print("No users registered.")
        return
    
    print("\nREGISTERED USERS")
    for user in users:
        print(f"User ID: {user.user_id}")
        print(f"Password: {user.password}")
        print(f"Authorization: {user.authorization}")
        print("-" * 50)

def login_user(users):
    print("\nUSER LOGIN")
    
    user_id = input("\nEnter user ID: ").strip()
    user = next((u for u in users if u.user_id == user_id), None)
    
    if not user:
        print("Error: User ID does not exist.")
        return None
    
    password = input("Enter password: ").strip()
    if user.password != password:
        print("Error: Password does not match.")
        return None
    
    print(f"Welcome, {user_id}!")
    return user

def get_employee_name():
    name = input("\nEnter employee name (or 'end' to finish): ").strip()
    return None if name.lower() == "end" else name

def get_pay_period():
    fmt = "%m/%d/%Y"
    while True:
        try:
            from_date = datetime.strptime(input("Enter pay period from date (mm/dd/yyyy): "), fmt).strftime(fmt)
            to_date = datetime.strptime(input("Enter pay period to date (mm/dd/yyyy): "), fmt).strftime(fmt)
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def get_employee_details():
    hours = float(input("Enter total hours worked: "))
    rate = float(input("Enter hourly rate: "))
    tax = float(input("Enter income tax rate (as %): "))
    return hours, rate, tax

def get_report_from_date():
    fmt = "%m/%d/%Y"
    while True:
        entry = input("Enter from date to filter report (mm/dd/yyyy) or 'All' for all records: ").strip()
        if entry.lower() == "all":
            return "All"
        try:
            return datetime.strptime(entry, fmt).strftime(fmt)
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy or enter 'All'.")

def add_payroll_records(payroll_file):
    print("\nADD EMPLOYEE PAYROLL RECORDS")
    
    with open(payroll_file, "a") as f:
        while True:
            name = get_employee_name()
            if name is None:
                break
            from_date, to_date = get_pay_period()
            hours, rate, tax = get_employee_details()
            f.write(f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax}\n")

def process_employees(payroll_file, filter_date):
    totals = {"employees": 0, "hours": 0.0, "gross": 0.0, "tax": 0.0, "net": 0.0}
    
    if not Path(payroll_file).exists():
        return totals
    
    with open(payroll_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            from_date, to_date, name, hours, rate, tax_rate = line.split("|")
            hours, rate, tax_rate = float(hours), float(rate), float(tax_rate)
            
            if filter_date != "All" and from_date != filter_date:
                continue
            
            gross_pay = hours * rate
            income_tax = gross_pay * (tax_rate / 100)
            net_pay = gross_pay - income_tax
            
            print("\nEmployee Payroll Information")
            print(f"Employee Name: {name}")
            print(f"Pay Period: {from_date} to {to_date}")
            print(f"Hours Worked: {hours}")
            print(f"Hourly Rate: ${rate:.2f}")
            print(f"Gross Pay: ${gross_pay:.2f}")
            print(f"Income Tax Rate: {tax_rate}%")
            print(f"Income Tax: ${income_tax:.2f}")
            print(f"Net Pay: ${net_pay:.2f}")
            
            totals["employees"] += 1
            totals["hours"] += hours
            totals["gross"] += gross_pay
            totals["tax"] += income_tax
            totals["net"] += net_pay
    
    return totals

def display_totals(totals):
    print("\nPAYROLL SUMMARY")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']:.2f}")
    print(f"Total Gross Pay: ${totals['gross']:.2f}")
    print(f"Total Tax: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net']:.2f}")

def view_payroll_report(payroll_file):
    print("\nVIEW PAYROLL REPORT")
    
    filter_date = get_report_from_date()
    totals = process_employees(payroll_file, filter_date)
    
    if totals["employees"] > 0:
        display_totals(totals)
    else:
        print("No employee records found for the specified date.")

def admin_menu(user, users_file, payroll_file):
    while True:
        print(f"\nADMIN MENU - Welcome {user.user_id}")
        print("1. View Payroll Report")
        print("2. Add Employee Payroll Records")
        print("3. View All Registered Users")
        print("4. Logout")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            view_payroll_report(payroll_file)
        elif choice == "2":
            add_payroll_records(payroll_file)
        elif choice == "3":
            users = load_users(users_file)
            display_users(users)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user, payroll_file):
    while True:
        print(f"\nUSER MENU - Welcome {user.user_id}")
        print("1. View Payroll Report")
        print("2. Logout")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            view_payroll_report(payroll_file)
        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    users_file = "users.txt"
    payroll_file = "payroll.txt"
    
    users = load_users(users_file) 
    if not users:
        print("\nNO USERS FOUND - REGISTRATION REQUIRED")
        users = register_users(users_file)
        display_users(users)
    
    while True:
        print("\nMAIN MENU")
        print("1. Login")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            logged_in_user = login_user(users)
            if logged_in_user:
                if logged_in_user.authorization == "Admin":
                    admin_menu(logged_in_user, users_file, payroll_file)
                else:
                    user_menu(logged_in_user, payroll_file)
                users = load_users(users_file)
        elif choice == "2":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()