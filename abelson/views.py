from flask import flash, render_template, request, session, redirect, url_for, jsonify
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
from abelson import app

login_manager = LoginManager()
login_manager.init_app(app)

class UserNotFoundError(Exception):
    pass

# Simple user class base on UserMixin
# http://flask-login.readthedocs.org/en/latest/_modules/flask/ext/login.html#UserMixin
class User(UserMixin):
    '''Simple User class'''
    USERS = {
        'admin':'password',
        'garrett':'password'
    }

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            return self_class(id)
        except UserNotFoundError:
            return None


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.get(id)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    else:
        return render_template('login.html')

@app.route('/login/check', methods=['POST'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
        return redirect(url_for('admin'))
    else:
        flash('Username or password incorrect')

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if current_user.is_authenticated == True:
        if request.method == "GET":
            return render_template('admin.html')
        if request.method == "POST":
            pass
    else:
        return redirect(url_for('index'))

@app.route("/admin/careers", methods=["GET", "POST"])
def admin_careers():
    if current_user.is_authenticated == True:
        if request.method == "GET":
            return render_template('admin_careers.html')
        if request.method == "POST":
            pass
    else:
        return redirect(url_for('index'))

@app.route("/admin/careers/new", methods=["GET", "POST"])
def admin_careers_new():
    if current_user.is_authenticated == True:
        if request.method == "GET":
            return render_template("admin_careers_new.html")
        if request.method == "POST":
            pass
    else:
        return redirect(url_for('index'))

@app.route("/admin/careers/<int:career_id>", methods=["GET", "POST"])
def edit_career(career_id):
    if current_user.is_authenticated == True:
        if request.method == "GET":
            return render_template("admin_careers_edit")
        if request.method == "POST":
            pass
    else:
        return redirect(url_for("index"))

@app.route("/careers", methods=['GET'])
def careers():
    return render_template('careers.html')
