import os
import utils
import shutil
import zipfile
import pyautogui
from time import sleep
from pathlib import Path
from pyperclip import paste, copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement


pyautogui.FAILSAFE = True


def automacao(periodo):
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    driver.get("https://webedi.nexxera.io/login")
    driver.maximize_window()

    _ = driver.find_element(By.ID, "mailbox").send_keys("EQSENG.EQSENG")
    _ = driver.find_element(By.ID, "password").send_keys("eqseng22")
    _ = driver.find_element(By.ID, "submit").click()

    aux = 0
    while True:
        try:
            _ = driver.find_element(By.XPATH, "/html/body/div[4]/div/button").click()
            break
        except:
            sleep(1)
            aux+=1
            if aux == 10:
                break

    while True:
        try:
            elemento_select = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/skyline-table-pagination/table/thead/tr/th/select")
            select = Select(elemento_select)
            select.select_by_index(7)
            break
        except:
            sleep(1)


    data1 = periodo.split(" até ")[0].strip()
    data2 = periodo.split(" até ")[1].strip()


    while True:
        _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").clear()
        _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").send_keys(periodo)

        sleep(1.5)
        _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/button").click()

        sleep(1.5)
        data_no_portal = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").get_attribute("value")
        data_no_portal = str(data_no_portal)[:10]

        if data_no_portal in [data1, data2]:
            break

    sleep(5)
    if driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").is_selected():
        _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").click()
        if driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
            while driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
                sleep(1)

    _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").click()
    while not driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
        sleep(1)


    sleep(5)
    _ = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[3]/div/div/button[1]").click()

    sleep(6)

    pyautogui.hotkey("ctrl", "j")

    sleep(2)
    pyautogui.press(["tab"]*4)
    pyautogui.press("enter", interval=3)
    pyautogui.press("f2", interval=0.5)
    pyautogui.hotkey('ctrl', 'c', interval=0.5)
        
    nome_do_arquivo = paste() + ".zip"
    pasta_downloads = Path.home() / "Downloads"
    caminho_completo = pasta_downloads / nome_do_arquivo


    pasta_destino = "C:\\Nexxera"

    try:
        os.mkdir(pasta_destino)
    except FileExistsError:
        shutil.rmtree(pasta_destino)
        os.mkdir(pasta_destino)
    except PermissionError:
        pass


    with zipfile.ZipFile(caminho_completo, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

    os.remove(caminho_completo)

    pyautogui.press("esc", interval=0.5)
    pyautogui.hotkey("ctrl", "w", interval=0.6)

    driver.quit()

    arquivos = [arquivo for arquivo in os.listdir(pasta_destino) if not arquivo.endswith(".protocolo") and arquivo[:3] == "PAG"]

    if arquivos:

        utils.clicarMicrosiga()

        for arq in arquivos:

            def lancar_CNAB(arq):
                banco, dados_banco = utils.retornar_objeto_banco(arq)

                sleep(1)
                pyautogui.hotkey("alt", "o", interval=0.2)
                pyautogui.press("n", interval=0.2)
                pyautogui.press("down", interval=0.2)
                pyautogui.press("enter", interval=0.2)

                while True:
                    esperar = utils.encontrarImagem(r'Imagens\esperarAparecer.png')
                    if type(esperar) == tuple:
                        break

                pyautogui.press("enter", interval=0.2)

                while True:
                    esperar = utils.encontrarImagem(r'Imagens\perguntas.png')
                    if type(esperar) == tuple:
                        break

                x, y = esperar
                pyautogui.click(x, y)

                sleep(1)

                pyautogui.press(["tab"]*3)

                caminho_absoluto = pasta_destino + "\\" + arq

                utils.colar_dado_no_campo(str(caminho_absoluto))

                utils.colar_dado_no_campo(dados_banco["arquivo de config"])

                utils.colar_dado_no_campo(banco)

                utils.colar_dado_no_campo(dados_banco["agencia"])

                utils.colar_dado_no_campo(dados_banco["conta"])

                utils.colar_dado_no_campo(dados_banco["subconta"])

                pyautogui.press("space", interval=0.2)
                pyautogui.press("up", interval=0.2)
                pyautogui.press("enter", interval=0.2)

                clicar = utils.encontrarImagem(r'Imagens\informacoes.png')
                x, y = clicar

                pyautogui.click(x, y)
                sleep(0.3)
                pyautogui.press(["tab"]*2, interval=0.2)
                pyautogui.press("enter", interval=1.2)

                while True:
                    esperar = utils.encontrarImagem(r'Imagens\aguarde.png')
                    if type(esperar) != tuple:
                        ignorar = utils.encontrarImagem(r'Imagens\ignorar.png')
                        ignorar2 = utils.encontrarImagem(r'Imagens\ignorar2.png')
                        ignorar3 = utils.encontrarImagem(r'Imagens\ignorar3.png')
                        erro_datab = utils.encontrarImagem(r'Imagens\erroDataBase.png')
                        if type(erro_datab) == tuple:
                            pyautogui.press("enter", interval=1)
                            pyautogui.press("esc", interval=1)
                            func_cta_pag = utils.encontrarImagem(r'Imagens\funcoesCtasPag.png')
                            x,y = func_cta_pag
                            pyautogui.doubleClick(x, y)
                            while True:
                                clicar = utils.encontrarImagem(r'Imagens\botaoConfirmar.png')
                                x, y = clicar
                                pyautogui.click(x, y)
                                clicar = utils.encontrarImagem(r'Imagens\botaoConfirmar.png')
                                if type(clicar) != tuple:
                                    break
                            while True:
                                ignorar4 = utils.encontrarImagem(r'Imagens\ignorar4.png')
                                if type(ignorar4) == tuple:
                                    pyautogui.press(["tab"]*2, interval=0.2)
                                    pyautogui.press("enter", interval=0.2)
                                    break
                            while True:
                                abriu = utils.encontrarImagem(r'Imagens\abriu.png')
                                if type(abriu) == tuple:
                                    return lancar_CNAB(arq)
                        if type(ignorar2) == tuple or type(ignorar3) == tuple:
                            pyautogui.press("enter", interval=0.2)
                            esperar = utils.encontrarImagem(r'Imagens\aguarde.png')
                        if type(ignorar) == tuple:
                            pyautogui.press("enter", interval=0.2)
                            while True:
                                negar = utils.encontrarImagem(r'Imagens\nao.png')
                                if type(negar) == tuple:
                                    pyautogui.press("right", interval=0.3)
                                    pyautogui.press("enter", interval=0.3)
                                    break
                        if type(esperar) != tuple:
                            break

            lancar_CNAB(arq)

            sleep(1)

            
