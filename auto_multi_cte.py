from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import BTN_BUSCAR, BTN_GERAR_PLANILHA, BTN_LOGIN, LINK_WRG_SP, PASSWORD, PASSWORD_FIELD, URL_ACESSO, URL_RELATORIOS, USERNAME, USERNAME_FIELD
from selenium.webdriver.chrome.options import Options
import os
from sys import platform

#Autor: André David


def lista_downloads():
      
    if platform == "darwin" or platform == "linux" or platform == "linux2":
        path = f"{os.path.dirname(__file__)}/relatorio"
    else:
        path = f"{os.path.dirname(__file__)}\\relatorio"
    
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    return files

def checar_download(quantidade_inicial):
    print("Aguardando o download da planilha. Não feche o navegador.")

    lista = lista_downloads()
    while len(lista) == quantidade_inicial:
        time.sleep(0.3)
        lista = lista_downloads()

    while "crdownload" in lista[-1]:
        time.sleep(0.3)
        lista = lista_downloads()

    print("Download concluído com sucesso!")

def opcoes_navegador(debug=False):
    chrome_options = Options()
    if debug:
        chrome_options.add_experimental_option("detach", True)
    
    if platform == "darwin" or platform == "linux" or platform == "linux2":
        caminho_download = f"{os.path.dirname(__file__)}/relatorio"
    else:
        caminho_download = f"{os.path.dirname(__file__)}\\relatorio"

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": caminho_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
        })
    #chrome_options.add_argument(f"download.default_directory={caminho_download}")

    return chrome_options


def inicicaliza_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service, chrome_options=opcoes_navegador())


def login_automatizado(driver):
    driver.get(URL_ACESSO)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH,BTN_LOGIN).click()

def geracao_relatorio(driver, espera=3):
    #abre a página de relatórios
    driver.get(URL_RELATORIOS)
    time.sleep(espera) #espera para continuar
    lista_botoes_buscar = driver.find_elements(By.CLASS_NAME,BTN_BUSCAR)
    lista_botoes_buscar[0].click()
    time.sleep(espera) #espera 3 segundos
    #clicando no link para gerar o relatório
    driver.find_element(By.XPATH,LINK_WRG_SP).click()

def download_planilha(driver):
    lista_botoes_download = driver.find_elements(By.CLASS_NAME, BTN_GERAR_PLANILHA)
    lista_botoes_download[1].click()

def acesso_automatizado(espera=3, quantidade_inicial=0):
    driver = inicicaliza_driver()
    login_automatizado(driver)
    time.sleep(espera)
    geracao_relatorio(driver, espera)
    time.sleep(espera)
    download_planilha(driver)
    checar_download(quantidade_inicial)

quantidade_inicial = len(lista_downloads())
acesso_automatizado(quantidade_inicial=quantidade_inicial)
print("O programa será encerrado!")
    

    

