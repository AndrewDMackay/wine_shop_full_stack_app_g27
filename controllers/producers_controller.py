
import re

from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import producer_repository
from repositories import wine_repository

from models.wine import Wine
from models.producer import Producer

producers_blueprint = Blueprint("producers", __name__)


# Index..
# GET '/producers/', finalised..

@producers_blueprint.route("/producers", strict_slashes=False, methods=['GET'])
def producers():
    producers = producer_repository.select_all()
    return render_template('producers/index.html', all_producers = producers)


# NEW
# GET '/producers/new'
# Returns an HTML form to the browser, finalised..

@producers_blueprint.route("/producers/new", strict_slashes=False, methods=['GET'])
def new_wines():
    producers = producer_repository.select_all()
    return render_template('producers/new.html', all_producers = producers)


# CREATE
# POST '/producers/'
# Receives the data from the form to insert into the database, finalised..

@producers_blueprint.route("/producers", strict_slashes=False, methods=['POST'])
def create_wine():
    wine_name = request.form['wine-name']
    producer_id = request.form['producer_id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    net_price = request.form['net-price']
    sell_price = request.form['sell-price']
    wine = Wine(wine_name, producer, stock, net_price, sell_price)
    wine_repository.save(wine)
    return redirect('/producers')


# # SHOW
# # GET '/producers/<id>', finalised..

@producers_blueprint.route("/producers/<id>", strict_slashes=False, methods=['GET'])
def show_wine(id):
    wine = wine_repository.select(id)
    return render_template('producers/show.html', wine = wine)


# EDIT
# GET '/producers/<id>/edit', finalised..

@producers_blueprint.route("/producers/<id>/edit", strict_slashes=False, methods=['GET'])
def edit_wine(id):
    wine = wine_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('producers/edit.html', wine = wine, all_producers = producers)


# UPDATE
# PUT '/producers/<id>'

@producers_blueprint.route("/producers/<id>", strict_slashes=False, methods=['POST'])
def update_wine(id):
    wine_name = request.form['wine-name']
    producer_id = request.form['producer-id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    net_price = request.form['net-price']
    sell_price = request.form['sell-price']
    wine = Wine(wine_name, producer, stock, net_price, sell_price)
    wine_repository.update(wine)
    return redirect('/producers')


# DELETE
# DELETE '/producers/<id>', finalised..

@producers_blueprint.route("/producers/<id>/delete", strict_slashes=False, methods=['POST'])
def delete_wine(id):
    wine_repository.delete(id)
    return redirect('/producers')