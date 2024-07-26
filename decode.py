'''
implement your decode function here
'''

def decode(password):
    list_password = list(password)
    password2 = []
    for i in range(len(list_password)):
        i_tmp = str(int(list_password[i]) - 3)
        password2.append(i_tmp)
        x = "".join(password2)
    return(x)




# def decode(password):
#
#     decoded_password = []  # Create empty list
#     for char in password:
#         if char.isdigit():
#             # Subtract 3 from the digit and wrap around using modulo 10
#             decoded_char = (int(char) - 3) % 10
#             decoded_password.append(str(decoded_char))
#         else:
#             raise ValueError("Password must contain only numeric characters.")
#     return ''.join(decoded_password)
#
