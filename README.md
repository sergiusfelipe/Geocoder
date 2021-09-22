# Geocoder
Geocoders utilizando API Bing via biblioteca GeoPy

## GEOCODER.py 

Possui uma interface para o usuário interagir construído utilizando TKinter. Possui duas opções Endereço --> Coordenada e Coordenada --> Endereço. O endereço pode estar en um campo único.

```python
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'black')
    canvas1.pack()
    
    browseButton_Excel_1 = tk.Button(text='Coordenada para Endereco', command=getEnde, bg='white', fg='red', font=('helvetica', 12, 'bold'))
    browseButton_Excel_2 = tk.Button(text='Endereco para Coordenada', command=getCoor, bg='white', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_text(90,295,fill="white",text="Desenvolvido por Sergio Tavora")
    canvas1.create_window(150, 100, window=browseButton_Excel_1)
    canvas1.create_window(150, 200, window=browseButton_Excel_2)

    root.mainloop()
```

Necessário gerar uma chave na API Rest da Bing e inserir no campo designado. O mesmo vale para o GEOCODER_SIMPLIFICADO.py

```python
geolocator = Bing(api_key = 'API KEY')
```

Caso ocorra algum tipo de erro durante a consulta, a cada X consultas é um backup é feito.

```python
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
```


## GEOCODER_SIMPLIFICADO.py

Não conta com a interface e a seleção é feita via caminho do arquivo. O endereço pode estar dividido em campos separados. A configuração de geocoder ou reverse deve ser feita no código.

## License
[MIT](https://choosealicense.com/licenses/mit/)

