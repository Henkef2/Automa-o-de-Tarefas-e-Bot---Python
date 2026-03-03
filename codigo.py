# labs = code packets

# Step by step for your program

import pyautogui     #biblioteca que permite que utilize teclado, mouse e toque na tela
import time
import pandas

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

pyautogui.PAUSE = 0.5  # comando para pausar por tempo determinado cada ação para evitar problema na execução
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # variável

# Step 1: Enter to business system
pyautogui.press("win")  
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# do the litle pause to website open
time.sleep(3)

# Step 2: Make Login
# click email camp
pyautogui.click(x=692, y=370) #posição x y encontrada utilizando codigo auxiliar.py, foi dado 5 segundos para selecionar o local onde quero selecionar com o mouse e printa e executa
pyautogui.write("todoidao@gmail.com")
pyautogui.press("tab") #pass to next fiel "password"
pyautogui.write("senhadoidona")
pyautogui.press("tab") #pass to next fiel "button" - logar
pyautogui.press("enter")


# Step 3: Open the database
# instalar as bibliotecas no terminal (pip install pandas) (pip install pandas openpyxl), pandas = trabalha com base de dados, openpyxl = trabalha com excel


tabela = pandas.read_csv("produtos.csv") #criei uma variável que contem a tabela produtos.csv
print(tabela)

for linha in tabela.index:   #para cada linha da tabela faça:. obs2: index = indice ou seja, cada linha, se quiser que começe por coluna não coloca index coloca columns
    # Step 4: Register 1 product
    # codigo
    pyautogui.click(x=687, y=249) #clica no campo do codigo
    codigo = str(tabela.loc[linha, "codigo"]) # localiza algo dentro de uma tabela, nesse caso estou procurando dentro da [linha a coluna "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"]) #obs, foi colocado = str( ) para converter o resultado em uma string, senao iria ficar somente texto e ia dar erro ao digitar numero 

    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":  #se a observação for diferente (!=) de "nan" (nan = nada, vazio), então faça, caso se for nan irá pular para prox linha
        pyautogui.write(obs)
    pyautogui.press("tab") #passar para o botão enviar

    pyautogui.press("enter") #cadastrou um produto
    pyautogui.scroll(1000) #vai rolar a tela para cima (+) ou para baixo (-) a quantidade de pixels colocada, 1000 é um valor muito alto para subir para o inicio da tela   



# Step 5: Repeat the 4 step until over the product list