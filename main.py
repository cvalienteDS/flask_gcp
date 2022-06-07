from flask import Flask
from flask import request, escape

app = Flask(__name__)


@app.route("/")
def index():
    celsius = request.args.get("celsius", "")  # The request.args dictionary contains any data submitted with an HTTP GET request
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
            """<h1>Web app to convert Celsius temperatures to Fahrenheit temperatures</h1>
            <form action="" method="get">
                Celsius temperature: <input type="text" name= "celsius">
                <input type="submit" value= "Convert to Fahrenheit">
            </form>"""
            + "Fahrenheit: "
            + fahrenheit
    )


@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
# celsius = input("Celsius: ")
# print("Fahrenheit:", fahrenheit_from(celsius))

# hello-app-352407
