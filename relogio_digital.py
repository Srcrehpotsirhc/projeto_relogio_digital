import tkinter as tk

import datetime

class TelaPrincipal:
    def __init__(self, mestre):
        self.nossaTela = mestre
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Arial', 26), fg='Black')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        agora = datetime.datetime.now()

        self.lblRelogio['text'] = agora.strftime('%H:%M:%S')

        self.nossaTela.after(1000, self.alteracao)


janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()
