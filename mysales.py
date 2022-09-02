import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "carenting")
imlec = db.cursor()

def Db_Sales_Insert(customer_id,car_id,number_of_day,finishing_day,total_price,plug_id):
    komut = "INSERT INTO sales (customer_id,car_id,number_of_day,finishing_day,total_price,plug_id) VALUES (%s,%s,%s,%s,%s,%s)"
    komut_parameters = (customer_id,car_id,number_of_day,finishing_day,total_price,plug_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("SATIŞ KAYDI BAŞARIYLA EKLENDİ...")

def Db_Sales_Finishind_Day():
    komut = "select car_id from sales WHERE finishing_day = CURRENT_DATE"
    imlec.execute(komut)
    liste = imlec.fetchall()
    return liste

def Db_Sales_List():
    komut = "SELECT * FROM mysales()"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("SATIŞ TARİHİ   : ",deger[0])
        print("MÜŞTERİ NO     : ",deger[1])
        print("MÜŞTERİ ADI    : ",deger[2])
        print("ARAÇ NO        : ",deger[3])
        print("ARAÇ PLAKASI   : ",deger[4])
        print("GÜN SAYISI     : ",deger[5])
        print("BAŞLANGIÇ GÜNÜ : ",deger[6])
        print("BİTİŞ GÜNÜ     : ",deger[7])
        print("TOPLAM TUTAR   : ",deger[8])
        print("FİŞ NO         : ",deger[9])
       
        print("")
    
    