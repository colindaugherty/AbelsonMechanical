from flask import flash, render_template, request, session, redirect, url_for, jsonify
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

from abelson import app, bcrypt
from . import db

login_manager = LoginManager()
login_manager.init_app(app)

class UserNotFoundError(Exception):
    pass


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
    try:
        loc = db.get_loc()
        return jsonify(status="200", location=loc), 200
    except Exception as e:
        return jsonify(status="500", message=str(e)), 500

@app.route("/admin/careers", methods=["GET"])
def admin_careers():
    return render_template('admin_careers.html', jobs=db.get_jobs() )


@app.route("/admin/careers/new", methods=["GET", "POST"])
def admin_careers_new():
    return render_template("admin_careers_new.html")

@app.route("/admin/careers/<id>", methods=["GET", "POST"])
def admin_careers_update(id):
    if (request.method == "GET"):
        job = db.get_job_by_id(id) 
        return render_template("admin_careers_update.html", job = job[0])   
    if (request.method == "POST"):
         db.update_job(id)
         return jsonify(status="201", msg="Career Updated"), 201

@app.route("/admin/careers/add", methods=["POST"])
def admin_careers_add():
    if request.form['name']!= "" and request.form['description'] != "":
        db.new_job(request.form)
        #print(request.form)
        return jsonify(status="201", msg="Job added successfully."), 201
    else:
        return jsonify(status="400", msg="Please fill in all fields."), 400

@app.route("/job/get", methods=["GET"])
def job_get():
    print("got here")
    jobs = db.get_job()
    return jsonify(status="200", msg="got the jobs"), 200

@app.route("/careers", methods=['GET'])
def careers():
    return render_template('careers.html')
