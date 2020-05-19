from pprint import pprint

import psycopg2 as pg
import json


def create_db(target):  # создает таблицы
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
        create table if not exists users_base(
            id serial primary key,
            user_id numeric(15) not null,
            kpi numeric(15) not null,
            data varchar(1023) not null,
            view boolean
            );
        """)
        print('Таблица пользователя ', target, ' создана.')

def delete_tables():
    # удалить таблицу
    conn = pg.connect(
        dbname='hw_postgresql',
        user='test',
        password='1234'
    )
    cur = conn.cursor()
    cur.execute("""
    drop table if exists users_base;
    """)
    conn.commit()
    conn.close()
    print('Таблица удалена')


def add_user(user_id, kpi, data):  # добавляет нового пользователя
    with pg.connect(
            dbname='hw_postgresql',
            user='test',
            password='1234'
    ) as conn:
        cur = conn.cursor()
        cur.execute("""
            insert into users_base(user_id, kpi, data, view)
            values (%s, %s, %s, %s);
        """, (user_id, kpi,  data, False))
        # for id, values in student.items():
        #     cur.execute("""
        #         insert into Student(name, gpa, birth)
        #         values (%s,%s,%s);
        #     """, (values[0], values[1], values[2]))

def get_one():
    try:
        with pg.connect(
                dbname='hw_postgresql',
                user='test',
                password='1234'
        ) as conn:
            cur = conn.cursor()
            cur.execute("""
                select users_base.data
                from users_base 
                WHERE view=FALSE;
             """ )
            # one_user = cur.fetchall()
            one_user = cur.fetchone()
            tmp = one_user[0]
            tmp = eval(tmp)
            id_ = tmp['id']
            cur = conn.cursor()
            cur.execute("""
                UPDATE users_base SET view=TRUE
                WHERE user_id=%s;
                """,(id_,))
    #            WHERE user_id="id";
    except:
        print('В БД не осталось не просмотренных пользователей!')
        return False
    return tmp