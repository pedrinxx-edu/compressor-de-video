import os
from comprimir_video import escolher_video, comprimir

caminho_video = escolher_video()
if not caminho_video:
    print("Nenhum vídeo escolhido.")
else:
    saida = comprimir(caminho_video)
    antes = os.path.getsize(caminho_video) / (1024 * 1024)
    depois = os.path.getsize(saida) / (1024 * 1024)
    print(f"Antes: {antes:.1f} MB | Depois: {depois:.1f} MB")