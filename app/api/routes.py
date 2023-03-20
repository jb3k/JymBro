from flask import render_template, redirect, session
from app import app
from app.forms.login import LoginForm


def track_views():
    if 'views' in session:
        session['views'] = session.get('views') + 1
    else:
        session['views'] = 1


@app.route('/views')
def views():
    return "Total visits: {}".format(session.get('visits'))


@app.route('/views/reset', methods=["POST"])
def reset_views():
    views = session.pop('views', None)
    return f'Reset views (previous {views})'



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('page.html', form=form)
