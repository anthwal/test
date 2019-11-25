import os
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
DATABASE_URL="postgres://xecvnfwmxrcxsh:23af39a6155c42d18cdc1e44565b7ad5826c793736458e8b70c04ac2e3f6ff61@ec2-23-21-70-39.compute-1.amazonaws.com:5432/db6gh7v6itdlja"

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/signupv",methods=["POST","GET"])
def signupv():
    username=request.form.get("username")
    email=request.form.get("email")
    password=request.form.get("password")
    db.execute("INSERT INTO customer(username,email,password) VALUES(:username,:email,:password)",
               {"username": username, "email": email, "password": password})
    db.commit()
    db.close()
    return render_template("login.html")    

if __name__ == "__main__":
    app.run()