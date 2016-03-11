from flask import flash, render_template, request, session, redirect, url_for, jsonify

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from abelson import app, bcrypt
from . import db, defOfRandom, AbelsonEmail

import base64


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'sid' in session.keys():
            return redirect(url_for('admin'))
        return render_template('login.html')
    elif request.method == 'POST':
        keys = request.form.keys()
        if "username" in keys and "password" in keys:
            user = db.get_user(request.form['username'])
            print(user)
            if user:
                user = user[0]
                print(request.form['password'])
                print(user['password'])
                if request.form['password'] == user['password']:
                    session['sid'] = user['id']
                    return redirect(url_for('admin'))
                flash('Invalid Login')
                return render_template("login.html")
        flash("Invalid Login")
        return render_template('login.html')


@app.route('/logout')
def logout():
    if 'sid' in session.keys():
        del session['sid']

    return redirect(url_for('login'))

@app.route("/")
def index():
    return render_template('index.html', locs=db.get_loc())

@app.route("/admin", methods=["GET"])
def admin():
    if 'sid' not in session.keys():
        return redirect(url_for('login'))

    return render_template('admin.html', locs=db.get_loc())


@app.route("/admin/loc", methods=["POST"])
def admin_loc():
    if 'sid' not in session.keys():
        return redirect(url_for('login'))

    if (defOfRandom.CheckLoc(request.form)):
         db.update_loc(request.form)
         flash("Updated Successfully")
         return redirect(url_for('admin'))
    else:
        return render_templare("admin.html", msg="Some of the fields are not put in right. Plese fix.")

@app.route("/loc/get", methods=["GET"])
def loc_get():
    try:
        loc = db.get_loc()
        return jsonify(status="200", location=loc), 200
    except Exception as e:
        return jsonify(status="500", message=str(e)), 500

@app.route("/admin/careers", methods=["GET"])
def admin_careers():
    if 'sid' not in session.keys():
        return redirect(url_for('login'))

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
