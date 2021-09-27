
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
def new_producers():
    producers = producer_repository.select_all()
    return render_template('producers/new.html', all_producers = producers)


# CREATE
# POST '/producers/'
# Receives the data from the form to insert into the database, finalised..

@producers_blueprint.route("/producers", strict_slashes=False, methods=['POST'])
def create_producer():
    producer_name = request.form['producer-name']
    country = request.form['country']
    region = request.form['region']
    producer_description = request.form['producer-description']
    producer = Producer(producer_name, country, region, producer_description)
    producer_repository.save(producer)
    return redirect('/producers')


# # SHOW
# # GET '/producers/<id>', finalised..

@producers_blueprint.route("/producers/<id>", strict_slashes=False, methods=['GET'])
def show_producer(id):
    producer = producer_repository.select(id)
    return render_template('producers/show.html', producer = producer)


# EDIT
# GET '/producers/<id>/edit', finalised..

@producers_blueprint.route("/producers/<id>/edit", strict_slashes=False, methods=['GET'])
def edit_producer(id):
    producer = producer_repository.select(id)
    producers = producer_repository.select_all()
    return render_template('producers/edit.html', producer = producer, all_producers = producers)


# UPDATE
# PUT '/producers/<id>'

@producers_blueprint.route("/producers/<id>", strict_slashes=False, methods=['POST'])
def update_producer(id):
    producer_name = request.form['producer-name']
    country = request.form['country']
    region = request.form['region']
    producer_description = request.form['producer-description']
    producer = Producer(producer_name, country, region, producer_description, id)
    producer_repository.update(producer)
    return redirect('/producers')


# DELETE
# DELETE '/producers/<id>', finalised..

@producers_blueprint.route("/producers/<id>/delete", strict_slashes=False, methods=['POST'])
def delete_producer(id):
    producer_repository.delete(id)
    return redirect('/producers')