import json
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/blogs")
def blogs_list():
    c = len(os.listdir("db"))
    return render_template("blogs.html", count=c)

@app.route("/blog/<pk>")
def blog_detail(pk):
    with open(f"db/blog{pk}.json", "r") as f:
        data = json.load(f)
    return render_template("blog.html", **data)

@app.route("/user/<username>")
def hello(username):
    return f"<h3> Hello {username}</h3>"

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        a1 = request.form.get("a1")
        a2 = request.form.get("a2")
        action = request.form.get("action")
        a1, a2 = int(a1), int(a2)
        match action:
            case "add":
                result = a1 + a2
            case "sub":
                result = a1 - a2
            case "mul":
                result = a1 * a2
            case "div":
                result = a1 / a2
            case "up":
                result = a1 ** a2
            case "%div":
                result = a1 % a2

        return render_template("calculate.html", natija=result)

@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    if request.method == "GET":
        return render_template("new-blog.html")
    else:
        title = request.form.get("title")
        body = request.form.get("body")
        data = {
            "title": title,
            "body": body
        }
        c = len(os.listdir("db"))
        with open(f"db/blog{c + 1}.json", "w") as f:
            json.dump(data, f)
        message = "Blog successfully created"
        return render_template("blogs.html", message=message)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
