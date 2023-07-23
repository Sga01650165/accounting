from time import sleep
def get_information():
    gataat = int(input('many of gataat:'))
    tedade_neroy_kar = int(input('tedade neroy kar:'))
    hazene_neroy_kar = int(input('hazene neroy kar:')) 
    tahgig_tosee_test = int(input('hazene tahgig tosee test:'))
    tedade_khodro = int(input('tedade khodro:'))
    logestic = int(input('hazene logestic:'))
    tabligat = int(input('hazene tabligat:'))
    maliyat = int(input('hazene maliyat:'))
    zayeat = int(input('hazene zayeat:'))
    sod = float(input('darsade sod:'))
    calculate(gataat, tedade_neroy_kar, hazene_neroy_kar, tahgig_tosee_test, tedade_khodro, logestic, tabligat, maliyat, zayeat, sod)

def calculate(gataat, tedade_neroy_kar,  hazene_neroy_kar, tahgig_tosee_test, tedade_khodro,  logestic, tabligat,  maliyat,  zayeat, sod):
    temp = gataat + (hazene_neroy_kar * tedade_neroy_kar) + tahgig_tosee_test + (logestic * tedade_khodro) + (tabligat * tedade_khodro) + maliyat + zayeat
    total = (temp * sod / 100) + temp
    print(f'temp : {temp:,} total : {total:,.2f}')  
    sleep(3)
get_information()