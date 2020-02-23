CREATE TABLE IF NOT EXISTS cryptos (
    id integer PRIMARY KEY,
    symbol text,
    name text
);

CREATE TABLE IF NOT EXISTS movements (
    id integer PRIMARY KEY,
    date text,
    time text,
    from_currency integer,
    from_quantity real,
    to_currency integer,
    to_quantity real,
    CONSTRAINT fk_from_currency FOREIGN KEY (from_currency) REFERENCES cryptos(id)
    CONSTRAINT fk_to_currency FOREIGN KEY (to_currency) REFERENCES cryptos(id)   
);
