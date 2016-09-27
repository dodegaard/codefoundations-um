import sqlalchemy

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('postgres', 'qq1122qq', 'northwind')

results = meta.tables['orders']

# To show the columns available from the Orders table in Northwind simply uncomment and run to the dashed line

#print(results.c)

#for col in results.c:
#    print(col)

#----------------------------------------------------

# To query the entire Orders table in Northwind simply uncomment the next few lines to the dashed line

#for row in con.execute(results.select()):
#    print(row)

#----------------------------------------------------

# This next use case is for a simple clause on the results object which in this case is Orders table from Northwind
# Uncomment next four lines  to illustrate and run it.

#clause = results.select().where(results.c.orderdate > '1997-06-01')
#
#for row in con.execute(clause):
#    print(row)







