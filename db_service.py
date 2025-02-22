
import mysql.connector

def get_db_connection():
  mydb = mysql.connector.connect(
  host="Prachi003.mysql.pythonanywhere-services.com",
  user="Prachi003",
  password="*******",
  database="Prachi003$devbits"
  )
  return mydb

def sign_up_user(user_name,password,email_id):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    insert_query = " INSERT INTO user(user_name,password,email_id) VALUES(%s,%s,%s)"
    try:

        cur.execute(insert_query, (user_name,password, email_id))
        db_connection.commit()
    except:
        return {'status': False, 'error': "Failed to insert"}
    result="sign up done"
    return result

sign_up_user('prachi','1233','abc@gmail.com')
def login(user_name,password):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    query = "SELECT user_id FROM user WHERE user_name=%s and password=%s"
    cur.execute(query,(user_name, password))
    row = cur.fetchall()

    return row

def add_to_watchlist(user_id,stock_id):
     db_connection = get_db_connection()
     cur = db_connection.cursor()
     insert_query = " INSERT INTO watchlist(user_id,stock_id) VALUES(%s,%s)"
     try:

        cur.execute(insert_query, (user_id,stock_id))
        db_connection.commit()
     except:
        return {'status': False, 'error': "Failed to insert"}
     result="watchlist updated"
     return result

def buy(user_id,stock_id,entry_price,quantity,time):
     db_connection = get_db_connection()
     cur = db_connection.cursor()
     insert_query = " INSERT INTO buys(user_id,stock_id,entry_price,quantity,time) VALUES(%s,%s,%s,%s,%s)"
     try:

        cur.execute(insert_query, (user_id,stock_id,entry_price,quantity,time))
        db_connection.commit()
        select_query = 'SELECT balance FROM user WHERE user_id=%s'
        cur.execute(select_query,(user_id,))
        count = cur.fetchall()

        balance  = count[0][0]-entry_price*quantity
        print(balance)
        select_query = 'SELECT holdings FROM user WHERE user_id=%s'
        cur.execute(select_query,(user_id,))
        count2 = cur.fetchall()

        holdings = count2[0][0]+entry_price*quantity
        print(holdings)

        update_query = "UPDATE `Prachi003$devbits`.`user` SET `balance` =%s, `holdings` = %s WHERE (`user_id` = %s);"
        cur.execute(update_query,(balance,holdings, user_id))
        db_connection.commit()
     except:
        return {'status': False, 'error': "Failed to insert"}
     result="added"
     return result

def sell(user_id,stock_id,exit_price,quantity,time):
     db_connection = get_db_connection()
     cur = db_connection.cursor()
     insert_query = " INSERT INTO sell(user_id,stock_id,exit_price,quantity,time) VALUES(%s,%s,%s,%s,%s)"
     try:

        cur.execute(insert_query, (user_id,stock_id,exit_price,quantity,time))
        db_connection.commit()
        select_query = 'SELECT balance FROM user WHERE user_id=%s'
        cur.execute(select_query,(user_id,))
        count = cur.fetchall()

        balance  = count[0][0]+exit_price*quantity
        print(balance)
        select_query = 'SELECT holdings FROM user WHERE user_id=%s'
        cur.execute(select_query,(user_id,))
        count2 = cur.fetchall()

        holdings = count2[0][0]-exit_price*quantity
        print(holdings)

        update_query = "UPDATE `Prachi003$devbits`.`user` SET `balance` =%s, `holdings` = %s WHERE (`user_id` = %s);"
        cur.execute(update_query,(balance,holdings, user_id))
        db_connection.commit()
     except:
        return {'status': False, 'error': "Failed to insert"}
     result="added"
     return result

def get_user_info(user_id):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    query="Select balance,holdings from user WHERE user_id=%s"
    cur.execute(query,(user_id,))
    rows=cur.fetchall()
    print (rows)
    print(rows[0][0])

    return {

        'info': {
            'balance': rows[0][0],
            'holdings': rows[0][1]

        }
    }

def get_user_buys(user_id):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    query="Select * from buys WHERE user_id=%s"
    cur.execute(query,(user_id,))
    rows=cur.fetchall()
    print (rows)


    result = []
    for row in rows:

        entry = {
            'stock_id': row[2],
            'quantity':row[3],
            'time':row[4],
            'entry_price':row[5]

            }

        result.append(entry)


    return result

def get_user_sale(user_id):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    query="Select stock_id from sell WHERE user_id=%s"
    cur.execute(query,(user_id,))
    rows=cur.fetchall()
    print (rows)


    result = []
    for row in rows:

        entry = {
            'stock_id': row[0],


            }

        result.append(entry)


    return result

def get_user_watchlist(user_id):
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    query="Select stock_id from watchlist WHERE user_id=%s"
    cur.execute(query,(user_id,))
    rows=cur.fetchall()
    print (rows)


    result = []
    for row in rows:

        entry = {
            'stock_id': row[0],


            }

        result.append(entry)


    return result
