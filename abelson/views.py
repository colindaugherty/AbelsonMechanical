from flask import flash, render_template, request, session, redirect, url_for, jsonify
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

from abelson import app, bcrypt
import abelson.db

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

@app.route("/admin", methods=["GET"])
def admin():
    return render_template('admin.html')


@app.route("/admin/loc", methods=["POST"])
def admin_loc(loc):
    db.update_loc()
    return jsonify(status="201", msg="Updated Location's information"), 201


@app.route("/loc/get", methods=["GET"])
def loc_get():
    db.get_loc()
    return jsonify(status="200"), 200

@app.route("/admin/careers", methods=["GET"])
def admin_careers():
    return render_template('admin_careers.html')


@app.route("/admin/careers/new", methods=["GET", "POST"])
def admin_careers_new():
    return render_template("admin_careers_new.html")

@app.route("/admin/careers/<int:career_id>", methods=["GET", "POST"])
def edit_career(career_id):
    return render_template("admin_careers_edit")


@app.route("/admin/careers/update", methods=["POST"])
def admin_careers_update():
         db.update_job()
         return jsonify(status="201", msg="Career Updated"), 201

@app.route("/admin/careers/add", methods=["POST"])
def admin_careers_add(data):
    if data.name != "" and data.description != "":
        db.new_job(data)
        return jsonify(status="201", msg="Job added successfully."), 201
    else:
        return jsonify(status="false")

@app.route("/job/get", methods=["GET"])
def job_get():
    db.get_job()
    return jsonify(status="hi")

@app.route("/careers", methods=['GET'])
def careers():
    return render_template('careers.html')
