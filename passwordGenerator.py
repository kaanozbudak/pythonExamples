import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+`~|?.,;:ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''

length = int(input("how many letter do you need: \n"))

for x in range(length):
    password += random.choice(chars)
print(password)
