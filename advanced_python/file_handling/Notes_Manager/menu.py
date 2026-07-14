

running = True
while running :
    print("""Welcome to Notes Manager
      1. View Notes
      2. Add Notes
      3. Replace All Notes
      4. Exit""")
    try :
        x = int(input("Enter the Task Number :"))
    except ValueError :
        print("Invalid input")
        continue

    if x == 1 :
        with open("notes.txt","r") as file:
            print(file.read())
    
    elif x == 2 :
         with open("notes.txt","a") as file:
            file.write(input("\n" + "enter the note :"))       
    
    elif x == 3 :
         with open("notes.txt","w") as file:
                file.write(input("enter the note :"))       
    
    elif x == 4 :
        print("Thanks for using Notes Manager!")
        break
    
    else :
        print("Invalid input")    