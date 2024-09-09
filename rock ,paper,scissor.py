import random
item=["rock","paper","scissor"]
user=input("enetr   rock \n enter  paper \n enter  scissor:::")
comp=random.choice(item)
print("your choice",user)
print("comp user",comp)
if user==comp:
    print("match tie")
elif user == "rock":
    if comp == "paper":
        print("you lose")
    else:
        print("you won!!")
elif user == "paper":
    if comp == "scissor":
        print("you lost")
    else:
        print("you won!!")
elif user == "scissor":
    if comp == "rock":
        print("you lost")
    else:
        print("you win!!")            

