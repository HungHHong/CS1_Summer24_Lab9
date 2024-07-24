def encode(password):
    # return ''.join(str((int(char) + 3) % 10) for char in password)
    encoded_password = []  # Create empty list
    for char in password:
        if char.isdigit():
            # Add 3 to the digit and wrap around using modulo 10
            encoded_char = (int(char) + 3) % 10
            encoded_password.append(str(encoded_char))
        else:
            raise ValueError("Password must contain only numeric characters.")
    return ''.join(encoded_password)

# def decode(password):
#
#     decoded_password = []  # List to hold the decoded characters
#     for char in password:
#         if char.isdigit():
#             # Subtract 3 from the digit and wrap around using modulo 10
#             decoded_char = (int(char) - 3) % 10
#             decoded_password.append(str(decoded_char))
#         else:
#             raise ValueError("Password must contain only numeric characters.")
#     return ''.join(decoded_password)


def main():
    encoded_password = ""
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No encoded password found. Please encode a password first.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()