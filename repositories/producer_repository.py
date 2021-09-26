from db.run_sql import run_sql

from models.author import Author
import repositories.author_repository as author_repository


def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['id'] )
    return author
    

def update(author):
    sql = "UPDATE authors SET (name) = (%s) WHERE id = %s"
    values = [author.name]
    run_sql(sql, values)
