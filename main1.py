from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import PrimaryKeyConstraint
#from flask_login import UserMixin
#from werkzeug.security import generate_password_hash,check_password_hash
#from flask_login import login_user,logout_user




local_server=True
app = Flask(__name__,template_folder='templates')

app.secret_key='prasanna'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3307/ems1'
db=SQLAlchemy(app)

class Test1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

#class Login(db.Model):
 #   enroll=db.Column(db.Integer,Primary_Key=True)
 #   email=db.Column(db.String(20),unique=True)
 #   password=db.Column(db.String(1000),unique=True)


    

@app.route("/")
def home():
    return render_template('bootstrap.html')
       
@app.route("/Faculty")
def Faculty():
    return render_template('faculty.html')

@app.route("/Visitors")
def Visitors():
    return render_template('visitors.html')              
   

@app.route("/Login")
def login():
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
        

      #  new_login=db.engine.execute(f"INSERT INTO `login` (`enroll`,`email`,`password`) VALUES ('DE20513))


    return render_template('signup.html')


@app.route('/test1')
def test1():
    try:
        Test1.query.all()

        return "my database is connected"
    except:
        
        return "my database is not connected"

    
app.run(debug=True)

