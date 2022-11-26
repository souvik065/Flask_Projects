
from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegisterationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'corey Schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Aplril 20, 2018'
    },
    {
        'author': 'Souvik Bhattacharya',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been created! you are nowable to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have benn logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check usernam and password', 'danger')
    return render_template('login.html', title='Login', form=form)
