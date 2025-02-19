from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Simple Flask App</title>
        </head>
        <body>
            <h1>I am Ahmad Raza.</h1>
            <p>VERCEL SCENES.</p>
        </body>
        </html>
    """)