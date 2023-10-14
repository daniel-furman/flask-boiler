import os
from datetime import datetime

from flask import Flask, request


app = Flask(__name__)


@app.route("/v1/run_pipes", methods=["GET"])
def run_pipes():
    if request.method == "GET":
        try:
            now = datetime.now()  # current date and time
            date_time = now.strftime("%m_%d_%Y_%H_%M_%S")

            if not os.path.exists(f"data/raw/{date_time}"):
                os.mkdir(f"data/raw/{date_time}")

            temp_json = request.get_json()

            input_folder = temp_json["input_folder"]
            output_folder = temp_json["output_folder"]

            input_fpath = os.path.join(input_folder, "some_data.parquet")

            # some operation
            # <>

            output_fpath = os.path.join(
                output_folder, date_time, "some_results.parquet"
            )

            return {"input_fpath": input_fpath, "output_fpath": output_fpath}, 200

        except:
            return {
                "error": "Except block called, pipeline failed",
                "status": 404,
            }, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
