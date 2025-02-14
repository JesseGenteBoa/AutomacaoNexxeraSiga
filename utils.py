import pyautogui
from time import sleep
from pyperclip import paste, copy
 

pyautogui.FAILSAFE = True
 
def encontrar_referencia(imagem):
    cont = 0
    while True:
        try:
            x, y, a, b = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.89)    
            return (x, y)
        except:
            sleep(0.8)
            cont += 1
            if cont == 2:
                break
            print("Imagem não encontrada")
            pass
 
 
def encontrar_imagem(imagem):
    cont = 0
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(imagem, grayscale=True, confidence=0.91)    
            return (x, y)
        except:
            sleep(0.8)
            cont += 1
            if cont == 2:
                break
            print("Imagem não encontrada")
            pass
 
 
def clicar_microsiga(imagem=r'Imagens\microsiga.png'):
    try:
        elemento = encontrar_imagem(imagem)
        x, y = elemento
        pyautogui.click(x, y)
    except:
        try:
            elemento = encontrar_imagem(r'Imagens\microsiga2.png')
            x, y = elemento
            pyautogui.click(x, y)
        except:
            elemento = encontrar_imagem(r'Imagens\microsigaWin11.png')
            x, y = elemento
            pyautogui.click(x, y)
 
 
def retornar_objeto_banco(arquivo):
    banco = arquivo.split("_")[1]
    if banco == "396881":
        banco = "104"
    bancos = {
        "341": {
            "arquivo de config":"itaupag.2pr",
            "agencia": "6243",
            "conta": "15755",
            "subconta": "0"
            },
        "001": {
            "arquivo de config":"bbpg.2pr",
            "agencia": "3013",
            "conta": "3506150",
            "subconta": "0"
            },
        "237": {
            "arquivo de config":"bradesco.2pr",
            "agencia": "1472",
            "conta": "80900",
            "subconta": "001"
            },
        "033": {
            "arquivo de config":"stdpag.2pr",
            "agencia": "1512",
            "conta": "13001503",
            "subconta": "0"
            },
        "104": {
            "arquivo de config":"caixapg.2pr",
            "agencia": "04270",
            "conta": "0300000012",
            "subconta": "0"
            },
    }
    return banco, bancos[banco]
 
 
def colar_dado_no_campo(dado):
    copy(dado)
    sleep(0.2)
    pyautogui.hotkey("ctrl", "v", interval=0.3)
    if dado in ["001", "04270", "341", "104", "237", "033", "bradesco.2pr", "0300000012"]:
        pass
    else:
        pyautogui.press("tab")
 
 
def reabrir_rotina_siga(data_formatada):
    pyautogui.press("esc", interval=1)
    func_cta_pag = encontrar_imagem(r'Imagens\funcoesCtasPag.png')
    x,y = func_cta_pag
    pyautogui.doubleClick(x, y)
    while True:
        clicar = encontrar_imagem(r'Imagens\botaoConfirmar.png')
        if type(clicar) == tuple:
            pyautogui.write(data_formatada, interval=0.2)
            pyautogui.press("tab", interval=0.2)
            x, y = clicar
            pyautogui.click(x, y)
            clicar2 = encontrar_imagem(r'Imagens\botaoConfirmar.png')
            while type(clicar2) == tuple:
                clicar2 = encontrar_imagem(r'Imagens\botaoConfirmar.png')
                x, y = clicar2
                pyautogui.click(x, y)
            break
    while True:
        ignorar4 = encontrar_imagem(r'Imagens\ignorar4.png')
        if type(ignorar4) == tuple:
            pyautogui.press(["tab"]*2, interval=0.2)
            pyautogui.press("enter", interval=0.2)
            break
    while True:
        abriu = encontrar_imagem(r'Imagens\abriu.png')
        if type(abriu) == tuple:
            return True
