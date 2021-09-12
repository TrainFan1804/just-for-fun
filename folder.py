import os


root_path = r'F:\Neuer Ordner'

folders = ['folder 01', 'folder 02', 'folder 03']

for folder in folders:

    os.mkdir(os.path.join(root_path, folder))