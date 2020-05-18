import psycopg2 as pg


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
            name varchar(254) not null,
            view boolean
            );
        """)
        print('Таблица пользователя ', target, ' создана.')

create_db(1)