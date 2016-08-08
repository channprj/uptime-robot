# views.py
from flask import render_template
from flask import flash
from flask import redirect
import app
from .forms import SignUpForm

# init
@app.route('/signup', methods=['GET', 'POST])
def sign_in():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Sign In requested... ')
        return redirect('/')

    return render_template('sign_up.html', title='Sign In', form=form)
