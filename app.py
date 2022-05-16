from db.core import test_db, get_db_cursor

if __name__ == "__main__":
    test_db()
    cursor = get_db_cursor()
    cursor.close()