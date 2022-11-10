from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
browser = webdriver.Edge("D:/Setup/chromedriver_win32/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tag=ul_tag.find_all("li")
            temp_list=[]
            for indi,eti in enumerate(li_tag):
                if indi==0:
                    temp_list.append(eti.find_all("a")[0].contents[0])
                else :
                    try:
                        temp_list.append(eti.contents[0])
                    
                    except:temp_list.append("")

            planets_data.append(temp_list)


        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas
data_frame=pd.DataFrame(planets_data,columns=headers)

# Convertir a CSV
data_frame.to_csv("datos_exel.csv",index=True,index_label="id")
    


