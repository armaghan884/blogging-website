from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/user_profile")
def user_profile():
    return render_template('user_profile.html')

if __name__ == '--main--':
    app.run()
    
