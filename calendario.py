import tkinter as tk
import calendar

def mostrar_calendario():
    ano = int(ano_entry.get())
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete("1.0", tk.END)
    for mes in range(1, 13):
        x = calendar.month(ano, mes)
        resultado_text.insert(tk.END, "\n" + "="*20 + f" MÊS {mes} " + "="*20 + "\n")
        resultado_text.insert(tk.END, x)
    resultado_text.config(state=tk.DISABLED)

# Cria janela principal
janela = tk.Tk()
janela.title("Calendário")
janela.configure (background='#000000')

# Rótulo e entrada para o ano
ano_label = tk.Label(janela, text="INSIRA O ANO:",bg='#00FF7F')
ano_label.pack()
ano_entry = tk.Entry(janela)
ano_entry.pack()

# Botão para mostrar os calendários
mostrar_button = tk.Button(janela, text="Mostrar Calendários", command=mostrar_calendario, bg='#00FF7F')
mostrar_button.pack()

# Área de texto para mostrar os calendários
resultado_text = tk.Text(janela, wrap=tk.WORD, state=tk.DISABLED, height=30, width=80,bg='#000000',fg='#FF0000')
resultado_text.pack()

janela.mainloop()
