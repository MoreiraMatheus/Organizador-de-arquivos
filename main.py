import os

def organiza_arquivos(diretorio):
    os.chdir(diretorio)

    #Listas de caminhos para as pastas
    Audios_doc = os.path.join(diretorio, 'Audios')
    Fotos_doc = os.path.join(diretorio, 'Fotos')
    Videos_doc = os.path.join(diretorio, 'Videos')
    Documentos_doc = os.path.join(diretorio, 'Documentos')
    Outros_doc = os.path.join(diretorio, 'Outros')
    exe_doc = os.path.join(diretorio, 'Apps')

    #Extensões aceitas pelo programa
    audios_ext = ('.mp3', '.wav', '.aiff', '.wma', '.flac', '.alac', '.aac')
    fotos_ext = ('.jpg', '.jpeg', '.png', '.gif', '.svg', '.jfif')
    videos_ext = ('.mp4', '.mov', '.wmv', '.flv', '.avi', '.avchd', '.webm', '.mkv')
    documentos_ext = ('.pdf', '.txt', '.xlsx', '.docx', '.py', '.jar', '.zip')
    exe_ext = ('.exe', '.apk')

    #Confere se as pastas existem
    try:
        if not os.path.isdir(Audios_doc):
            os.mkdir(Audios_doc)
        if not os.path.isdir(Fotos_doc):
            os.mkdir(Fotos_doc)
        if not os.path.isdir(Videos_doc):
            os.mkdir(Videos_doc)
        if not os.path.isdir(Documentos_doc):
            os.mkdir(Documentos_doc)
        if not os.path.isdir(exe_doc):
            os.mkdir(exe_doc)
        if not os.path.isdir(Outros_doc):
            os.mkdir(Outros_doc)
    except:
        print('Erro ao criar pastas')

    #Move os arquivos
    try:
        lista_arquivos = os.listdir(diretorio)
        for arquivo in lista_arquivos:
            caminho_antigo = os.path.join(diretorio, arquivo)
            caminho_novo = ''
            if not os.path.isdir(arquivo):
                ext = arquivo[arquivo.rfind('.'):].lower()
                if ext in audios_ext:
                    caminho_novo = Audios_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Audio')
                elif ext in fotos_ext:
                    caminho_novo = Fotos_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Fotos')
                elif ext in videos_ext:
                    caminho_novo = Videos_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Videos')
                elif ext in documentos_ext:
                    caminho_novo = Documentos_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Docs')
                elif ext in exe_ext:
                    caminho_novo = exe_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Apps')
                else:
                    caminho_novo = Outros_doc
                    print(f'O arquivo {arquivo} foi movido para a pasta: Outros')
            os.replace(caminho_antigo, os.path.join(caminho_novo, arquivo))
    except:
        print('Erro ao mover arquivos')

if __name__ == '__main__':
    diretorio = r'C:\Users\famil\OneDrive\Área de Trabalho\teste'#nome do diretório que será usado
    organiza_arquivos(diretorio)
