# Autor: Lucas Inácio
# Consulta de CNPJ

# Importar biblioteca visual
import customtkinter as ctk

# Importar  biblioteca de requisições
import requests

# Aparência da janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

window_cnpj = ctk.CTk()
window_cnpj.title('Consulta CNPJ')
window_cnpj.geometry('800x600')

# Função Consulta CNPJ
def consulta_cnpj():
    cnpj = entry_cnpj.get().strip()
    if not cnpj:
        resultado.configure('CNPJ Inválido')
        return


    try:
        url = f'https://api.opencnpj.org/{cnpj}'
        res = requests.get(url)
        dados = res.json()

        informacao = (
            f'cnpj: {dados["cnpj"]}\n'
            f'Razão Social: {dados["razao_social"]}\n'
            f'Situação cadastral: {dados["situacao_cadastral"]}\n'
        )
        resultado.configure(text=informacao)
    except:
        resultado.configure('Erro ao consultar CNPJ')

# Título da janela
titulo = ctk.CTkLabel(window_cnpj,
                      text='Consulta de CNPJ',
                      font=('Arial', 22),
                      text_color='#C80028')
titulo.pack(pady=10)

# Entrada de dados
entry_cnpj = ctk.CTkEntry(window_cnpj,
                          placeholder_text='Digite seu CNPJ',
                          width=400,
                          height=40,
                          corner_radius=12)
entry_cnpj.pack(pady=20)

# Botão
consultar = ctk.CTkButton(window_cnpj,
                          text='Consultar',
                          width=400,
                          height=40,
                          fg_color='#0000FF',
                          hover_color="#383898",
                          command=consulta_cnpj)
consultar.pack(pady=20)

# Resultado
resultado = ctk.CTkLabel(window_cnpj,
                      text='Resultado',
                      font=('Arial', 22),
                      text_color='#0DE201')
resultado.pack(pady=10)

window_cnpj.mainloop()