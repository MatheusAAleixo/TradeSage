import os

CONFIG_FILE = "modo_config.txt"

def get_modo():
    """Lê o modo atual do arquivo, padrão é 'conservador'."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return file.read().strip()
    return "conservador"

def set_modo(novo_modo):
    """Salva o novo modo no arquivo."""
    with open(CONFIG_FILE, "w") as file:
        file.write(novo_modo.lower())
