import os
import logging

from flask import Flask, request
import mysql.connector
from redis import Redis
from rq import Queue

from async import get_datetime

r = Redis(host="redis", port=6379)
queue = Queue(connection=r)

app = Flask(__name__)

# create folder structure within docker container
if not os.path.exists(f"data"):
    os.mkdir(f"data")
if not os.path.exists(f"data/raw"):
    os.mkdir(f"data/raw")
if not os.path.exists(f"data/raw/cleaned"):
    os.mkdir(f"data/raw/cleaned")
if not os.path.exists(f"data/raw/received"):
    os.mkdir(f"data/raw/received")
if not os.path.exists(f"data/raw/working"):
    os.mkdir(f"data/raw/working")
if not os.path.exists(f"data/results"):
    os.mkdir(f"data/results")


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


@app.route("/v1/run_pipe", methods=["PUT"])
def run_pipe():
    if request.method == "PUT":
        queue.enqueue(get_datetime)
        return {"success": "async worker queued", "status": 200}, 200


@app.route("/v1/grab_datetimes", methods=["GET"])
def grab_datetimes():
    if request.method == "GET":
        # grab all temps from db
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sample_table")
        response_datetimes = cursor.fetchall()
        cursor.close()
        connection.close()
        return {"response_datetimes": response_datetimes}, 200


@app.route("/v1/grab_one_datetime", methods=["GET"])
def grab_one_datetime():
    if request.method == "GET":
        # grab temp from db with json input
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        temp_json = request.get_json()

        datetime_id = temp_json["datetime_id"]

        cursor.execute(
            f'SELECT * FROM sample_table WHERE datetime_id = "{datetime_id}"',
        )
        response_temp = cursor.fetchone()
        cursor.close()
        connection.close()

        if response_temp is None:
            return {"error": "Params not found", "status": 404}, 404
        else:
            return {
                "id": response_temp["temp_entry_id"],
                "datetime_id": response_temp["datetime_id"],
            }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
