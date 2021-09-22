# Geocoder
Geocoders utilizando API Bing via biblioteca GeoPy. Esse código foi escrito de acordo com as necessidades no setor em que trabalhei mas as vantagens se estenderam muito além. Se tornou uma ferramenta que facilitou os diversos trabalhos e várias situações. Por exemplo: postes sem endereço nos atributos da viatoria assim impossibilitando o licenciamento, localizações não exatas havendo somente informações de endereço, necessidade de informações de endereço mas só havia coordenadas, etc.

## GEOCODER.py 

Possui uma interface para o usuário interagir construído utilizando TKinter. Possui duas opções Endereço --> Coordenada e Coordenada --> Endereço.

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
![print_geocoder](https://github.com/sergiusfelipe/Imagens/blob/main/Anota%C3%A7%C3%A3o%202021-09-22%20150739.png)

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
O endereço será pegue da coluna 'endercom'.

```python
location = geolocator.geocode(df2.loc[i,'endercom'])
```
As coordenadas serão pegues das colunas 'LATITUDE' e 'LONGITUDE'.

```python
coord = [df1.loc[i,'LATITUDE'],df1.loc[i,'LONGITUDE']]
```

## GEOCODER_SIMPLIFICADO.py

Não conta com a interface e a seleção é feita via caminho do arquivo.

```python
base = pds.read_excel(r'CAMINHO DO EXCEL.xlsx')
```

O endereço pode estar dividido em campos separados.

```python
logradouro = str(df2.loc[i,'logradouro']) + " " + str(df2.loc[i,'Numero']) + " - " + str(df2.loc[i,'bairro']) + ", Fortaleza, CE"
cidade = str('Fortaleza')
estado = str('Ceara')
cep = str(df2.loc[i,'CepEnderecoPadrao'])
            
l = dict(addressLine = str(logradouro),locality = str(cidade),adminDistrict = str(estado))
```

A configuração de geocoder ou reverse deve ser feita no código. 

```python
coordenadas = getCoor(base_1)
```
ou
```python
endereco = getEnde(base_1)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

