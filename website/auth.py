<<<<<<< HEAD
from asyncio.windows_events import NULL
=======
>>>>>>> f359d6af7bb635398222ae5134030f00ffa83cb4
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import MusicCatalog, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 6 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/catalog', methods=['GET', 'POST'])
@login_required
def catalog():
<<<<<<< HEAD
    search_value = request.form.get('search_string')
    search = "%{}%".format(search_value)
    results = MusicCatalog.query.filter(MusicCatalog.pieceName.like(search)).all()
    show_piece = MusicCatalog.query.order_by(MusicCatalog.user_id)
    return render_template("music_catalog.html", user=current_user, show_piece=show_piece, results=results, search=search)
    

    

    
=======
    show_piece = MusicCatalog.query.order_by(MusicCatalog.user_id)

    return render_template("music_catalog.html", user=current_user, show_piece=show_piece)

>>>>>>> f359d6af7bb635398222ae5134030f00ffa83cb4
