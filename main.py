import myusers
import mycars
import mycustomers
import myaccounting
import mysales
import datetime


def my_login_to_system():
    print("SİSTEME GİRİŞ")
    print("")
    myUserName = input("Kullanıcı Adınızı Giriniz: ")
    myUserPassword = input("Şifrenizi Giriniz: ")
    myLoginValues = myusers.Db_Users_Select_Login(myUserName,myUserPassword)
    if myLoginValues:
        print("GİRİŞ GERÇEKLEŞTİRİLDİ")
        print("")
        My_Process_C()
    else:
        print("HATALI KULLANICI ADI VEYA ŞİFRE")
        


def My_Process_C(myLocalValue=0):
    print("")
    print("1 - KULLANICI LİSTELEME İŞLEMİ")
    print("2 - KULLANICI EKLEME İŞLEMİ")
    print("3 - KULLANICI ŞİFRE DEĞİŞTİRME İŞLEMİ")
    print("4 - KULLANICI SİLME İŞLEMİ")
    print("5 - ARAÇ LİSTELEME İŞLEMİ")
    print("6 - ARAÇ EKLEME İŞLEMİ")
    print("7 - ARAÇ GÜNCELLEME İŞLEMİ")
    print("8 - ARAÇ SİLME İŞLEMİ")
    print("9 - MÜŞTERİ LİSTELEME İŞLEMİ")
    print("10 - MÜŞTERİ EKLEME İŞLEMİ")
    print("11 - MÜŞTERİ GÜNCELLEME İŞLEMİ")
    print("12 - MÜŞTERİ SİLME İŞLEMİ")
    print("13 - ARAÇ KİRALAMA FİYAT LİSTESİ")
    print("14 - ARAÇ FİYATI EKLEME İŞLEMİ")
    print("15 - ARAÇ FİYATI GÜNCELLEME İŞLEMİ")
    print("16 - ARAÇ FİYATI SİLME İŞLEMİ")
    print("17 - MUHASEBE FİŞ LİSTESİ")
    print("18 - MUHASEBE FİŞ GİRİŞ İŞLEMİ")
    print("19 - MUHASEBE FİŞ SİLME İŞLEMİ")
    print("20 - MUHASEBE KAR-ZARAR DURUMU")
    print("21 - ARAÇ KİRALAMA İŞLEMİ")
    print("22 - ARAÇ DURUMU GÜNCELLEME")
    print("23 - SATIŞ LİSTESİ")
    print("")
    mySelectionProcess = int(myLocalValue)
    if mySelectionProcess==0:
        myChoose = input("YAPILACAK İŞLEM NUMARASINI GİRİNİZ: ")
        mySelectionProcess = int(myChoose)
    else:
        mySelectionProcess = myLocalValue

    if mySelectionProcess == 1:
        print("")
        print("KULLANICI LİSTELEME İŞLEMİ")
        print("")
        myusers.Db_Users_Select()
    elif mySelectionProcess == 2:
        print("KULLANICI EKLEME İŞLEMİ")
        print("")
        myUserName = input("KULLANICI ADI: ")
        myUserPassword = input("ŞİFRE: ")
        myStaffName = input("PERSONEL ADI: ")
        myStaffSurname = input("PERSONEL SOYADI: ")
        myDepartment = input("DEPARTMAN: ")

        mySearchUser = myusers.Db_Users_Search(myUserName)
        if mySearchUser:
            print("Böyle Bir Kullanıcı Mevcut Ekleyemezsiniz")
            My_Process_C(2)
        else:
            myusers.Db_Users_Insert(myUserName,myUserPassword,myStaffName,myStaffSurname,myDepartment)
    elif mySelectionProcess == 3:
        print("")
        print("KULLANICI ŞİFRE DEĞİŞTİRME İŞLEMİ")
        print("")
        myUserID = int(input("KULLANICI ID: "))
        myUserPassword = input("YENİ ŞİFREYİ GİR: ")
        myusers.Db_User_Change_Password(myUserPassword,myUserID)
    elif mySelectionProcess == 4:
        print("")
        print("KULLANICI SİLME İŞLEMİ")
        print("")
        myUserID = int(input("KULLANICI ID: "))
        myDeleteAnswer = input("KULLANICIYI SİLMEK İSTİYOR MUSUNUZ ?: ")
        if myDeleteAnswer == 'E':
            myusers.Db_User_Delete(myUserID)
        elif myDeleteAnswer == 'H':
            print("SİLME İŞLEMİ İPTAL EDİLDİ...")
    elif mySelectionProcess ==5:
        print("")
        print("ARAÇLARI LİSTELEME İŞLEMİ")
        print("")
        mycars.Db_Cars_List()
    elif mySelectionProcess ==6:
        print("")
        print("ARAÇ EKLEME İŞLEMİ")
        print("")
        myNewPlate = input("PLAKA: ")
        myNewBrand = input("MARKA: ")
        myNewModel = input("MODEL: ")
        myNewYear = int(input("YIL: "))
        myNewColor = input("RENK: ")
        myNewGear = input("VİTES: ")
        mycars.Db_Cars_Insert(myNewPlate,myNewBrand,myNewModel,myNewYear,myNewColor,myNewGear,'Açık')
        print("")
        mycars.Db_Cars_List()
    elif mySelectionProcess == 7:
        print("")
        print("ARAÇ GÜNCELLEME İŞLEMİ")
        print("")
        mySelectionCarForUpdate = int(input("ARAÇ ID: "))
        mySelectionCarInformation = mycars.Db_Cars_Search_With_ID(mySelectionCarForUpdate)
        for nexCarInformation in mySelectionCarInformation:
            myLastCarPlate = nexCarInformation[0]
            myLastCarBrand = nexCarInformation[1]
            myLastCarModel = nexCarInformation[2]
            myLastCarYear =  nexCarInformation[3]
            myLastCarColor = nexCarInformation[4]
            myLastCarGear = nexCarInformation[5]
        
        myNewCarPlate = input("YENİ PLAKAYI GİRİNİZ: ")
        myNewCarBrand = input("YENİ MARKAYI GİRİNİZ: ")
        myNewCarModel = input("YENİ MODELİ GİRİNİZ: ")
        myNewCarYear =  int(input("YENİ YIL GİRİNİZ: "))
        myNewCarColor = input("YENİ RENK GİRİNİZ: ")
        myNewCarGear = input("YENİ VİTES GİRİNİZ: ")

        if myNewCarPlate != "":
            myLastCarPlate = str(myNewCarPlate)
        if myNewCarBrand !="":
            myLastCarBrand = str(myNewCarBrand)
        if myNewCarModel !="":
            myLastCarModel = str(myNewCarModel)
        if myNewCarYear !=0:
            myLastCarYear = int(myNewCarYear)
        if myNewCarColor !="":
            myLastCarColor = str(myNewCarColor)
        if myNewCarGear !="":
            myLastCarGear = str(myNewCarGear)

        mycars.Db_Car_Update(myLastCarPlate,myLastCarBrand,myLastCarModel,myLastCarYear,myLastCarColor,myLastCarGear,mySelectionCarForUpdate)
        print("")
        mycars.Db_Cars_List()

    elif mySelectionProcess ==8:
        print("")
        print("ARAÇ SİLMEK İŞLEMİ")
        print("")  
        mySelectionCarID = int(input("ARAÇ ID: "))
        myCarStatusInformation = mycars.Db_Cars_Search_Status_With_ID(mySelectionCarID)
        for nextCarStatus in myCarStatusInformation:
            myLastCarStatus = nextCarStatus[0]
        
        if myLastCarStatus !="Açık":
            print("")
            print("ARACIN DURUMU AÇIK OLMADIĞINDAN SİLEMEZSİNİZ...")
            print("ARACIN SON DURUMU: ",myLastCarStatus)
            print("")
        else:
            mycars.Db_Car_Price_Delete(mySelectionCarID)
            mycars.Db_Cars_Delete(mySelectionCarID)
            print("")
            mycars.Db_Cars_List()
    
    elif mySelectionProcess == 9:
        print("")
        print("MÜŞTERİ LİSTELEME İŞLEMİ")
        print("")
        mycustomers.Db_Customers_Select()
    
    elif mySelectionProcess == 10:
        print("")
        print("MÜŞTERİ EKLEME İŞLEMİ")
        print("")
        myCustomerNewName = input("ÜNVANI GİRİNİZ: ")
        myCustomerNewAdress = input("ADRESİ GİRİNİZ: ")
        myCustomerNewNumber = input("TELEFON GİRİNİZ: ")
        myCustomerNewEmail = input("EMAİL GİRİNİZ: ")
        myCustomerNewStatus = input("TİP GİRİNİZ: ")
        mycustomers.Db_Customers_Insert(myCustomerNewName,myCustomerNewAdress,myCustomerNewNumber,myCustomerNewEmail,myCustomerNewStatus)
        print("")
        mycustomers.Db_Customers_Select()
    
    elif mySelectionProcess == 11:
        print("")
        print("MÜŞTERİ GÜNCELLEME İŞLEMİ")
        print("")
        mySelectionCustomerForUpdate = int(input("MÜŞTERİ ID: "))
        mySelectionCustomerInformation = mycustomers.Db_Customer_Search_With_ID(mySelectionCustomerForUpdate)
        for nexCustomerInformation in mySelectionCustomerInformation:
            myLastCustomerName = nexCustomerInformation[0]
            myLastCustomerAddress = nexCustomerInformation[1]
            myLastCustomerNumber = nexCustomerInformation[2]
            myLastCustomerEmail =  nexCustomerInformation[3]
            myLastCustomerStatus = nexCustomerInformation[4]
        
        myNewCustomerName = input("YENİ ÜNVAN GİRİNİZ: ")
        myNewCustomerAddress = input("YENİ ADRES GİRİNİZ: ")
        myNewCustomerNumber = input("YENİ NUMARA GİRİNİZ: ")
        myNewCustomerEmail =  input("YENİ MAİL GİRİNİZ: ")
        myNewCustomerStatus = input("YENİ TİPİ GİRİNİZ: ")

        if myNewCustomerName != "":
            myLastCustomerName = str(myNewCustomerName)
        if myNewCustomerAddress !="":
            myLastCustomerAddress = str(myNewCustomerAddress)
        if myNewCustomerNumber !="":
            myLastCustomerNumber = str(myNewCustomerNumber)
        if myNewCustomerEmail !="":
            myLastCustomerEmail = str(myNewCustomerEmail)
        if myNewCustomerStatus !="":
            myLastCustomerStatus = str(myNewCustomerStatus)
        
        mycustomers.Db_Customers_Update(myLastCustomerName,myLastCustomerAddress,myLastCustomerNumber,myLastCustomerEmail,myLastCustomerStatus,mySelectionCustomerForUpdate)
        print("")
        mycustomers.Db_Customers_Select()
    
    elif mySelectionProcess == 12:
        print("")
        print("MÜŞTERİ SİLME İŞLEMİ")
        print("")
        mySelectionCustomerID = int(input("MÜŞTERİ KODU: "))
        print("")
        mycustomers.Db_Customers_Delete(mySelectionCustomerID)
        print("")
        mycustomers.Db_Customers_Select()
    elif mySelectionProcess == 13:
        print("")
        print("ARAÇ KİRALAMA FİYAT LİSTESİ")
        print("")
        mycars.Db_Cars_Price_List()
    
    elif mySelectionProcess == 14:
        print("")
        print("ARAÇ FİYATI EKLEME İŞLEMİ")
        print("")
        myNewPriceCarID = int(input("ARAÇ ID: "))
        myNewCarPrice = int(input("FİYAT: "))
        mycars.Db_Car_Price_Insert(myNewPriceCarID,myNewCarPrice)
        print("")
        mycars.Db_Cars_Price_List()
    
    elif mySelectionProcess == 15:
        print("")
        print("ARAÇ FİYATI GÜNCELLEME İŞLEMİ")
        print("")
        myNewPriceCarID = int(input("ARAÇ ID: "))
        myNewCarPrice = int(input("FİYAT: "))
        mycars.Db_Car_Price_Update(myNewCarPrice,myNewPriceCarID)
        print("")
        mycars.Db_Cars_Price_List()
    
    elif mySelectionProcess == 16:
        print("")
        print("ARAÇ FİYATI SİLME İŞLEMİ")
        print("")
        myNewPriceCarID = int(input("ARAÇ ID: "))
        mycars.Db_Car_Price_Delete(myNewPriceCarID)
        print("")
        mycars.Db_Cars_Price_List()
    
    elif mySelectionProcess == 17:
        print("")
        print("MUHASEBE FİŞ LİSTESİ")
        print("")
        myaccounting.Db_Accounting_List()
    
    elif mySelectionProcess == 18:
        print("")
        print("MUHASEBE FİŞ GİRİŞ İŞLEMİ")
        print("")
        myPlugExplanation = input("AÇIKLAMA: ")
        myPlugTotalPrice =  int(input("TUTAR: "))
        myPlugType = input("FİŞ TİPİ: ")
        myAccountingType = input("GELİR/GİDER: ")
        myaccounting.Db_Accounting_Insert(myPlugExplanation,myPlugTotalPrice,myPlugType,myAccountingType)
        print("")
        myaccounting.Db_Accounting_List()
    
    elif mySelectionProcess == 19:
        print("")
        print("MUHASEBE FİŞ SİLME İŞLEMİ")
        print("")
        myPlugId = int(input("FİŞ NUMARASI: "))
        myPlugInformation = myaccounting.Db_Accounting_Search_With_ID(myPlugId)
        for myNextPlugInfo in myPlugInformation:
            myLastPlugType = myNextPlugInfo[0]
        
        if myLastPlugType == 'Satış':
            print("FİŞ SATIŞ ÜZERİNDEN OLUŞTUĞU İÇİN SİLEMEZSİNİZ")
            print("")
        else:
            myaccounting.Db_Accounting_Delete(myPlugId)
            print("")
            myaccounting.Db_Accounting_List()
    
    elif mySelectionProcess == 20:
        print("")
        print("MUHASEBE KAR-ZARAR DURUMU")
        print("")
        myProfitStatus = myaccounting.Db_Accounting_Search_With_Accounting_Type("Gelir")
        myCostStatus = myaccounting.Db_Accounting_Search_With_Accounting_Type("Gider")
        for myNextProfitStatus in myProfitStatus:
            myLastProfitStatus = int(myNextProfitStatus[0])
        for myNextCostStatus in myCostStatus:
            myLastCostStatus = int(myNextCostStatus[0])
        
        myTotalProfit = myLastProfitStatus - myLastCostStatus
        print("")
        print("TOPLAM GELİR TUTARI    : ",myLastProfitStatus)
        print("TOPLAM GİDER TUTARI    : ",myLastCostStatus)
        print("TOPLAM KAR-ZARAR TUTARI: ",myTotalProfit)
    
    elif mySelectionProcess == 21:
        print("")
        print("ARAÇ KİRALAMA İŞLEMİ")
        print("")
        mySalesCustomerID = int(input("MÜŞTERİ NUMARASI: "))
        mySalesCarID = int(input("ARAÇ ID: "))
        mySalesNumberOfDay = int(input("GÜN SAYISI: "))
        myPriceListInformation = mycars.Db_Cars_Pricelist_Search_Status_With_ID(mySalesCarID)
        for nextCarPrice in myPriceListInformation:
            myLastCarPrice = int(nextCarPrice[0])
        
        mySalesTotalPrice = myLastCarPrice * mySalesNumberOfDay
        today = datetime.date.today()
        mySalesFinishingDay = today + datetime.timedelta(days = mySalesNumberOfDay)

        myaccounting.Db_Accounting_Insert("Araç Kiralama",mySalesTotalPrice,"Satış","Gelir")
        myAccountingLastRecord = myaccounting.Db_Accounting_Last_Record()
        for nextAccountingLastRecord in myAccountingLastRecord:
            myLastRecord = int(nextAccountingLastRecord[0])
        
        mycars.Db_Car_Status_Update('Kirada',mySalesCarID)
        mysales.Db_Sales_Insert(mySalesCustomerID,mySalesCarID,mySalesNumberOfDay,mySalesFinishingDay,mySalesTotalPrice,myLastRecord)
        print("")
        mysales.Db_Sales_List()
    
    elif mySelectionProcess == 22:
        print("")
        print("ARAÇ DURUM GÜNCELLEME")
        print("")
        mySalesFinishingDayInfo = mysales.Db_Sales_Finishind_Day()
        for nextSalesFinishingDay in mySalesFinishingDayInfo:
            myCarIdRecord = int(nextSalesFinishingDay[0])
            mycars.Db_Car_Status_Update('Açık',myCarIdRecord)
        
        print("ARAÇ DURUM GÜNCELLEME İŞLEMİ TAMAMLANDI...")
    
    elif mySelectionProcess == 23:
        print("")
        print("SATIŞ LİSTELEME İŞLEMİ")
        print("")
        mysales.Db_Sales_List()

    

########################################
my_login_to_system()
    





