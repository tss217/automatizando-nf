#ts217

import pyautogui
from time import sleep
import pandas as pd
import argparse

def clcik(x,y):
    sleep(3)
    pyautogui.click(x,y)

def getValue(value):
    sleep(1)
    pyautogui.write(str(value))
    sleep(1)
    pyautogui.press("enter")

def getOut():
    sleep(10)
    pyautogui.hotkey("ctrl", "r")
    sleep(10)
    pyautogui.keyDown("esc")
    sleep(1)
    pyautogui.keyUp("esc")
    

def loadColumns(table, *columns):
    df = pd.read_excel(table)
    return {col:df[col] for col in columns}

def comparator(orderTotal,partnerTotal):
    return f"{min(float(orderTotal), float(partnerTotal)):.2f}"


   # if orderTotal > partnerTotal:
    #    return partnerTotal

   # return orderTotal

def start():

    print("""

    =========================================================


    _   _ ______            _____ _____  _____  __   ______
    | \ | ||  ___|          |_   _/  ___|/ __  \/  | |___  /
    |  \| || |_     ______    | | \ `--. `' / /'`| |    / / 
    | . ` ||  _|   |______|   | |  `--. \  / /   | |   / /  
    | |\  || |                | | /\__/ /./ /____| |_./ /   
    \_| \_/\_|                \_/ \____/ \_____/\___/\_/   


    =========================================================
    CRIADO POR THIAGO SANTOS
    =========================================================

    """)

    while True:

        choice = input("deseja fazer nota somente do menor?(y/n)").lower()
        if choice in ("y","n"):
            return choice

def contador():
    for x in range(15):
        sleep(1)
        print(f"iniciando em ...........................{x}")

def total(choice, orderTotal, partnerTotal):
    return comparator(orderTotal, partnerTotal) if choice == "y" else orderTotal


parse =   argparse.ArgumentParser(description="Exemplo de flags no terminal")
parse.add_argument("-e",type=str,help="tabela")
args = parse.parse_args()

choiceFromstart= start()
contador()

data = loadColumns(args.e,"ID CURTO DO PEDIDO","VALOR DOS ITENS (R$)","TOTAL PAGO PELO CLIENTE (R$)")
sleep(10)

#order, orderTotal, partnerTotal in zip(data["N° PEDIDO"],data["TOTAL DO PEDIDO"],data["TOTAL DO PARCEIRO"]):

for order, orderTotal, partnerTotal in zip( data["ID CURTO DO PEDIDO"], data["VALOR DOS ITENS (R$)"],data["TOTAL PAGO PELO CLIENTE (R$)"]):
    

    print(f"pedido: {order}............. total do pedido: R${orderTotal}, total do parceiro: R${partnerTotal}")
    clcik(245,231)
    getValue(total(choiceFromstart,orderTotal,partnerTotal))
    clcik(627,577)
    clcik(849,905)
    getOut()
    clcik(629,891)

