import random
password_simbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
a = int(input('Выберите длину пароля в цифрах'))
password = ''
for i in range(a):
    password += random.choice(password_simbols)
print(password)
