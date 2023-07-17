
import random
from faker import Faker
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="mysecretpassword",
    database="postgres"
)


cursor = connection.cursor()
fake = Faker("uk_UA")

def show_groups():
    cursor.execute("SELECT * FROM groups")
    groups = cursor.fetchall()
    print("Existing groups:")
    for group in groups:
        print(group)


# Створення функції для заповнення таблиці студентів
def insert_students(num_students):
    existing_group_ids = []
    cursor.execute("SELECT group_id FROM groups")
    existing_groups = cursor.fetchall()
    for group in existing_groups:
        existing_group_ids.append(group[0])

    for _ in range(num_students):
        first_name = fake.first_name()
        last_name = fake.last_name()
        group_id = random.choice(existing_group_ids)
        query = "INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s)"
        values = (first_name, last_name, group_id)
        cursor.execute(query, values)
        connection.commit()



# Створення функції для заповнення таблиці груп
def insert_groups(num_groups):
    for i in range(1, num_groups + 1):
        group_name = f"Group {i}"
        query = "INSERT INTO groups (group_name) VALUES (%s)"
        values = (group_name,)
        cursor.execute(query, values)
        connection.commit()

# Створення функції для заповнення таблиці викладачів
def insert_teachers(num_teachers):
    for _ in range(num_teachers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        query = "INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)"
        values = (first_name, last_name)
        cursor.execute(query, values)
        connection.commit()

# Створення функції для заповнення таблиці предметів
def insert_subjects(num_subjects):
    for _ in range(num_subjects):
        subject_name = fake.job()
        teacher_id = random.randint(1, 3)
        query = "INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)"
        values = (subject_name, teacher_id)
        cursor.execute(query, values)
        connection.commit()

# Створення функції для заповнення таблиці оцінок
def insert_grades(num_grades):
    existing_student_ids = []
    cursor.execute("SELECT student_id FROM students")
    existing_students = cursor.fetchall()
    for student in existing_students:
        existing_student_ids.append(student[0])

    for _ in range(num_grades):
        student_id = random.choice(existing_student_ids)  # Випадкове значення з наявних student_id
        subject_id = random.randint(1, 8)
        grade = round(random.uniform(60, 100), 1)
        date_received = fake.date_between(start_date="-3y", end_date="today")
        query = "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)"
        values = (student_id, subject_id, grade, date_received)
        cursor.execute(query, values)
        connection.commit()



if __name__ == "__main__":
    insert_groups(3)
    show_groups()  # Виведення існуючих груп після додавання
    insert_teachers(5)
    insert_subjects(8)
    insert_students(30)
    show_groups()  # Виведення існуючих груп після додавання студентів
    insert_grades(500)

cursor.close()
connection.close()
