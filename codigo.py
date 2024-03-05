# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# biblioteca pyautogui - permite automatizar qualquer tarefa teclado,mouse e tela do pc. Automatizar rotina

import pyautogui #pacote automacao
import time  # pacote de espera


pyautogui.PAUSE = 0.7
#pyautogui.click (clica)
#pyautogui.write (palavra inteira)
#pyautogui.press (presiona uma tecla)

# 1_ entrar no sistema da empresa
    #abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
time.sleep(2)
pyautogui.write(link)

pyautogui.press("enter")

# dar uma pause em um local especifico: biblioteca time
time.sleep(3)


# 2_ Fazer Login 
#clicks click(x=1523, y=312, click = 2) diz quantos click vai dar 
#buton click(x=1523, y=312, button = "left") qual botão do mouse vai clicar
pyautogui.click(x=2468, y=402)
pyautogui.write("UmEmail@gmail.com")

# Quando e formulario para passar de um campo para outro e so apertar Tab
pyautogui.press("tab")
pyautogui.write("Senha123")
pyautogui.click(x=2666, y=561)
time.sleep(3)

# 3_ Importar a base de dados
import pandas #importar a base de dados
tabela = pandas.read_csv("produtos.csv")


# 4_ cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:
    pyautogui.click(x=2417, y=274)
    # Codigo do produto
    # codigo = tabela.loc[1,"marca"] se quiser pergar alguma coisa e so colocar linha / coluna tipo: linha 1, da marca[1,"marca"]
    #                    linha, coluna
    # pega o codigo do produto e coloca na linha

    pyautogui.write(str( tabela.loc[linha,"codigo"]) )
    pyautogui.press("tab")

    # Codigo do Marca
    pyautogui.write(tabela.loc[linha,"marca"] )
    pyautogui.press("tab")


    # Codigo do Tipo

    pyautogui.write(tabela.loc[linha,"tipo"] )
    pyautogui.press("tab")

    # Codigo do categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"] ))
    pyautogui.press("tab")

    # Codigo do preco
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]) )
    pyautogui.press("tab")

    # Codigo do custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    # Codigo do obs

    # aqui tem uma observação que não existe, temos que tratar
    obs = tabela.loc[linha,"obs"]
    #isna significa vazio
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    #voltar ao inicio da tela positivo pra cima negativo pra baixo
    pyautogui.scroll(5000)

# 5_ repetir ate acabar a base de dadostps://dlp.hashtagtreinamentos.com/python/intensivao/login
