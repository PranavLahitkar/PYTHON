import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="pranav",
    password="12345678",
    database="studentsdb"
)
db_cursor = db_connection.cursor()

# Function to insert a new student into the database
def add_student(student_id, name, age, grade):
    sql = "INSERT INTO students (student_id, name, age, grade) VALUES (%s, %s, %s, %s)"
    values = (student_id, name, age, grade)
    db_cursor.execute(sql, values)
    db_connection.commit()
    print("Student added successfully!")

# Function to retrieve all students from the database
def get_all_students():
    db_cursor.execute("SELECT * FROM students")
    students = db_cursor.fetchall()
    for student in students:
        print(student)

# Main function
def main():
    while True:
        print("\n1. Add a student")
        print("2. View all students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            add_student(student_id, name, age, grade)
        elif choice == "2":
            get_all_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    # Close the database connection
    db_cursor.close()
    db_connection.close()
    print("Program exited.")

if __name__ == "__main__":
    main()
