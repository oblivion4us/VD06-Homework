from flask import render_template, request, redirect, url_for
from form_app import app

cards =[]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        age = request.form.get('age')
        hobby = request.form.get('hobby')

        if name and city and age and hobby:
            cards.append({'name': name,
                          'city': city,
                          'age': age,
                          'hobby': hobby
                          })
            return redirect(url_for('index'))

    return render_template('index.html', cards=cards)
