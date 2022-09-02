import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "carenting")
imlec = db.cursor()

def Db_Cars_List():
    komut = "SELECT * FROM cars ORDER BY car_id ASC"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","PLAKA:",deger[1]," | ","MARKA:",deger[2]," | ","MODEL: ",deger[3],"YIL: ",deger[4],"RENK: ",deger[5],"VİTES: ",deger[6],"DURUM: ",deger[7])

def Db_Cars_Insert(car_plate,car_brand,car_model,car_year,car_color,car_gear,car_status):
    komut = "INSERT INTO cars (car_plate,car_brand,car_model,car_year,car_color,car_gear,car_status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    komut_parameters = (car_plate,car_brand,car_model,car_year,car_color,car_gear,car_status)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ARAÇ BAŞARIYLA EKLENDİ...")

def Db_Cars_Search_With_ID(car_id):
    komut = "SELECT car_plate,car_brand,car_model,car_year,car_color,car_gear FROM cars Where car_id = %s"
    komut_parameters = [car_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Car_Update(car_plate,car_brand,car_model,car_year,car_color,car_gear,car_id):
     komut = "Update cars SET car_plate = %s,car_brand=%s,car_model=%s,car_year=%s,car_color=%s,car_gear=%s WHERE car_id = %s"
     komut_parameters = (car_plate,car_brand,car_model,car_year,car_color,car_gear,car_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("ARAÇ BAŞARIYLA GÜNCELLENDİ...")

def Db_Cars_Search_Status_With_ID(car_id):
    komut = "SELECT car_status FROM cars Where car_id = %s"
    komut_parameters = [car_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste


def Db_Cars_Delete(car_id):
    komut = "DELETE FROM cars WHERE car_id = %s"
    komut_parameters = str(car_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ARAÇ BAŞARIYLA SİLİNDİ...")


def Db_Cars_Price_List():
    komut = "select cars.car_plate,cars.car_brand,cars.car_model,pricelist.price from pricelist inner join cars on cars.car_id = pricelist.car_id"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("PLAKA:",deger[0]," | ","MARKA:",deger[1]," | ","MODEL:",deger[2]," | ","FİYAT: ",deger[3])

def Db_Car_Price_Insert(car_id,price):
    komut = "INSERT INTO pricelist (car_id,price) VALUES (%s,%s)"
    komut_parameters = (car_id,price)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ARABA FİYATI BAŞARIYLA EKLENDİ...")

def Db_Car_Price_Update(price,car_id):
    komut = "UPDATE pricelist SET price=%s WHERE car_id = %s"
    komut_parameters = (price,car_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("ARABA FİYATI BAŞARIYLA EKLENDİ...")

def Db_Car_Price_Delete(car_id):
    komut = "DELETE FROM pricelist WHERE car_id = %s"
    komut_parameters = str(car_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print(car_id,"ID Lİ ARAÇ FİYATI BAŞARIYLA SİLİNDİ...")

def Db_Cars_Pricelist_Search_Status_With_ID(car_id):
    komut = "SELECT price FROM pricelist Where car_id = %s"
    komut_parameters = [car_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Car_Status_Update(car_status,car_id):
     komut = "Update cars SET car_status = %s WHERE car_id = %s"
     komut_parameters = (car_status,car_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     





