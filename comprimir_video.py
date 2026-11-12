import tkinter as tk
from tkinter import filedialog
import subprocess, os

def escolher_video():
    print("Escolha o vídeo que deseja comprimir...")
    janela = tk.Tk()
    janela.withdraw()
    janela.attributes("-topmost", True)

    # Cria o caminho dinâmico para a pasta Vídeos/Captures do usuário atual
    caminho_padrao = os.path.join(os.path.expanduser("~"), "Videos", "Captures")

    caminho = filedialog.askopenfilename(
        title="Escolha o vídeo",
        initialdir=caminho_padrao,
        filetypes=[("Vídeos", "*.mp4 *.mov *.mkv *.avi")]
    )

    janela.destroy()
    return caminho

def comprimir(caminho_video):
    sem_extensao, extensao = os.path.splitext(caminho_video)
    saida = sem_extensao + "_comprimido.mp4"

    comando = [
        "ffmpeg", "-y",
        "-i", caminho_video,
        "-vf", "scale=-2:'min(720,ih)'",
        "-c:v", "libx264", "-crf", "28", "-preset", "slow",
        "-c:a", "aac", "-b:a", "96k",
        saida
    ]
    subprocess.run(comando)
    return saida