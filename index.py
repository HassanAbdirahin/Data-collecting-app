from tabulate import tabulate

def get_user_info():
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your Email address: ")
    return name, phone_number, email

def main():
    try:
        array_size = int(input("Enter the number of entries you want to make: "))
        user_data = []

        for _ in range(array_size):
            print(f"\nEnter details for entry {_ + 1}:")
            name, phone_number, email = get_user_info()
            user_data.append((name, phone_number, email))

        print("\nUser data stored successfully:")
        headers = ["Entry", "Name", "Phone Number", "Email Address"]
        data = [[index + 1, *data] for index, data in enumerate(user_data)]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    except ValueError:
        print("Please enter a valid number for the array size.")

if __name__ == "__main__":
    main()
