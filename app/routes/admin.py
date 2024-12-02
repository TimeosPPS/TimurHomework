from flask import Flask, render_template, request, url_for, redirect
from . import app
from app.db.models.pizza import Pizza
from app.db.models.base import Session


@app.route('/admin_page/', methods=['GET', 'POST'])
def add_pizza():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = int(request.form['price'])
        image_url = request.form['image_url']

        session = Session()
        new_pizza = Pizza(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )
        session.add(new_pizza)
        session.commit()
        session.close()

    return render_template('admin_hub/configuration.html')
