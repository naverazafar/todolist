from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
  return render_template("home.html")

@app.route("/add")
def addTask():
  return "Add Task Site"

@app.route("/delete")
def deleteTask():
  return "Delete Task Site"

if __name__ == "__main__":
  app.run()