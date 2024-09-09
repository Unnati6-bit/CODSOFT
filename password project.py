import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@34567890_+,.:{}"
passwordlength=int(input("enter the length of password"))
a="".join(random.sample(password,passwordlength))
print("your password is",a)