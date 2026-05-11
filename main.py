
def show_menu():
    print("\nGame Statistics Analyzer")
    print("1. Show leaderboard")
    print("2. Show average score")
    print("3. Show best performance")
    print("4. Export report")
    print("5. Run tests")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            print("Leaderboard feature will be connected later.")
        elif choice == "2":
            print("Average score feature will be connected later.")
        elif choice == "3":
            print("Best performance feature will be connected later.")
        elif choice == "4":
            print("Export report feature will be connected later.")
        elif choice == "5":
            print("Tests will be connected later.")
        elif choice == "0":
            print("Exit program.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()