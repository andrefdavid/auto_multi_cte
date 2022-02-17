from re import U
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import BTN_BUSCAR, BTN_GERAR_PLANILHA, BTN_LOGIN, LINK_WRG_SP, PASSWORD, PASSWORD_FIELD, URL_ACESSO, URL_RELATORIOS, USERNAME, USERNAME_FIELD
from selenium.webdriver.chrome.options import Options
import os
from sys import platform
import argparse

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

    while "crdownload" in lista[-1] or "tmp" in lista[-1] or "google" in lista[-1]:
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


def login_automatizado(driver, url_login=URL_ACESSO, usuario=USERNAME, senha=PASSWORD):
    driver.get(url_login)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(usuario)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(senha)
    driver.find_element(By.XPATH,BTN_LOGIN).click()


def filtra_pesquisa(driver, chave):
    elementos = driver.find_elements(By.CLASS_NAME, "input")
    i = 0
    
    for elemento in elementos:
        
        try:
            elemento.send_keys(chave)
            break
        except selenium.common.exceptions.ElementNotInteractableException:
            #print(f"O elemento {i} não é o correto!")
            print("Processando...")
        finally:
            i = i + 1
    botoes = driver.find_elements(By.CLASS_NAME, "btn.btn-default.btn-primary.btnPesquisarFiltroPesquisa")
    for botao in botoes:
        try:
            botao.click()
            break
        except selenium.common.exceptions.ElementNotInteractableException:
            #print("Botão não clicável")
            print("processando")



def geracao_relatorio(driver, espera=3, relatorio="WRG-SP", url_relatorio=URL_RELATORIOS):
    #abre a página de relatórios
    driver.get(url_relatorio)
    time.sleep(espera) #espera para continuar
    lista_botoes_buscar = driver.find_elements(By.CLASS_NAME,BTN_BUSCAR)
    lista_botoes_buscar[0].click()
    time.sleep(espera) #espera 3 segundos
    filtra_pesquisa(driver, relatorio)
    time.sleep(espera) #espera 3 segundos
    #clicando no link para gerar o relatório
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/a").click()
    

def download_planilha(driver):
    lista_botoes_download = driver.find_elements(By.CLASS_NAME, BTN_GERAR_PLANILHA)
    lista_botoes_download[1].click()

def acesso_automatizado(espera=3, quantidade_inicial=0, relatorio="WRG-SP", usuario=USERNAME, senha=PASSWORD, login_url=URL_ACESSO, relatorio_url=URL_RELATORIOS):
    driver = inicicaliza_driver()
    login_automatizado(driver, url_login=login_url, usuario=usuario, senha=senha)
    time.sleep(espera)
    geracao_relatorio(driver, espera, relatorio, url_relatorio=relatorio_url)
    time.sleep(espera)
    download_planilha(driver)
    checar_download(quantidade_inicial)





parser = argparse.ArgumentParser(description="Extrai automaticamente os relatórios do sistema")
parser.add_argument("--relatorio", metavar="-r", type=str, help="O filtro do relatório que se deseja obter. Ex: WRG-SP", default="WRG-SP")
parser.add_argument("--usuario", metavar="-u", type=str, help="O usuário utilizado no login", default=USERNAME)
parser.add_argument("--senha", metavar="-s", type=str, help="A senha utilizada no login", default=PASSWORD)
parser.add_argument("--loginurl", metavar="-l", type=str, help="A URL da página de login", default=URL_ACESSO)
parser.add_argument("--relatoriourl", metavar="-e", type=str, help="A URL da página de relatórios", default=URL_RELATORIOS)


parser.add_argument("--espera", metavar="-e", type=int, help="O tempo que o sistema deve esperar após cada ação automatizada (o padrão é de 3 segundos)", default=3)

args = parser.parse_args()
print(args)

quantidade_inicial = len(lista_downloads())
acesso_automatizado(espera=args.espera, quantidade_inicial=quantidade_inicial, relatorio=args.relatorio, usuario=args.usuario, senha=args.senha, login_url=args.loginurl, relatorio_url=args.relatoriourl)
print("O programa será encerrado!")
    

