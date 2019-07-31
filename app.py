from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't already taken
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in', methods = ['GET','POST'])
def logged_in():
    if request.method == 'POST':
        update_fav_food
    print("login_session['name'] is : " + login_session["name"])
    fav = get_user(login_session['name']).fav_food
    return render_template('logged.html',fav=fav)


@app.route('/logout')
def logout():
    login_session['logged_in']= False
    login_session['name']= None
    return home()
'''
@app.route('/favorite food')
def update_food():
    # Get the user (of username)
    user = get_user(username)
    # Update the user's fav_food to favoritefood
    user.edit_fav_food(favoritefood)
'''



if __name__ == '__main__':
    app.run(debug=True)
