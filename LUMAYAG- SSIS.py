import csv

def menu_display():
    print("-------------------------------------")
    print("Welcome to Student Information System")
    print("-------------------------------------")
    print("\n1. Add Data")
    print("2. Data List")
    print("3. Edit Data")
    print("4. Delete Data")
    print("5. Search")
    print("6. Exit")

def add_info():
    print("-------------------------")
    print(    "ADD STUDENT DATA"     )
    print("-------------------------")
    with open("Student data.csv","a", newline="" ) as af:
        writer_object = csv.writer(af, delimiter=',')
        y = [input("Id Number: "), input("Name: "), input("Course: "), input("Year: "), input("Gender: ")]
        writer_object.writerow(y)
        print("\nADDED SUCCESSFULLY!")

        input("Press any key to continue")
        return


def data_list():
    print("-------------------------")
    print(       "DATA LIST"         )
    print("-------------------------")
    with open("Student data.csv") as note:
        reader = csv.reader(note, delimiter=',')
        student_list = []
        for row in reader:
            student_list.append(row)
        for item in student_list:
            print(item)

        input("Press any key to continue")
        return


def edit():
    print("------------------------")
    print("EDIT STUDENT INFORMATION")
    print("------------------------")
    with open("Student data.csv") as update:
        reader = csv.reader(update, delimiter=',')
        test = []
        for items in reader:
            test.append(items)

        x = str(input("Type user's Id Number you wish to edit: "))

        for index, item in enumerate(test):
            if x == item[0]:
                print(f'{item} is found!')
                break
        else:
            print("User Not Found!")
            input("Press any key to continue")
            return

        y = [input("Id Number: "), input("Name: "), input("Course: "), input("Year: "), input("Gender: ")]

        test[index] = y

    with open("Student data.csv", 'w', newline="") as edit:
        writer = csv.writer(edit, delimiter=',')
        for items in test:
            writer.writerow(items)

    print("\nEDITED SUCCESSFULLY!")

    input("Press any key to continue")
    return


def delete():
    print("--------------------------")
    print("DELETE STUDENT INFORMATION")
    print("--------------------------")

    id = input("Enter Student's Id Number you wish to delete: ")
    student_found = False
    updated_data = []
    with open("Student data.csv", "r") as dlt:
        reader = csv.reader(dlt)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open("Student data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Id Number: ", id)
        print("\nSTUDENT'S INFORMATION IS DELETED SUCCESSFULLY!")
    else:
        print("User Not Found!")

        input("Press any key to continue")
        return




def search():
    print("--------------------------")
    print("SEARCH STUDENT INFORMATION")
    print("--------------------------")
    with open("Student data.csv") as search:
        reader = csv.reader(search, delimiter=',')
        test = []
        for items in reader:
            test.append(items)

        x = str(input("Type user's Id Number you wish to search: "))

        for index, item in enumerate(test):
            if x == item[0]:
                print(f'{item} is Found')
                break
        else:
            print("User Not Found!")

            input("Press any key to continue")
            return


while True:
    menu_display()

    enter = int(input("\nEnter the number you wish to proceed: "))
    if enter == 1:
        add_info()
    elif enter == 2:
        data_list()
    elif enter == 3:
        edit()
    elif enter == 4:
        delete()
    elif enter == 5:
        search()
    else:
        break

print("-----------------------------")
print(" Thank you! You are all done.")
print("-----------------------------")
