

lis1 = []
print ("will put the id of the students in a list")

for i in range (10):
    lis1.append(input("enter the id of the student: "))

    ver = input ("if you dont want to continue prees x other print another letter")
    if ver == "x":
        break


students  = {}

for i in lis1:

    print ("let put the details of the", i, "student: ")
    lis2 = []
    first_name = input ("enter the first name: ")
    lis2.append(first_name)
    last_name = input ("enter the last name: ")
    lis2.append(last_name)
    phone = int(input("enter the phone: "))
    lis2.append(phone)

    dic ={"details": lis2}


    print ("let put the notes: ")
    notes = []
    for i in range (5):
        note = int (input("enter the note"))
        notes.append(note)

    dic = {"notes": notes}

    students[i] = dic
    





    
    

