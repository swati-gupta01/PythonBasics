from flask import Flask,render_template,url_for,flash ,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from Social_N_Flask.forms import RegistrationForm,LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']='234292f9a3ebfa7af753c06fb239ec7b' #cokkies unmodified
app.config['SQLALCHEMY_DATABASE_URI']='sq lite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    username=db.Column(db.String(20),unique=True ,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20) ,nullable=False ,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return  f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False )
    date_posted = db.Column(db.Datetime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id =db.Column(db.Interger ,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


posts=[ {
    'author':'Swati',
    'title':'My 1st Blog',
    'content':'content of 1st post',
    'date_posted':'April 20 ,2018'
},{'author':'Nishu',
    'title':'My 2nd Blog',
    'content':'content of 2nd post',
    'date_posted':'April 21 ,2018'}]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return  redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='login',form=form)

if __name__=='__main__':
    app.run(port=4009,debug=True)