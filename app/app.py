from flask import Flask, request

app = Flask(__name__)


@app.route("/v1/grab_one_temp", methods=["GET"])
def grab_one_temp():
    if request.method == "GET":
        temp_json = request.get_json()

        hello_world = temp_json["hello world"]

        if hello_world is None:
            return {"error": "Params not found", "status": 404}, 404
        else:
            return {
                "hello world": hello_world,
            }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
