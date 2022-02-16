PROJETO PARA AUTOMATIZAÇÃO DE ACESSO E DOWNLOAD DA PLANILHA AO SISTEMA

OS DADOS DE ACESSO DEVEM SER CONFIGURADOS NO ARQUIVO CONFIG.PY
#ACESSO AO SISTEMA
URL_ACESSO = "" #link de acesso da página de login
USERNAME = "" #PREENCHER O NOME DE USUÁRIO DE ACESSO AO SISTEMA
PASSWORD = "" #PREENCHER O NOME DE USUÁRIO DE ACESSO AO SISTEMA

#PAGINA RELATÓRIOS 
URL_RELATORIOS = "" #link após clicar no botão de relatórios

É necessário fazer a instalação do Selenium (pip install selenium) e do webdriver_manager(pip install webdriver_manager)
----------------
Funcionamento: esta solução acessa a página de login do sistema e insere os dados de acesso, gerando um clique automático no botão de login.
Após isso, a ferramenta acessa a página de relatórios diretamente e, de forma automática, clica nos botões de Buscar -> no Link do Relatório -> Gerar Relatório em formato XLS

Todos os botões e links são identificados através dos atributos das TAGs HTML existentes no momento da criação do código. Caso a página seja alterada, a solução também precisará ser revista


----------------
A solução foi proposta para um uso e cenário específico e deve ser utilizada apenas para fins de estudo.
O autor não se responsabiliza por qualquer dano causado durante a utilização desta solução ou soluções derivadas.