from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Course, Grade, Teacher, Group, Discipline

# Підключення до бази даних
engine = create_engine('sqlite:///contacts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Функція для знаходження 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    top_students = session.query(Student).\
        join(Grade).\
        group_by(Student.id).\
        order_by(func.avg(Grade.score).desc()).\
        limit(5).all()
    return top_students

# Функція для знаходження студента із найвищим середнім балом з певного предмета
def select_2(course_name):
    top_student = session.query(Student).\
        join(Grade).\
        join(Course).\
        filter(Course.name == course_name).\
        group_by(Student.id).\
        order_by(func.avg(Grade.score).desc()).\
        first()
    return top_student

# Функція для знаходження середнього балу у групах з певного предмета
def select_3(course_name):
    avg_score = session.query(func.avg(Grade.score)).\
        join(Course).\
        filter(Course.name == course_name).\
        scalar()
    return avg_score

# Функція для знаходження середнього балу на потоці (по всій таблиці оцінок)
def select_4():
    avg_score_all = session.query(func.avg(Grade.score)).scalar()
    return avg_score_all

# Функція для знаходження курсів, які читає певний викладач
def select_5(teacher_name):
    teacher_courses = session.query(Course).\
        join(Teacher).\
        filter(Teacher.name == teacher_name).all()
    return teacher_courses

# Функція для знаходження списку студентів у певній групі
def select_6(group_name):
    group_students = session.query(Student).\
        join(Group).\
        filter(Group.name == group_name).all()
    return group_students

# Функція для знаходження оцінок студентів у окремій групі з певного предмета
def select_7(group_name, course_name):
    group_grades = session.query(Grade).\
        join(Student).\
        join(Group).\
        join(Course).\
        filter(Group.name == group_name, Course.name == course_name).all()
    return group_grades

# Функція для знаходження середнього балу, який ставить певний викладач зі своїх предметів
def select_8(teacher_name):
    teacher_avg_score = session.query(func.avg(Grade.score)).\
        join(Course).\
        join(Teacher).\
        filter(Teacher.name == teacher_name).scalar()
    return teacher_avg_score

# Функція для знаходження списку курсів, які відвідує певний студент
def select_9(student_name):
    student_courses = session.query(Course).\
        join(Grade).\
        join(Student).\
        filter(Student.name == student_name).all()
    return student_courses

# Функція для знаходження списку курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    student_teacher_courses = session.query(Course).\
        join(Grade).\
        join(Student).\
        join(Teacher).\
        filter(Student.name == student_name, Teacher.name == teacher_name).all()
    return student_teacher_courses

