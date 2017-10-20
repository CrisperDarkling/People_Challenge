def add_person():
    print("")
    FirstName = input("Enter Your First Name\n> ")
    
    print("")
    LastName = input("Enter Your Last Name\n> ")
    
    print("")
    Team = input("Enter Your Team\n> ")

    print("")
    Age = input("Enter Your Age\n> ")
    
    file = open("input.txt", "a")
    file.write(FirstName + ", " + LastName + ", " + Team + ", " + Age + "\n" )
    file.close()

def view_people():
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    
    print(lines)
    file.close()

def stats():
    num_lines = open("input.txt").read().count("\n")
    print("Amount of people in list:")
    print(num_lines)
    
    
    game_loop()
    
def show_menu():
    print("1. Add Person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")

    option = input("Enter option: ")
    return option

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_person()
            print("You selected 'Add Person'")
        elif option == "2":
            view_people()
            print("You selected 'View People'")
        elif option == "3":
            stats()
            print("You selected 'Stats'")
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")


game_loop()