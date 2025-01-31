import pyautogui
from time import sleep
from pyperclip import paste, copy


def encontrarImagem(imagem):
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


def clicarMicrosiga(imagem=r'Imagens\microsiga.png'):
    try:
        elemento = encontrarImagem(imagem)
        x, y = elemento
        pyautogui.click(x, y)
    except:
        try:
            elemento = encontrarImagem(r'Imagens\microsiga2.png')
            x, y = elemento
            pyautogui.click(x, y)
        except:
            elemento = encontrarImagem(r'Imagens\microsigaWin11.png')
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

   
