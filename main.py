from encode import encode
from decode import decode


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