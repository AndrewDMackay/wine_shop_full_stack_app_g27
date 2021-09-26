
from db.run_sql import run_sql

from models.producer import Producer
import repositories.wine_repository as wine_repository


def save(producer):
    sql = "INSERT INTO producers (producer_name, country, region, producer_description) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [producer.producer_name, producer.country, producer.region, producer.producer_description]
    results = run_sql(sql, values)
    id = results[0]['id']
    producer.id = id
    return producer


def delete_all():
    sql = "DELETE  FROM producers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM producers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    producers = []
    sql = "SELECT * FROM producers"
    results = run_sql(sql)

    for row in results:
        producer = producer(row['producer_name'], row['producer_name'], row['country'], row['region'], row['producer_description'], row['id'])
        producers.append(producer)
    return producers


def select(id):
    producer = None
    sql = "SELECT * FROM producers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        producer = producer(result['producer_name'], result['producer_name'], result['country'], result['region'], result['producer_description'], result['id'])
    return producer
    

def update(producer):
    sql = "UPDATE producers SET (producer_name, country, region, producer_description) = (%s, %s, %s, %s) WHERE id = %s"
    values = [producer.producer_name, producer.country, producer.region, producer.producer_description]
    run_sql(sql, values)
