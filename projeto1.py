import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, min_letters=1, min_digits=1, min_symbols=1):
    # Definição da função para gerar senha
    if length < (min_letters + min_digits + min_symbols):
        raise ValueError("O tamanho total deve ser maior ou igual à soma mínima de letras, dígitos e símbolos.")

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Adiciona os caracteres mínimos obrigatórios
    password.extend(random.choices(string.ascii_letters, k=min_letters))
    password.extend(random.choices(string.digits, k=min_digits))
    password.extend(random.choices(string.punctuation, k=min_symbols))

    # Adiciona caracteres aleatórios até atingir o comprimento desejado
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(all_chars, k=remaining_length))

    # Embaralha os caracteres para garantir aleatoriedade
    random.shuffle(password)
    return ''.join(password)

def display_password():
    try:
        # Obtém o comprimento da senha e as preferências de tipo de caractere dos campos de entrada
        length = int(length_entry.get())
        min_letters = int(min_letters_entry.get() or 1)
        min_digits = int(min_digits_entry.get() or 1)
        min_symbols = int(min_symbols_entry.get() or 1)

        # Gera e exibe a senha
        password = generate_password(length, min_letters, min_digits, min_symbols)
        password_label.config(text=f"Senha aleatória: {password}")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Cria rótulos e campos de entrada para a entrada do usuário
length_label = tk.Label(root, text="Tamanho da senha:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

min_letters_label = tk.Label(root, text="Letras mínimas:")
min_letters_label.grid(row=1, column=0, padx=5, pady=5)

min_letters_entry = tk.Entry(root)
min_letters_entry.grid(row=1, column=1, padx=5, pady=5)

min_digits_label = tk.Label(root, text="Dígitos mínimos:")
min_digits_label.grid(row=2, column=0, padx=5, pady=5)

min_digits_entry = tk.Entry(root)
min_digits_entry.grid(row=2, column=1, padx=5, pady=5)

min_symbols_label = tk.Label(root, text="Símbolos mínimos:")
min_symbols_label.grid(row=3, column=0, padx=5, pady=5)

min_symbols_entry = tk.Entry(root)
min_symbols_entry.grid(row=3, column=1, padx=5, pady=5)

# Cria um botão para gerar a senha
generate_button = tk.Button(root, text="Gerar Senha", command=display_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Cria um rótulo para exibir a senha gerada
password_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
password_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Executa o loop principal do evento para exibir a GUI
root.mainloop()
