import pyautogui
import time
import pandas

#aqui é importado a tabela de excel usando o pandas 
table = pandas.read_csv('produtos.csv')
print(table)

#a função PAUSE fara com que haja um inetervalo em segundos entre cada comando 
pyautogui.PAUSE = 0.5


#Função que abre o navegador
def openBrowser():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press("enter")
    
    #Aqui é acessado o link doCAHA000252     site
    page = "http://127.0.0.1:5500/webpage/index.html"
    time.sleep(3)
    pyautogui.write(page)
    pyautogui.press("enter")

def insertData():
    #neste trecho será preenchido cada campo do formulário com
    # cada item da planilha 
    for line in table.index:
        pyautogui.click(x=520, y=238)
        
        #código
        code = table.loc[line, "codigo"]
        pyautogui.write(code)
        pyautogui.press('tab')

        #marca
        brand = table.loc[line, "marca"]
        pyautogui.write(brand)
        pyautogui.press('tab')
        
        #tipo
        type = table.loc[line, "tipo"]
        pyautogui.write(type)
        pyautogui.press('tab')
        
        #categoria
        category = str(table.loc[line, "categoria"])
        pyautogui.write(category)
        pyautogui.press('tab')
        
        #preco
        price = str(table.loc[line, "preco_unitario"])
        pyautogui.write(price)
        pyautogui.press('tab')
        
        #custo
        cost = str(table.loc[line, "custo"])
        pyautogui.write(cost)
        pyautogui.press('tab')
        
        
        #obs
        obs = table.loc[line, 'obs']
        if not pandas.isna(obs):
            pyautogui.write(obs)
            
        #enviar produto
        pyautogui.press('tab')
        pyautogui.press('enter')

        #limpar form
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        pyautogui.scroll(5000)
        
        if code and brand and type and category and price and cost and obs == " " :
            print("Tarefa finalizada")
        
def iniciate():
    openBrowser()
    time.sleep(2)
    insertData()
    
iniciate()