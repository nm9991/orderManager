import sqlite3

kapcsolat = sqlite3.connect("DB/orders.db")
ab = kapcsolat.cursor()
ab.execute("CREATE TABLE IF NOT EXISTS orders (orderID INTEGER PRIMARY KEY, name TEXT, address TEXT, product TEXT, amount INTEGER)")

ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
           (10001, "Rodney Schwartz", "78705 Austin, Texas, 2323 San Antonio St", "Vase", "1"))
kapcsolat.commit()

ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
           (10002, "Shirley Lin", "76901 San Angelo, Texas, 2503 Sherwood Way", "Pillow", "3"))
kapcsolat.commit()

ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
           (10003, "Ewan Gibbs", "48104 Ann Arbor, Michigan, 318 S Main St", "Sofa", "1"))
kapcsolat.commit()

ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
           (10004, "Leslie Page", "30087 Stone Mountain, Georgia, 567 Stephenson Rd", "Table", "2"))
kapcsolat.commit()

ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
           (10005, "Linda Riley", "32084 St Augustine, Florida, 35 Hypolita St", "Chair", "8"))
kapcsolat.commit()


ab.close()
kapcsolat.close()