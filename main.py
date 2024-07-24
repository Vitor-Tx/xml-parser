from bs4 import BeautifulSoup
from glob import glob
from pathlib import Path
import pandas as pd


path = str(Path())
pathList = glob(path + "/notas/*.xml")
soupList = []
for path in pathList:
    file = open(path, "r")
    soupList.append(BeautifulSoup(file.read(), 'lxml-xml'))
    file.close()


dic_list = []
for soup in soupList:
    items = soup.find_all("det")
    chave = soup.find("infNFe").get("Id")
    for item in items:
        dic = {
        "Tipo": "",
        "Comprovante": "",
        "Nome do Componente": "", 
        "Chave Nfe": "", 
        "Código do Item na Nfe": "", 
        "Quantidade": ""}
    
        dic["Tipo"] = ("Subcomponente")
        dic["Comprovante"] = ("Nfe")
        dic["Nome do Componente"] = (item.find("xProd").get_text())
        dic["Chave Nfe"] = (chave[3:])
        dic["Código do Item na Nfe"] = (item.find("cProd").get_text())
        dic["Quantidade"] = (item.find("qCom").get_text())
        dic_list.append(dic)
    

df = pd.DataFrame(dic_list)
df.to_excel("notas.xlsx")

