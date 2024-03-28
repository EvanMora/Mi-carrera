from flask import Flask, render_template, request, redirect, url_for
from utils import query, departaments, cities, uni, career

app = Flask(__name__)
info = {"departament": "", "city": "", "uni": ""}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/departament")
def departament():
    list_departaments = departaments()
    return render_template("departament.html", list_departaments=list_departaments)


@app.route("/city", methods=["POST"])
def city():
    global info
    info["departament"] = request.form["departament"]
    return render_template("cities.html", list_cities=cities(info["departament"]))


@app.route("/unis", methods=["POST"])
def unis():
    global info
    info["city"] = request.form["city"]
    return render_template("unis.html", list_unis=uni(info["city"]))


@app.route("/redirect", methods=["POST"])
def redir():
    return redirect(f"/careers/{request.form['program']}")


@app.route("/careers", methods=["POST"])
def careers():
    global info
    info["uni"] = request.form["uni"]
    return render_template("careers.html", careers=career(info["city"], info["uni"]))


@app.route("/careers/<career_id>")
def career_info(career_id):
    data = query(
        f"""
                SELECT * FROM programas
                WHERE ID == {career_id}
                """
    )
    return render_template("career.html", data=data[0])


if __name__ == "__main__":
    app.run()
