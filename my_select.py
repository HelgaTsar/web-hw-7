from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_1():
    result = session.query(Student.fullname,
                            func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5).all()

    return result


def select_2(discipline_id: int):
    result = session.query(Discipline.name,
                      Student.fullname,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()

    return result


def select_3(discipline_id):
    result = session.query(Discipline.name,
                      Group.name,
                      func.round(func.avg(Grade.grade), 2).label('avg_grade')
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Group) \
        .join(Discipline) \
        .filter(Student.id == Grade.student_id) \
        .filter(Group.id == Student.group_id) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Group.name, Discipline.name) \
        .all()

    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .all()

    return result


def select_5(teacher_id):
    result = session.query(Teacher.fullname, 
                           Discipline.name
                           ) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Discipline.teacher_id == teacher_id) \
        .all()

    return result


def select_6(group_id):
    result = session.query(Group.name, 
                           Student.fullname
                           ) \
        .select_from(Group) \
        .join(Student) \
        .filter(Group.id == group_id) \
        .all()
                      
    return result


def select_7(discipline_id):
    result = session.query(Discipline.name,
                           Group.name,
                           Student.fullname,
                           Grade.grade
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .join(Group) \
        .filter(Discipline.id == discipline_id) \
        .filter(Student.id == Grade.student_id) \
        .filter(Group.id == Student.group_id) \
        .order_by(Discipline.name, Group.name) \
        .all()
                           
    return result


def select_8(teacher_id):
    result = session.query(Teacher.fullname,
                           Discipline.name,
                           func.round(func.avg(Grade.grade), 2).label('avg_grade')
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Grade.discipline_id == Discipline.id) \
        .filter(Discipline.teacher_id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .all()
    
    return result


def select_9(student_id):
    result = session.query(Student.fullname,
                          Discipline.name
                          ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Student.id == student_id) \
        .filter(Grade.discipline_id == Discipline.id) \
        .all()
    
    return result


def select_10(student_id, teacher_id):
    result = session.query(Student.fullname, 
                           Teacher.fullname,
                           Discipline.name
                           ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Student.id == student_id) \
        .filter(Discipline.teacher_id == teacher_id) \
        .group_by(Discipline.name) \
        .all()

    return result



if __name__ == '__main__':
    print('\nTask №1:\n', select_1())
    print('\nTask №2:\n', select_2(1))
    print('\nTask №3:\n', select_3(2))
    print('\nTask №4:\n', select_4())
    print('\nTask №5:\n', select_5(3))
    print('\nTask №6:\n', select_6(3))
    print('\nTask №7:\n', select_7(1))
    print('\nTask №8:\n', select_8(3))
    print('\nTask №9:\n', select_9(2))
    print('\nTask №10:\n', select_10(1, 3))