
from db.run_sql import run_sql

from models.wine import Wine
import repositories.producer_repository as producer_repository


def save(wine):
    sql = "INSERT INTO wines (wine_name, producer_id, stock, net_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [wine.wine_name, wine.producer.id, wine.stock, wine.net_price, wine.sell_price]
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
        wine = Wine(row['wine_name'], producer, row['stock'], row['net_price'], row['sell_price'], row['id'])
        wines.append(wine)
    return wines

    (wine_name, producer_id, stock, net_price, sell_price)


def select(id):
    wine = None
    sql = "SELECT * FROM wines WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        producer = producer_repository.select(result['producer_id'])
        wine = Wine(result['wine_name'], producer, result['stock'], result['net_price'], result['sell_price'], result['id'])
    return wine


def update(wine):
    sql = "UPDATE wines SET (wine_name, producer, producer_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [wine.wine_name, wine.producer.id, wine.stock, wine.net_price, wine.sell_price]
    run_sql(sql, values)











