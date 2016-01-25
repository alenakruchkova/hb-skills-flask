from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route('/application-form')
def application():
    """Gets application info"""

    # first_name = request.args.get("firstname")
    # last_name = request.args.get("lastname")
    # salary = request.args.get("salary")
    # job = request.args.get("positions")

    return render_template("application-form.html")
                            # fname=first_name,
                            # lname=last_name,
                            # required_salary=salary,
                            # position=job)


@app.route('/application-response')
def response():
    """ Gets information from application.

    Confirms application receival"""

    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    salary = request.args.get("salary")
    job = request.args.get("positions")

    return render_template("application-response.html",
                            fname=first_name,
                            lname=last_name,
                            required_salary=salary,
                            position=job)




if __name__ == "__main__":
    app.run(debug=True)
