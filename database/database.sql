CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_user TEXT NOT NULL,
    surname TEXT NOT NULL,
    user_name TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    pass_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_prod TEX NOT NULL,
    buyer INTEGER NOT NULL,
    seller INTEGER NOT NULL,
    price INTEGER NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,

    FOREIGN KEY (buyer) REFERENCES users (id),
    FOREIGN KEY (seller) REFERENCES users (id)
);
CREATE TABLE IF NOT EXISTS product (
    prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
    img BLOB, /* An url to the photo(s) */
    title TEXT NOT NULL,
    belong_to INTEGER NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    about TEXT NOT NULL, /* It needs to be a pre formateded description */
    uploaded TEXT,

    FOREIGN KEY (belong_to) REFERENCES users (id)
);
CREATE TABLE IF NOT EXISTS sellers (
    seller_id INTEGER NOT NULL,
    product INTEGER DEFAULT 0, /* There will be not such id product in the table product */

    FOREIGN KEY (seller_id) REFERENCES users (id),
    FOREIGN KEY (product) REFERENCES product (prod_id)
);