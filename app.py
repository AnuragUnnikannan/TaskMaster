from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        person = str(request.form["person_name"])
        task = str(request.form["task_name"])
        return redirect("/upload?person="+person+"&task="+task)
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        return redirect("/")
    person = request.args.get("person")
    task = request.args.get("task")
    return render_template("upload.html", person_name = f"Person Name: {person}", task_name = f"Task Name: {task}")

if __name__ == "__main__":
    app.run(debug=True)