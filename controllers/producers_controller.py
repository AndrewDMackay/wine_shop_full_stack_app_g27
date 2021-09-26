import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import author_repository
from repositories import book_repository

from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)


# Index..
# GET '/books/', finalised..

@books_blueprint.route("/books", strict_slashes=False, methods=['GET'])
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


# NEW
# GET '/books/new'
# Returns an HTML form to the browser, finalised..

@books_blueprint.route("/books/new", strict_slashes=False, methods=['GET'])
def new_books():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)


# CREATE
# POST '/books/'
# Receives the data from the form to insert into the database, finalised..

@books_blueprint.route("/books", strict_slashes=False, methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/books')


# # SHOW
# # GET '/books/<id>', finalised..

@books_blueprint.route("/books/<id>", strict_slashes=False, methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)


# EDIT
# GET '/books/<id>/edit'

@books_blueprint.route("/books/<id>/edit", strict_slashes=False, methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)


# UPDATE
# PUT '/books/<id>'

@books_blueprint.route("/books/<id>", strict_slashes=False, methods=['POST'])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author, id)
    book_repository.update(book)
    return redirect('/books')


# DELETE
# DELETE '/books/<id>', finalised..

@books_blueprint.route("/books/<id>/delete", strict_slashes=False, methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')