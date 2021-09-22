import tkinter as tk
from tkinter import filedialog
import pandas as pds
from geopy.geocoders import Bing
import time

#Funcao para converterendereco em coordenadas
def getCoor ():
    global df1
    
    import_file_path = filedialog.askopenfilename()
    df1 = pds.read_excel (import_file_path)
    
    geolocator = Bing(api_key = 'API KEY')
    df3 = pds.DataFrame()
    
    #O endereco precisa estar numa coluna endercom
    df2 = pds.DataFrame(df1, columns = ['endercom'])
    linhas = len(df2.index)
    lat = []
    lon = []
    j = 0
    for i in range(0,linhas):
        location = geolocator.geocode(df2[i:i+1])
        print((location.latitude, location.longitude))
        lat.append(location.latitude)
        lon.append(location.longitude)
        #A cada X consultas eh feita o backup
        if j == 1000:
            df3['LATITUDE'] = lat
            df3['LONGITUDE'] = lon
            nome = 'BKP.xlsx'
            try:
                df3.to_excel(nome)
            except:
                df3.to_csv(nome)
            df3.drop(df3.index, inplace=True)
            j = 0
        j += 1
    
    #As coordenadas sao armazenadas nas colunas LATITUDE e LONGITUDE
    df2['LATITUDE'] = lat
    df2['LONGITUDE'] = lon

    #A planilha com as novas colunas de coordenadas serao salvas no caminho abaixo
    df2.to_excel('resultado_coordenada.xlsx')
    
    print("CONCLUIDO")
    
#Funcao para converter coordenadas para endereco
def getEnde ():
    global df1
    
    import_file_path = filedialog.askopenfilename()
    df1 = pds.read_excel (import_file_path)
    
    geo = Bing(api_key = 'API KEY')
    df3 = pds.DataFrame()
    lista = []
    j = 0
    
    #As coordenadas precesam estar separadaas em colunas LATITUDE e LONGITUDE
    for i in range(0,len(df1['LATITUDE'])):
        coord = [df1.loc[i,'LATITUDE'],df1.loc[i,'LONGITUDE']]
        consulta = geo.reverse(coord, timeout=2).address
        print("Endereco " + str(i+1) + ": " + consulta)
        lista.append(consulta)
        #A cada X consultas eh feita o backup
        if j == 1000: 
            df3['endercom'] = lista
            nome = 'BKP.xlsx'
            try:
                df3.to_excel(nome)
            except:
                df3.to_csv(nome)
            df3.drop(df3.index, inplace=True)
            j = 0
        j += 1
        time.sleep(0.5)
        
    #Os enderecos sao armazenados na coluna endercom
    df1['endercom']=lista
    print(df1['endercom'])

    #A planilha com as novas colunas de coordenadas serao salvas no caminho abaixo
    df1.to_excel('resultado_endereco.xlsx')
    
    print("CONCLUIDO")
    
    
    
if __name__ == "__main__":
    
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'black')
    canvas1.pack()
    
    browseButton_Excel_1 = tk.Button(text='Coordenada para Endereco', command=getEnde, bg='white', fg='red', font=('helvetica', 12, 'bold'))
    browseButton_Excel_2 = tk.Button(text='Endereco para Coordenada', command=getCoor, bg='white', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 100, window=browseButton_Excel_1)
    canvas1.create_window(150, 200, window=browseButton_Excel_2)
    canvas1.create_text(90,295,fill="white",text="Desenvolvido por Sergio Tavora")

    root.mainloop()