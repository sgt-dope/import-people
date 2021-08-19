import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

cmnd = os.popen("gp url 5432")
gitpod_url = cmnd.read().strip()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin@{gitpod_url}/users'
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(250), nullable=False)

# from models import Person
db.create_all()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        person1 = Person(first_name=request.form.get("first_name"), last_name=request.form.get("last_name"), email=request.form.get("email"))
        db.session.add(person1)
        db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
