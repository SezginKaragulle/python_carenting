import psycopg2

db = psycopg2.connect(user = "postgres",
                      password = "1234",
                      host = "localhost",
                      port = "5432",
                      database = "carenting")
imlec = db.cursor()


def Db_Users_Select():
    komut = "SELECT user_id,user_name,staff_name,staff_surname,department FROM users ORDER BY user_id ASC"
    imlec.execute(komut)
    liste = imlec.fetchall()
    for deger in liste:
        print("ID:",deger[0]," | ","KULLANICI ADI:",deger[1]," | ","ADI:",deger[2]," | ","SOYADI: ",deger[3],"DEPARTMAN: ",deger[4])

def Db_Users_Select_Login(user_name,user_password):
    komut = "SELECT * FROM users Where user_name = %s and user_password = %s"
    komut_parameters = [user_name,user_password]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_Users_Insert(user_name,user_password,staff_name,staff_surname,department):
    komut = "INSERT INTO users (user_name,user_password,staff_name,staff_surname,department) VALUES (%s,%s,%s,%s,%s)"
    komut_parameters = (user_name,user_password,staff_name,staff_surname,department)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("KULLANICI BAŞARIYLA EKLENDİ...")

def Db_Users_Search(user_name):
    komut = "SELECT * FROM users Where user_name = %s"
    komut_parameters = [user_name]
    imlec.execute(komut,komut_parameters)
    liste = imlec.fetchall()
    return liste

def Db_User_Change_Password(user_password,user_id):
     komut = "Update users SET user_password = %s WHERE user_id = %s"
     komut_parameters = (user_password,user_id)
     imlec.execute(komut,komut_parameters)
     db.commit()
     print("ŞİFRE GÜNCELLENDİ...")

def Db_User_Delete(user_id):
    komut = "DELETE FROM users WHERE user_id = %s"
    komut_parameters = str(user_id)
    imlec.execute(komut,komut_parameters)
    db.commit()
    print("KULLANICI BAŞARIYLA SİLİNDİ...")