from pprint import pprint

import psycopg2 as pg


def create_db():  # создает таблицы
    with pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
        create table if not exists Student(
            id serial primary key,
            name varchar(100) not null,
            gpa numeric(10,2),
            birth timestamp with time zone        
            );
        """)
        cur.execute("""
        create table if not exists Course(
            id integer not null,
            name varchar(100) not null
            );
        """)
        print('Создание таблиц завершено.')

def delete_tables():
    # удалить таблицы в тестовых целях
    conn = pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    )
    cur = conn.cursor()
    cur.execute("""
    drop table if exists Student;
    """)
    conn.commit()
    conn.close()
    print('Таблицы удалены')



def get_students(course_id):  # возвращает студентов определенного курса
    pass

def get_all_students():
    with pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            select * from Student;
        """)
        t12 = cur.fetchall()
        pprint(t12)



def add_students(course_id, students):  # создает студентов и
    # записывает их на курс
    pass


def add_student(student):  # просто создает студента
    with pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
        ) as conn:
            cur = conn.cursor()
            # cur.execute("""
            # insert into Student(name, gpa)
            # values(%s, %s)
            # """, ('test', 4.0 ))
            for id, values in student.items():
                cur.execute("""
                insert into Student(name, gpa, birth)
                values (%s,%s,%s);
            """, (values[0], values[1], values[2]))


def get_student(student_id):
    with pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            select * from Student where id=%s;
        """,(student_id,))
        data_student = cur.fetchall()
        return(data_student)


if __name__ == '__main__':

    delete_tables()
    create_db()
    #misha = Student('Mikhail')
    #add_student(misha)
   # print(misha.id_)
    #get_all_students()
    students = {1: ['Aleksey', 3.0, '13.04.1980'],
                     2: ['Dmitriy', 4.5, '15.04.1971'],
                     3: ['Sergey', 4.6, '10.01.1992'],
                     4: ['Volodka', 2.1, '03.02.1989'],
                     5: ['Poligraph', 2.0, '01.01.1961'],
                     6: ['Gerasim', 3.3, '13.11.2000']
                     }
    add_student(students)
    one_ = get_student(1)
    three_ = get_student(3)
    pprint(one_)
    pprint(three_)
    #get_all_students()


