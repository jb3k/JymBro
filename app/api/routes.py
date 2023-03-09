from flask import render_template
from app import app
from app.forms.login import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1> Success!!! </h1>'
    return render_template('page.html', form=form)
