import re
import main
from time import sleep
from pathlib import Path
from tkinter import Tk, Canvas, Entry, messagebox, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Imagens")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def validar_data(data):
    padrao = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

    if re.match(padrao, data):
        return True
    else:
        return False


def verificar_data():
    data = entry_1.get()
    data2 = entry_2.get()
    if validar_data(data) and validar_data(data2):
        return f"{data} até {data2}"


def acionar_automacao():
    data = verificar_data()
    if data:
        sleep(0.5)
        window.iconify()
        sleep(1)
        main.automacao(data)
        messagebox.showinfo("Sucesso!", "Todos os pagamentos foram inseridos no microsiga.")
    else:
        messagebox.showerror("Erro", "Data inválida! Use o formato dd/mm/aaaa.")



window = Tk()

window.geometry("494x217")
window.configure(bg = "#222222")
window.title("Arquivos Nexxera")
window.iconbitmap(relative_to_assets("robozinho.ico"))

vcmd = (window.register(validar_data), '%P')

canvas = Canvas(
    window,
    bg = "#222222",
    height = 217,
    width = 494,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    247.0,
    108.0,
    image=image_image_1
)

entry_bg_1 = canvas.create_image(
    123.5,
    91.5,
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    relief="groove",
    justify="center",
    highlightbackground="#000000",
    validate='focusout', 
    validatecommand=vcmd,
    font=("Inter", 16 * -1),
    highlightthickness=0
)
entry_1.place(
    x=33.0,
    y=78.0,
    width=181.0,
    height=25.0
)

entry_bg_2 = canvas.create_image(
    371.5,
    91.5,
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    relief="groove",
    justify="center",
    validate='focusout', 
    validatecommand=vcmd,
    highlightbackground="#000000",
    font=("Inter", 16 * -1),
    highlightthickness=0
)
entry_2.place(
    x=281.0,
    y=78.0,
    width=181.0,
    height=25.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: acionar_automacao(),
    relief="flat",
    cursor="hand2"
)
button_1.place(
    x=134.0,
    y=138.0,
    width=225.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()
