
DROP TABLE IF EXISTS wines;
DROP TABLE IF EXISTS producers;

CREATE TABLE producers (
  id SERIAL PRIMARY KEY,
  producer_name VARCHAR(255),
  country VARCHAR(255),
  region VARCHAR(255),
  winemaker VARCHAR(255),
  active BOOLEAN
);

CREATE TABLE wines (
  id SERIAL PRIMARY KEY,
  wine_name VARCHAR(255),
  stock INT,
  net_price FLOAT,
  sell_price FLOAT,
  producer_id INT REFERENCES producers(id)
);

