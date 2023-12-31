import os
import logging

from flask import Flask, request
import mysql.connector
from redis import Redis
from rq import Queue

from worker import get_datetime

r = Redis(host="redis", port=6379)
queue = Queue(connection=r)

app = Flask(__name__)


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


@app.route("/v1/grab_one_datetime", methods=["POST"])
def grab_one_datetime():
    if request.method == "POST":
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
