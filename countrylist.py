"""
Emmanuela Mbe
CIS 261
Country
"""


def display_menu():
    
    print("\nThe Country List Program")
    print("\nCOMMAND MENU")
    print("view - View a country")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("exit - Exit program")
    print()


def prepopulate_countries():

    countries = {
        "JP": "Japan",
        "FR": "France",
        "DE": "Germany",
    }
    return countries


def view_country(countries):

    print("\nAll country codes:")
    for code in countries:
        print(f"  {code}")
    
    country_code = input("\nEnter country code: ").upper()
    
    if country_code in countries:
        country_name = countries[country_code]
        print(f"Country name: {country_name}")
    else:
        print(f"Error: {country_code} is not a valid country code.")


def add_country(countries):

    country_code = input("\nEnter country code: ").upper()
    
    if country_code in countries:
        print(f"Error: {country_code} already exists in the database.")
    else:
        country_name = input("Enter country name: ")
        countries[country_code] = country_name
        print(f"{country_name} was added.")


def delete_country(countries):

    country_code = input("\nEnter country code: ").upper()
    
    if country_code in countries:
        country_name = countries[country_code]
        del countries[country_code]
        print(f"{country_name} was deleted.")
    else:
        print(f"Error: {country_code} is not a valid country code.")


def main():

    countries = prepopulate_countries()
    
    while True:
        display_menu()
        command = input("Command: ").lower()
        
        if command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            delete_country(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Error: Not a valid command. Please try again.")


if __name__ == "__main__":
    main()