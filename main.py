import os

def organize_files(directory):
    os.chdir(directory)

    #Listas de caminhos para as pastas
    Audios_doc = os.path.join(directory, 'Audios')
    Photos_doc = os.path.join(directory, 'Fotos')
    Videos_doc = os.path.join(directory, 'Videos')
    Documents_doc = os.path.join(directory, 'Documentos')
    Others_doc = os.path.join(directory, 'Outros')
    Apps_doc = os.path.join(directory, 'Apps')

    #Extensões aceitas pelo programa
    Audios_ext = ('.mp3', '.wav', '.aiff', '.wma', '.flac', '.alac', '.aac')
    Photos_ext = ('.jpg', '.jpeg', '.png', '.gif', '.svg', '.jfif')
    Videos_ext = ('.mp4', '.mov', '.wmv', '.flv', '.avi', '.avchd', '.webm', '.mkv')
    Documents_ext = ('.pdf', '.txt', '.xlsx', '.docx', '.py', '.jar', '.zip')
    Apps_ext = ('.exe', '.apk')

    #Confere se as pastas existem
    try:
        if not os.path.isdir(Audios_doc):
            os.mkdir(Audios_doc)
        if not os.path.isdir(Photos_doc):
            os.mkdir(Photos_doc)
        if not os.path.isdir(Videos_doc):
            os.mkdir(Videos_doc)
        if not os.path.isdir(Documents_doc):
            os.mkdir(Documents_doc)
        if not os.path.isdir(Apps_doc):
            os.mkdir(Apps_doc)
        if not os.path.isdir(Others_doc):
            os.mkdir(Others_doc)
    except:
        print('Erro ao criar pastas')

    #Move os arquivos
    try:
        file_list = os.listdir(directory)
        for file in file_list:
            old_way = os.path.join(directory, file)
            new_way = ''
            if not os.path.isdir(file):
                ext = file[file.rfind('.'):].lower()
                if ext in Audios_ext:
                    new_way = Audios_doc
                    print(f'O arquivo {file} foi movido para a pasta: Audio')
                elif ext in Photos_ext:
                    new_way = Photos_doc
                    print(f'O arquivo {file} foi movido para a pasta: Fotos')
                elif ext in Videos_ext:
                    new_way = Videos_doc
                    print(f'O arquivo {file} foi movido para a pasta: Videos')
                elif ext in Documents_ext:
                    new_way = Documents_doc
                    print(f'O arquivo {file} foi movido para a pasta: Docs')
                elif ext in Apps_ext:
                    new_way = Apps_doc
                    print(f'O arquivo {file} foi movido para a pasta: Apps')
                else:
                    new_way = Others_doc
                    print(f'O arquivo {file} foi movido para a pasta: Outros')
            os.replace(old_way, os.path.join(new_way, file))
    except:
        print('Erro ao mover arquivos')

if __name__ == '__main__':
    directory = r''#nome do diretório que será usado
    organize_files(directory)
