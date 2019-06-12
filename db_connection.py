import psycopg2 as pg2

con = pg2.connect(dbname = 'userdb',user = 'postgres', password = '',
                  host = 'localhost', port = '5432')

cur = con.cursor()

with open('<filepath>','r') as fp:
    reader = fp.read()

    for row in reader:
        cur.execute('<sql query>',row)

con.commit()

