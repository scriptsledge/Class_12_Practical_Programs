import pickle
import sys
dict={}
# function to write
def write_in_file():
    file = open("student.dat","ab") # a-append, b-binary
    no = int(input("Enter no of students :"))
    for i in range(no):
        print("Enter details of student ", i+1)
        dict["roll"] = int(input("Enter roll number: "))
        dict["name"] = input("Enter the name: ")
        dict["marks"] = int(input("Enter the marks: "))
        pickle.dump(dict,file)
    file.close()
# function to display
def display():
    # read form file and display
    file = open("student.dat","rb")
    try:
        while True:
            student = pickle.load(file)
            print(student)
    except EOFError:
        pass
    file.close()
# function to search
def search():
    file = open("student.dat","rb")
    r= int(input("Enter the rollno to search: "))
    found = 0
    try:
        while True:
            data = pickle.load(file)
            if data["roll"] == r:
                print("The rollno =",r,"record found")
                print(data)
                found = 1
                break
    except EOFError:
        pass
    if found ==0:
        print("The rollno =",r ,"record is not found")
    file.close()
# main program
while True:
    print("Menu \n 1- Write in a file \n 2-Display")
    print("3- Search \n 4- Exit \n")
    ch = int(input("Enter your choice = "))
    if ch == 1:
        write_in_file()
    if ch == 2:
        display()
    if ch == 3:
        search()
    if ch == 4:
        print("Hari Om")
        sys.exit()