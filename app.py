from flask import Flask, request, render_template_string

app = Flask(__name__)

users = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>

    <form method="POST">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>

        <button type="submit">Register</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}

    <h3>Registered Users</h3>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} - {{ user.email }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        users.append({
            "name": name,
            "email": email,
            "password": password
        })

        message = f"Registration successful for {name}"

    return render_template_string(
        HTML,
        message=message,
        users=users
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
