from db.run_sql import run_sql

from models.wine import Wine
import repositories.producer_repository as producer_repository


def save(wine):
    sql = "INSERT INTO wines (title, producer_id) VALUES (%s, %s) RETURNING *"
    values = [wine.title, wine.producer.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    wine.id = id
    return wine


def delete_all():
    sql = "DELETE  FROM wines"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM wines WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    wines = []
    sql = "SELECT * FROM wines"
    results = run_sql(sql)

    for row in results:
        producer = producer_repository.select(row['producer_id'])
        wine = wine(row['title'], producer, row['id'])
        wines.append(wine)
    return wines


def select(id):
    wine = None
    sql = "SELECT * FROM wines WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        producer = producer_repository.select(result['producer_id'])
        wine = wine(result['title'], producer, result['id'])
    return wine


def update(wine):
    sql = "UPDATE wines SET (title, producer, producer_id) = (%s, %s, %s) WHERE id = %s"
    values = [wine.title, wine.producer.id, wine.id]
    run_sql(sql, values)











