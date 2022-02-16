#ACESSO AO SISTEMA
URL_ACESSO = "" #link de acesso da página de login
USERNAME = "" #PREENCHER O NOME DE USUÁRIO DE ACESSO AO SISTEMA
PASSWORD = "" #PREENCHER O NOME DE USUÁRIO DE ACESSO AO SISTEMA

#TAGS USADAS PARA AUTOMAÇÃO
USERNAME_FIELD = "//*[@id=\"login-form\"]/fieldset/section[1]/label[2]/input"
PASSWORD_FIELD = "//*[@id=\"login-form\"]/fieldset/section[2]/label[2]/input"
BTN_LOGIN = "//*[@id=\"login-form\"]/footer/section/section[2]/button"

#MENUS
MENU_SUPERIOR = "//*[@id=\"left-panel\"]/nav"
MENU_RELATORIOS = "//*[@id=\"ulMenuSistema\"]/li[2]/a"
MENU_CTE_ES = "//*[@id=\"ulMenuSistema\"]/li[2]/ul/li[1]/a"

#PAGINA RELATÓRIOS 
URL_RELATORIOS = "" #link após clicar no botão de relatórios
BTN_BUSCAR = "btn.btn-default.btn-primary.botaoBusca"
BTN_GERAR_PLANILHA = "btn.btn-success.btnPesquisarFiltroPesquisa"
#DIV RELATÓRIOS
LINK_WRG_SP = "//*[@id=\"292\"]/td[3]/a"
