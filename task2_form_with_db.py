from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
# MongoDB Atlas connection
MONGO_URI=os.getenv("MONGO_URI")
app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")

        try:
            # Try inserting into MongoDB
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            # Show error on the same page (no redirect)
            return render_template("form.html", error=str(e))

    return render_template("form.html")

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)