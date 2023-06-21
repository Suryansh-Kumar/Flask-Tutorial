from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        'id': 2,
        'title': "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 15,00,000"
    },
    {
        'id': 3,
        'title': "Frontend Engineer",
        "location": "Remote",
        "salary": "Rs. 12,00,000"
    },
    {
        'id': 4,
        'title': "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$150,000"
    }
]


@app.route("/")
def home():
    return render_template("index.html", jobs=JOBS, company_name="Jovian")


@app.route("/about")
def about():
    return "<h1>ABOUT</h1>"


@app.route("/projects")
def projs():
    return "<h1>PROJECTS</h1>"


@app.route("/services")
def services():
    return "<h1>SERVICES</h1>"


@app.route("/blogs")
def blogs():
    return "<h1>BLOGS</h1>"

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
