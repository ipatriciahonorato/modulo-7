from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')
alchemyEngine = create_engine(DATABASE_URL, pool_recycle=3600)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notes")
def notes():
    # Connect to the database
    dbConnection = alchemyEngine.connect()

    # Fetch data from the person table
    dataFrame = pd.read_sql("select * from notas", dbConnection)
    print(dataFrame)

    # Close the database connection
    dbConnection.close()
    return render_template("notas.html", items= dataFrame.to_dict(orient='records'))

@app.route("/add", methods=['POST'])
def add():
    try:
        # Connect to the database
        dbConnection = alchemyEngine.connect()
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')

        # Avoid SQL injection
        stmt = text("INSERT INTO notas (titulo, descricao) VALUES (:titulo, :descricao)")
        dbConnection.execute(stmt, {"titulo": titulo, "descricao": descricao})
        dbConnection.commit()  # Commit the transaction
    except Exception as e:
        print(f"Error: {e}")
    finally:
        dbConnection.close()
    return redirect(url_for('notes'))

@app.route("/delete/<int:item_id>", methods=['POST'])
def delete(item_id):
    print(f"Attempting to delete item with ID: {item_id}")
    try:
        # Connect to the database
        dbConnection = alchemyEngine.connect()

        # Avoid SQL injection
        stmt = text("DELETE FROM notas WHERE id = :item_id")
        dbConnection.execute(stmt, {"item_id": item_id})
        dbConnection.commit()  # Commit the transaction
    except Exception as e:
        print(f"Error: {e}")
    finally:
        dbConnection.close()
    return redirect(url_for('notes'))

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the provided credentials are correct
    if username == "patriciahonorato" and password == "#123!":
        # If correct, redirect to the notes page
        return redirect(url_for('notes'))
    else:
        # If incorrect, show an error or redirect back to the login page with a message
        return "Invalid credentials, please try again."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
