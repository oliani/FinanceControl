import sqlite3
conn = sqlite3.connect('maindb.db')

c = conn.cursor()

c.execute('''CREATE TABLE cashier (
    id integer NOT NULL CONSTRAINT cashier_pk PRIMARY KEY AUTOINCREMENT,
    total double NOT NULL,
    name varchar(255) NOT NULL
);''')

c.execute('''
CREATE TABLE item (
    id integer NOT NULL CONSTRAINT item_pk PRIMARY KEY AUTOINCREMENT,
    price double NOT NULL,
    product_id varchar(20) NOT NULL,
    CONSTRAINT item_product FOREIGN KEY (product_id)
    REFERENCES product (id)
);''')

c.execute('''
CREATE TABLE operation (
    id integer NOT NULL CONSTRAINT operation_pk PRIMARY KEY,
    value double NOT NULL,
    obs varchar(255) NOT NULL,
    cashier_id integer NOT NULL,
    CONSTRAINT operation_cashier FOREIGN KEY (cashier_id)
    REFERENCES cashier (id)
);''')

c.execute('''
CREATE TABLE "order" (
    id int NOT NULL CONSTRAINT order_pk PRIMARY KEY,
    obs varchar(255) NOT NULL,
    total double NOT NULL,
    date varchar(11) NOT NULL,
    item_id integer,
    finalizado boolean DEFAULT true,
    CONSTRAINT order_item FOREIGN KEY (item_id)
    REFERENCES item (id)
);''')

c.execute('''
CREATE TABLE product (
    id varchar(20) NOT NULL CONSTRAINT product_pk PRIMARY KEY,
    name varchar(255),
    cost double NOT NULL
);''')

c.execute('''
CREATE TABLE stock (
    quant int NOT NULL,
    obs varchar(255) NOT NULL,
    id integer NOT NULL CONSTRAINT stock_pk PRIMARY KEY AUTOINCREMENT,
    product_id varchar(20) NOT NULL,
    CONSTRAINT stock_product FOREIGN KEY (product_id)
    REFERENCES product (id)
);''')

conn.commit()

conn.close

print("DB criado com sucesso!")
