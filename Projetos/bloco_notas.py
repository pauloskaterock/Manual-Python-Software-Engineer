import subprocess
import pyautogui
import time

# Abrir o Bloco de Notas usando subprocess
subprocess.Popen(["notepad.exe"])
time.sleep(1)  # Espera 1 segundo para o Bloco de Notas abrir

# Simular a digitação usando pyautogui
texto = "Olá, Bloco de Notas!"
pyautogui.typewrite(texto)

# Opcional: salvar o arquivo
# pyautogui.hotkey('ctrl', 's')
# pyautogui.typewrite('nome_do_arquivo.txt')
# pyautogui.press('enter')

# Aguardar alguns segundos antes de fechar o Bloco de Notas
time.sleep(2)

# Fechar o Bloco de Notas
pyautogui.hotkey('alt', 'f4')
