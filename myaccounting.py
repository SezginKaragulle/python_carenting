import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "carenting")
imlec = db.cursor()


def Db_Accounting_List():
    komut = "SELECT * FROM accounting ORDER BY plug_id ASC"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID         : ",deger[0])
        print("FİŞ TARİHİ : ",deger[1])
        print("AÇIKLAMA   : ",deger[2])
        print("TUTAR      : ",deger[3])
        print("FİŞ TİPİ   : ",deger[4])
        print("GELİR/GİDER: ",deger[5])
        print("")

def Db_Accounting_Insert(explanation,total_price,plug_type,accounting_type):
    komut = "INSERT INTO accounting (explanation,total_price,plug_type,accounting_type) VALUES (%s,%s,%s,%s)"
    komut_parameters = (explanation,total_price,plug_type,accounting_type)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("FİŞ BAŞARIYLA EKLENDİ...")

def Db_Accounting_Delete(plug_id):
    komut = "DELETE FROM accounting WHERE plug_id = %s"
    komut_parameters = str(plug_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("FİŞ BAŞARIYLA SİLİNDİ...")

def Db_Accounting_Search_With_ID(plug_id):
    komut = "SELECT plug_type FROM accounting Where plug_id = %s"
    komut_parameters = [plug_id]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Accounting_Search_With_Accounting_Type(accounting_type):
    komut = "SELECT SUM(total_price) FROM accounting Where accounting_type = %s"
    komut_parameters = [accounting_type]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste


def Db_Accounting_Last_Record():
    komut = "SELECT plug_id FROM accounting WHERE plug_type = 'Satış' ORDER BY plug_id DESC LIMIT 1"
    imlec.execute(komut)
    liste = imlec.fetchall()
    return liste