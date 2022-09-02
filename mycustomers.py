import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "carenting")
imlec = db.cursor()

def Db_Customers_Select():
    komut = "select * from customers"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","ADI:",deger[1]," | ","ADRES:",deger[2]," | ","TELEFON: ",deger[3]," | ","EMAİL: ",deger[4],"TİPİ: ",deger[5])


def Db_Customers_Insert(customer_name,customer_address,customer_number,customer_email,customer_status):
    komut = "INSERT INTO customers (customer_name,customer_address,customer_number,customer_email,customer_status) VALUES (%s,%s,%s,%s,%s)"
    komut_parameters = (customer_name,customer_address,customer_number,customer_email,customer_status)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("MÜŞTERİ BAŞARIYLA EKLENDİ...")

def Db_Customers_Update(customer_name,customer_address,customer_number,customer_email,customer_status,customer_id):
     komut = "Update customers SET customer_name = %s,customer_address=%s,customer_number=%s,customer_email=%s,customer_status=%s WHERE customer_id = %s"
     komut_parameters = (customer_name,customer_address,customer_number,customer_email,customer_status,customer_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("MÜŞTERİ BAŞARIYLA GÜNCELLENDİ...")


def Db_Customer_Search_With_ID(customer_id):
    komut = "SELECT customer_name,customer_address,customer_number,customer_email,customer_status FROM customers Where customer_id = %s"
    komut_parameters = [customer_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Customers_Delete(customer_id):
    komut = "DELETE FROM customers WHERE customer_id = %s"
    komut_parameters = str(customer_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("MÜŞTERİ BAŞARIYLA SİLİNDİ...")