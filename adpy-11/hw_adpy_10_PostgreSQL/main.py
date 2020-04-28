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
        print('Таблица студентов создана.')
        cur.execute("""
        create table if not exists Course(
            id serial primary key,
            name varchar(100) not null
            );
        """)
        print('Таблица курсов создана.')

        cur.execute("""
        create table if not exists student_course(
            id serial primary key,
            student_id integer references Student(id),
            course_id integer references Course(id));
        """)
        print('Таблица связей создана.')


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
    cur.execute("""
    drop table if exists Course;
    """)
    conn.commit()
    cur.execute("""
    drop table if exists student_course;
    """)
    conn.commit()
    conn.close()
    print('Таблицы удалены')


def get_students(course_id):  # возвращает студентов определенного курса
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            select student.name 
            from student 
            join student_course on student.id = student_course.student_id 
            join course on course.id = student_course.course_id 
            where course.id = %s
        """, (course_id,))
        students_by_course = cur.fetchall()
        return students_by_course


def get_all_students():  # функция для отладки
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            select * from Student;
        """)
        return cur.fetchall()


def add_new_course(course_name):  # добавляем новый курс в базу
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            insert into Course (name)
            values (%s)
            """, (course_name,))


def add_students(course_id, students):  # создает студентов и
    # записывает их на курс
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        for student in students:
            cur.execute("""
            insert into student_course (student_id, course_id)
            values (%s, %s)
            """, (student, course_id))


def add_student(student):  # просто создает студента
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
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
        """, (student_id,))
        data_student = cur.fetchall()
        return (data_student)


if __name__ == '__main__':
    # delete_tables()
    # create_db()
    # misha = Student('Mikhail')
    # add_student(misha)
    # print(misha.id_)
    # get_all_students()
    students = {1: ['Aleksey', 3.0, '13.04.1980'],
                2: ['Dmitriy', 4.5, '15.04.1971'],
                3: ['Sergey', 4.6, '10.01.1992'],
                4: ['Volodka', 2.1, '03.02.1989'],
                5: ['Poligraph', 2.0, '01.01.1961'],
                6: ['Gerasim', 3.3, '13.11.2000']
                }
    # add_student(students)
    # print('Студенты с курса "Пайтон для Чайников":', lambda x[0]: students_course_adpy_11)
    # add_new_course('adpy_11')
    # add_new_course('pyda-8')
    # add_students(1, students_course_adpy_11)
    # add_students(2, students_course_pyda_8)
    # get_all_students()
    students_course_adpy_11 = [1, 2, 4, 6]
    students_course_pyda_8 = [3, 5]
    students_from_adpy = get_students(1)
    print('Студенты, которые записались на курс "Python для чугунных чайников": ')
    for i in students_from_adpy:
        print(i[0] + '   ', end='')
    print('\n')
    students_from_pyda = get_students(2)
    print('Мечтатели, что верят, что станут Дата-сайентистами: ')
    for i in students_from_pyda:
        print(i[0] + '   ', end='')
