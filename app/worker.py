import mysql.connector
from datetime import datetime
import uuid


def get_connection():
    config = {
        "user": "root",
        "password": "root",
        "host": "db",
        "port": "3306",
        "database": "sample_db",
    }
    conn = mysql.connector.connect(**config)

    return conn


def get_datetime():
    db_conn = get_connection()
    cursor = db_conn.cursor(prepared=True)

    now = datetime.now()  # current date and time
    datetime_id = now.strftime("%m_%d_%Y_%H_%M_%S")
    random_uuid = uuid.uuid4()

    try:
        cursor.execute(
            "INSERT INTO datetime_table (temp_entry_id, datetime_id) VALUES (?, ?)",
            (random_uuid, datetime_id),
        )
        db_conn.commit()

    except Exception as e:
        print(e)

    cursor.close()
    return 200
