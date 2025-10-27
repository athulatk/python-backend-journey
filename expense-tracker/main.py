from utils.utils import show_menu,add_expense,view_expenses,delete_expense;

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        else:
            break

if __name__ == "__main__":
    main()
