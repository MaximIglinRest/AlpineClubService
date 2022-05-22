from core import get_db_cursor


def get_mountains_with_ascent() -> dict:
    cursor = get_db_cursor()
    select_query = """
    SELECT mountain.id, mountain.name, a.id, a.start, a.end
    FROM mountain left join ascent a on a.mountain_id=mountain.id
    ORDER BY a.start
    """
    cursor.execute(select_query)
    result = {
        mountain: {
            "id": mountain_id,
            "ascent_id": ascent_id,
            "ascent_start": ascent_start,
            "ascent_end": ascent_end
        } for mountain_id, mountain, ascent_id, ascent_start, ascent_end in cursor.fetchall()
    }

    cursor.close()
    return result


def add_mountain(mountain_name: str, mountain_height: int, district_id) -> None:
    cursor = get_db_cursor()
    insert_query = f"""
    INSERT INTO mountain(name, high, district_id) VALUES ({mountain_name}, {mountain_height}, {district_id}); 
    """
    cursor.execute(insert_query, 'mountain')
    cursor.close()
    return


add_mountain("Эверест", 5555, 1)
get_mountains_with_ascent()
