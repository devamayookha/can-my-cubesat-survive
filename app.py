from flask import Flask, render_template, request
from simulator.power_model import run_simulation

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():

    try:
        altitude = float(request.form.get("altitude", ""))
        battery = float(request.form.get("battery", ""))
        panel = float(request.form.get("panel", ""))
        payload = float(request.form.get("payload", ""))

        if altitude <= 0:
            raise ValueError

        if battery <= 0:
            raise ValueError

        if panel <= 0:
            raise ValueError

        if payload < 0:
            raise ValueError

    except ValueError:

        error = (
            "Please enter valid values. "
            "Altitude, Battery Capacity, and Solar Panel Area "
            "must be greater than 0. Payload Power cannot be negative."
        )

        return render_template(
            "index.html",
            error=error
        )

    result = run_simulation(
        altitude,
        battery,
        panel,
        payload
    )

    return render_template(
        "result.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)