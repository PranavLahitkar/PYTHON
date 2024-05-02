from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple dictionary to hold user credentials (in a real application, use a database)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username exists and if the password is correct
    if username in users and users[username] == password:
        # Successful login
        return f"Welcome, {username}!"
    else:
        # Failed login
        return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
