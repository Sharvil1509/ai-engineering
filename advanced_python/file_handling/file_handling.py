#file = open("notes.txt")
# content = file.read()
# print(content)
# file.close()

# with open("notes.txt") as file:
#     content = file.read()
# print(content)    

with open("notes.txt", "r") as file:
    print(file.read())

with open("notes.txt","w") as file:
    file.write("i am learing ai")
    
with open("notes.txt","a") as file:
    file.write("i am sharvil")

with open("my_first_file.txt", "w") as file:
    file.write("Hello!")