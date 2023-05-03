import random
import string

def generate_password(length):
    # define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate the password using the defined characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# example usage
password = generate_password(12)
print(password)