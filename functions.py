students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title()) #Capitalise the first letter 
    return students_titlecase

def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def read_students(f):
    for line in f:
        yield line #yields a single line from the file
        
def save_file(student):
    try:
        f = open("students.txt", "a+") #open a file, a = append, file doesn't have to already exist
        f.write(student + "\n") #writes to a new line
        f.close()
    except Exception:
        print("Couldn't save")

def read_file():
    try:
        f = open("students.txt", "r") #r = read
        for student in f.read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Error")

"""
def var_args(name, **kwargs): #lets you input any number of arguments (keyword arguments)
    print(name)
    print(kwargs["description"], kwargs["feedback"]) #print the keyword arguments

var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)
"""

read_file()
print_students_titlecase()


student_name = input("Enter name:")
student_id = input("Enter id: ")

add_student(student_name, student_id)
save_file(student_name)