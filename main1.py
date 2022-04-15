from tokenize import String
from flask import Flask, redirect, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user



local_server=True
app = Flask(__name__,template_folder='templates')

app.secret_key='prasanna'



# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3307/ems1'
db=SQLAlchemy(app)



class Test1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Login(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    enroll=db.Column(db.String(10),unique=True)
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000),unique=True)

    
  

@app.route("/")
def home():
    return render_template('bootstrap.html')
       
@app.route("/Faculty")
def Faculty():
    return render_template('faculty.html')

@app.route("/Visitors")
def Visitors():
    return render_template('visitors.html')              
   

@app.route("/Login",methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        log=Login.query.filter_by(email=email).first()

        if log and check_password_hash(log.password,password):
            login_user(log)
            return redirect(url_for("Faculty"))
        else:
            print("invalid credentials")
            return render_template('login.html')    
        
    return render_template('login.html')

@app.route("/Logout")
def logout():
    return render_template('login.html')


@app.route("/SignUp",methods=['POST','GET'])
def signup():

    if request.method== "POST":

        enrollmentnumber=request.form.get('enrollmentnumber')
        email=request.form.get('email')
        password=request.form.get('password')
        log=Login.query.filter_by(email=email).first()
        if log:
            print("email already exists")
            return render_template('/signup.html')

        encpassword=generate_password_hash(password)
        new_log=db.engine.execute(f"INSERT INTO `login` (`enroll`,`email`,`password`) VALUES ('{enrollmentnumber}','{email}','{encpassword}')")
        return render_template("login.html")

    return render_template('signup.html')


@app.route('/test1')
def test1():
    try:
        Test1.query.all()

        return "my database is connected"
    except:
        
        return "my database is not connected"

    
app.run(debug=True)
