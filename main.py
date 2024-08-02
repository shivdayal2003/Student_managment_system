class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

students = {}

def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists")
        return
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    major = input("Enter student major: ")
    student = Student(student_id, name, age, major)
    students[student_id] = student
    print("Student added successfully")

def view_students():
    if not students:
        print("No students to show")
    else:
        print("Student List:")
        for student in students.values():
            print(student)

def find_student():
    student_id = input("Enter student ID: ")
    student = students.get(student_id)
    if student:
        print(student)
    else:
        print("Student not found")

def remove_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        del students[student_id]
        print("Student removed successfully")
    else:
        print("Student not found")

def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Remove Student")
    print("5. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            find_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
