import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

p1 = make_password()
p2 = make_password(12)

print(f"Password: {p1}")
print(f"Length: {len(p1)}")
print(f"Password: {p2}")
print(f"Length: {len(p2)}")