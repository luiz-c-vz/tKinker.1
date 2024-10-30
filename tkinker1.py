from tkinter import Tk
import tkinker as tk
from tkinker import ttk
janela= tk.Tk()
var_promocoes = tk.Intvar()
checkbox_promocoes = tk.checkbutton(text= "Deseja receber e-mail promocionai?", variable_ = var_promocoes)
checkbox_promocoes.grid(row= 0, column=0)

janela.title("Coletação de Moedas")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text= "Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, heignt=5)
mensagem.grid(row=0, column= 0, columnspan=2, sticky="NSFW")

mensagem2 = tk.Label(text_="Selecione a moeda desejada")
mensagem2.grid(row=1, column= 0)

#moeda = tk.Entry()
#moeda.grid(row=1, column= 1)

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text_= "cotação não encontrada")
    mensagem_cotacao.grid(row = 3, column = 0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"cotação do {moeda_preenchida} é de {cotacao_moeda} reais  "

botao= tk.Button(text= "Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

dicionario_cotacoes = {
    'Dolar': 5.47,
    'Euro': 6.68,
    'Bitcoin':20000
}
moedas = list(dicionario_cotacoes.keys())
moeda = ttk.combobox(janela,values=moedas)
moeda.grid(row=1, column=1)

caixa_texto = tk.text(width= 10 , height= 5)
caixa_texto.grid(row=5, column=0, skicky='nswe')

def buscar_cotacoes():
    texto= caixa_texto.get("1.0", tk. END)
    lista_moedas= texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem4 = tk.Label(text= '\n'. join(mensagem_cotacoes))
    mensagem4.grid(row= 6, column=1)

botao_multiplascotacoes = tk.Button(text= "Buscar Cotações", command= buscar_cotacoes)
botao_multiplascotacoes.grid(row= 5, column=1)

def enviar():
    print(var_promocoes.get())

botao_enviar = tk.button(text= "Enviar", command = enviar)
botao-enviar.grid(row=1, column=0)

janela.mainloop()