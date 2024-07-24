

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