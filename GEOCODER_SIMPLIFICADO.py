import pandas as pds
from geopy.geocoders import Bing
import time


def getCoor(df2):

    geolocator = Bing(api_key = 'API KEY')
    linhas = len(df2.index)
    lat = []
    lon = []
    
    for i in range(0,linhas):
    
        logradouro = str(df2.loc[i,'logradouro']) + " " + str(df2.loc[i,'Numero']) + " - " + str(df2.loc[i,'bairro']) + ", Fortaleza, CE"
        cidade = str('Fortaleza')
        estado = str('Ceara')
        cep = str(df2.loc[i,'CepEnderecoPadrao'])
            
        l = dict(addressLine = str(logradouro),locality = str(cidade),adminDistrict = str(estado))
        print(l)
        location = geolocator.geocode(l)
        print('CALCULANDO DISTANCIAS: ',i*100/linhas,'%. ')
        lat.append(location.latitude)
        lon.append(location.longitude)
        time.sleep(0.5)
    
    
    df2['LAT2'] = lat
    df2['LON2'] = lon
    
    return df2
	
    
def getEnde(df1):
    
    geo = Bing(api_key = 'API KEY')
    lista = []
    uf = []
    cidade = []
    logradouro = []
    
    for i in range(0,len(df1['LATITUDE'])):
        coord = [df1.loc[i,'LATITUDE'],df1.loc[i,'LONGITUDE']]
        consulta = geo.reverse(coord, timeout=2).address
        print("Endereco " + str(i+1) + ": " + consulta)
        lista.append(consulta)
        sep = consulta.split(",")
        sep_1 = sep[-2].split(" ")
        
        uf.append(sep[-2])
        try:
            cidade.append(sep[-3])
        except:
            cidade.append("Nao identificado")
        logradouro.append(sep[0])
        
        time.sleep(0.5)
        
        

    df1['ender'] = lista
    #df1["LOGRADOURO"] = logradouro
    #df1["CIDADE"] = cidade
    #df1["UF"] = uf
    
    
    
    return df1
    
if __name__ == "__main__":

    base = pds.read_excel(r'CAMINHO DO EXCEL.xlsx')
    base_1 = pds.DataFrame(base)
    print('BASE OK')

    coordenadas = getCoor(base_1)
    print("FASE 1 OK")
    #coordenadas.to_excel("COORDENADAS.xlsx")


    coordenadas.to_excel("RESULTADO_ENDEREÇO.xlsx")
    print("CONCLUIDO")