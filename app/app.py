import os
import logging
from datetime import datetime

from flask import Flask, request


app = Flask(__name__)


@app.route("/v1/run_pipeline", methods=["GET"])
def run_pipes():
    if request.method == "GET":
        try:
            # grab id for run (we use date time to second as id)
            now = datetime.now()  # current date and time
            date_time = now.strftime("%m_%d_%Y_%H_%M_%S")

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

            # create run folder at datetime
            if not os.path.exists(f"data/results/{date_time}"):
                os.mkdir(f"data/results/{date_time}")
                logging.warning(
                    f'<system logs> created a run folder at "data/results/{date_time}"'
                )

            # grab incoming json
            temp_json = request.get_json()
            input_fpath = temp_json["input_fpath"]
            output_folder = temp_json["output_folder"]

            # some operation
            # <>
            # now save results to docker container

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
