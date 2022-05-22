from core import get_db_cursor


def first_migration():
    """Function for init aplinists table"""
    cursor = get_db_cursor()
    sql_init_query = """
    CREATE TABLE member (id INTEGER PRIMARY KEY, name STRING NOT NULL, address STRING NOT NULL);
    CREATE TABLE country (id INTEGER PRIMARY KEY, name STRING NOT NULL);
    CREATE TABLE district(
    id INTEGER PRIMARY KEY,
    country_id INTEGER, FOREIGN KEY(country_id) REFERENCES country (id)
    );
    CREATE TABLE mountain (
    id INTEGER PRIMARY KEY,
    name STRING NOT NULL,
    high REAL NOT NULL,
    district_id INTEGER, FOREIGN KEY(district_id) REFERENCES district (id)
    );
    CREATE TABLE ascent (
    id INTEGER PRIMARY KEY,
    start TEXT NOT NULL,
    end TEXT NOT NULL,
    mountain_id INTEGER, FOREIGN KEY(mountain_id) REFERENCES mountain (id)
    );
    CREATE TABLE ascent_members(
    id INTEGER PRIMARY KEY,
    member_id INTEGER, 
    ascent_id INTEGER,
    FOREIGN KEY(member_id) REFERENCES member (id),
    FOREIGN KEY(ascent_id) REFERENCES ascent (id)
    );
    """

    cursor.executescript(sql_init_query)
    cursor.close()


first_migration()

def second_migration():
    sql_query = """
    ALTER TABLE district add name STRING;
    """
    cursor = get_db_cursor()
    cursor.executescript(sql_query)
    cursor.close()

second_migration()