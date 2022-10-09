import flask
from flask import Flask
from flask_cors import CORS, cross_origin
from user_entity import User
from address_vo import Address
from friends_vo import Friends
from user_repository import User_repository

app = Flask(__name__)
CORS(app)



@app.route("/v1/user", methods=["PUT"])
@cross_origin()
def starting_url():
    json_data = flask.request.get_json()
    user = json_data["name"]
    user_name   = json_data["user_name"] 
    email = json_data["email"]
    phone = json_data["phone"]
    gender = json_data["gender"]
    password = json_data["password"]
    date_of_birth = "01/01/2018"
    street_name = json_data["street_name"]
    street_number = json_data["street_number"]
    city = json_data["city"]
    post_code = json_data["post_code"]
    country = json_data["country"]
    address = Address(street_name, street_number, city, post_code, country)
    user = User(1, user, user_name, email, phone, gender, password, address, Friends(1,[0]), 1)
    print(vars(address))
    print(vars(user.friend))
    print(vars(user))
    response = User_repository.store_user(user)
    return response

@app.route("/v1/user", methods=["GET"])
@cross_origin()
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        response = User_repository.get_user(user)
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            flash("Incorrect username/password!", "danger")
    return render_template('auth/login.html',title="Login")
