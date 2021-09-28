

import re

from controllers.producers_controller import producers

from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import producer_repository
from repositories import wine_repository

from models.wine import Wine
from models.producer import Producer


wines_blueprint = Blueprint("wines", __name__)


# Index..
# GET '/wines/', [ Finalised ]

@wines_blueprint.route("/wines", strict_slashes=False, methods=['GET'])
def wines():
    wines = wine_repository.select_all()
    producers = producer_repository.select_all()
    return render_template('wines/index.html', all_wines = wines, all_producers = producers)


# NEW
# GET '/wines/new'
# Returns an HTML form to the browser, [ Finalised ]

@wines_blueprint.route("/wines/new", strict_slashes=False, methods=['GET'])
def new_wines():
    producers = producer_repository.select_all()
    return render_template('wines/new.html', all_producers = producers)


# CREATE
# POST '/wines/'
# Receives the data from the form to insert into the database, [ Finalised ]

@wines_blueprint.route("/wines", strict_slashes=False, methods=['POST'])
def create_wine():
    wine_name = request.form['wine-name']
    producer_id = request.form['producer_id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    net_price = request.form['net-price']
    sell_price = request.form['sell-price']
    wine = Wine(wine_name, producer, stock, net_price, sell_price)
    wine_repository.save(wine)
    return redirect('/wines')


# # SHOW
# # GET '/wines/<id>', [ Finalised ]

@wines_blueprint.route("/wines/<id>", strict_slashes=False, methods=['GET'])
def show_wine(id):
    wine = wine_repository.select(id)
    return render_template('wines/show.html', wine = wine)


# EDIT
# GET '/wines/<id>/edit', [ Finalised ]

@wines_blueprint.route("/wines/<id>/edit", strict_slashes=False, methods=['GET'])
def edit_wine(id):
    wine = wine_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('wines/edit.html', wine = wine, all_producers = producers)


# UPDATE
# PUT '/wines/<id>'

@wines_blueprint.route("/wines/<id>", strict_slashes=False, methods=['POST'])
def update_wine(id):
    producer_id = request.form['producer-id']
    producer = producer_repository.select(producer_id)
    wine_name = request.form['wine-name']
    stock = request.form['stock']
    net_price = request.form['net-price']
    sell_price = request.form['sell-price']
    wine = Wine(wine_name, producer, stock, net_price, sell_price, id)
    wine_repository.update(wine)
    return redirect('/wines')


# DELETE
# DELETE '/wines/<id>', [ Finalised ]

@wines_blueprint.route("/wines/<id>/delete", strict_slashes=False, methods=['POST'])
def delete_wine(id):
    wine_repository.delete(id)
    return redirect('/wines')


# FILTER
# FILTER '/wines/filter/<id>', draft..

@wines_blueprint.route('/wines/filter/<id>', strict_slashes=False, methods=['GET'])
def filter_products_by_producer(filter):
    filter = filter
    wines = wine_repository.select_all()
    return render_template("/wines/filter.html", all_wines = wines, filter = filter)

