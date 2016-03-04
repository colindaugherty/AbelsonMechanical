from flask import flash, render_template, request, session, redirect, url_for, jsonify
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from abelson import app, bcrypt
from . import db, defOfRandom, AbelsonEmail

import base64

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
    if(defOfRandom.LoginCheck(request)): 
        return url_for('admin')
    else:
        flash('Username or password incorrect')

    return url_for('login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html', locs=db.get_loc())

@app.route("/admin", methods=["GET"])
def admin():
    return render_template('admin.html', locs=db.get_loc())


@app.route("/admin/loc", methods=["POST"])
def admin_loc():
    db.update_loc(request.form)
    flash("Updated Successfully")
    return redirect(url_for('admin'))

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
        if request.form['name'] != "" and request.form['description'] != "":
            db.update_job(request.form, id)
            return jsonify(status="201", msg="Career Updated"), 201
        else:
            return jsonify(status="400", msg="Please fill in all fields."), 400

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
    return render_template('careers.html', jobs=db.get_jobs() )

@app.route("/contact", methods=['POST'])
def contact():
    if defOfRandom.formCheck(request.form):
        MSG = MIMEText("Hi,\nMy name is " + request.form['firstname'] + " " + request.form['lastname'] +
                       "\n" + "My email and phone are " + request.form['email'] + " " + request.form['phone'] +
                       "\n" + "My company and industry are " + request.form['company'] + " " + request.form['industry'] +
                       "\n" + request.form['msg'])
        MSG['subject'] = "Contact Question"
        MSG['From'] = 'Bob <abelsonmec@gmail.com>'
        MSG['To'] = 'abelsonmec@gmail.com'

        AbelsonEmail.smtp_sendEmail(AbelsonEmail.EMAIL_CONFIG, MSG)

        return jsonify(status="201", msg="Email sent."), 201
    else:
        return jsonify(status="400", msg="Please fill in all fields."), 400

@app.route("/careers/send", methods=["POST"])
def careers_send():
    if defOfRandom.formCheck(request.form):
        MSG = MIMEMultipart()
        txt_attach = MIMEText(
            "Hi,\nMy name is " + request.form['firstname'] + " " + request.form['lastname'] +
            "\n" + "My email and phone are " + request.form['email'] + " " + request.form['phone'] +
            "\n I am aplying for " + request.form["position"] + 
            "\n" + request.form["msg"] )
        MSG['Subject'] = "Contact Question"
        MSG['From'] = 'Bob <abelsonmec@gmail.com>'
        MSG['To'] = 'abelsonmec@gmail.com'
        pdf = request.files['application'].read()
        attachment = MIMEApplication(pdf, "pdf")
        attachment.add_header('content-disposition', 'attachment', filename='file.pdf')
        MSG.attach(txt_attach)
        MSG.attach(attachment)

        AbelsonEmail.smtp_sendEmail(AbelsonEmail.EMAIL_CONFIG, MSG)

        return jsonify(status="201", msg="Aplication submited."), 201
    else:
        return jsonify(status="400", msg="Please fill in all fields."), 400
