import psycopg2 as pg


def create_db():  # создает таблицы
    conn = pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    )
    cur = conn.cursor()
    cur.execute("""
    create table if not exists Student(
        id serial primary key,
        name varchar(100) not null,
        gpa numeric(10,2),
        birth timestamp with time zone        
        );
    """)
    conn.commit()
    print('Создание таблиц завершено.')
    conn.close()


def get_students(course_id):  # возвращает студентов определенного курса
    pass


def add_students(course_id, students):  # создает студентов и
    # записывает их на курс
    pass


def add_student(student):  # просто создает студента
    conn = pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    )
    cur = conn.cursor()
    cur.execute("""
        insert into Student(name, gpa)
        values('Антон Тетёркин', 5.0), ('Дмитрий Лонкин', 4.9), ('Алексей Лапшин', 2.0);
    """)
    conn.commit()
    conn.close()

def get_student(student_id):
    pass


if __name__ == '__main__':
    create_db()
    add_student(1)

