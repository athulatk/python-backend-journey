from utils.utils import show_menu,add_expense,view_expenses;

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        else:
            break

if __name__ == "__main__":
    main()
