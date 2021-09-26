
import re

from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import producer_repository
from repositories import wine_repository

from models.wine import Wine
from models.producer import Producer

wines_blueprint = Blueprint("wines", __name__)


# Index..
# GET '/wines/', finalised..

@wines_blueprint.route("/wines", strict_slashes=False, methods=['GET'])
def wines():
    wines = wine_repository.select_all()
    return render_template("wines/index.html", all_wines = wines)


# NEW
# GET '/wines/new'
# Returns an HTML form to the browser, finalised..

@wines_blueprint.route("/wines/new", strict_slashes=False, methods=['GET'])
def new_wines():
    producers = producer_repository.select_all()
    return render_template("wines/new.html", all_producers = producers)


# CREATE
# POST '/wines/'
# Receives the data from the form to insert into the database, finalised..

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
# # GET '/wines/<id>', finalised..

@wines_blueprint.route("/wines/<id>", strict_slashes=False, methods=['GET'])
def show_wine(id):
    wine = wine_repository.select(id)
    return render_template('wines/show.html', wine = wine)


# EDIT
# GET '/wines/<id>/edit', finalised..

@wines_blueprint.route("/wines/<id>/edit", strict_slashes=False, methods=['GET'])
def edit_wine(id):
    wine = wine_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('wines/edit.html', wine = wine, all_producers = producers)


# UPDATE
# PUT '/wines/<id>'

@wines_blueprint.route("/wines/<id>", strict_slashes=False, methods=['POST'])
def update_wine(id):
    wine_name = request.form['wine-name']
    producer_id = request.form['producer-id']
    producer = producer_repository.select(producer_id)
    stock = request.form['stock']
    net_price = request.form['net-price']
    sell_price = request.form['sell-price']
    wine = Wine(wine_name, producer, stock, net_price, sell_price)
    wine_repository.update(wine)
    return redirect('/wines')


# DELETE
# DELETE '/wines/<id>', finalised..

@wines_blueprint.route("/wines/<id>/delete", strict_slashes=False, methods=['POST'])
def delete_wine(id):
    wine_repository.delete(id)
    return redirect('/wines')