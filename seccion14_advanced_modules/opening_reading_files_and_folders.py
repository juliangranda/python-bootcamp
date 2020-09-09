f = open('practice.txt','w+')
f.write('this is a test string')
f.close()

#permite obtener la ruta en el sistema operativo
import os
print(os.getcwd())

#muestra lo que esta en esa ruta del os
print(os.listdir())
print(os.listdir('C:\\Users'))

#mover los archivos
import shutil
#shutil.move('practice.txt','C:\\Users')

#eliminar algo
#pip install send2trash

import send2trash
print(os.listdir())
send2trash.send2trash('practice.txt')

file_path = 'D:\\autodidacta\\python-bootcamp\\python\\seccion14_advanced_modules\\example_top_level'
for folder, sub_folders, files in os.walk(file_path):
    print(f"current looking at {folder}")
    print('\n')
    print('the subfolders are: ')
    for sub_fold in sub_folders:
        print(f"subfolder: {sub_fold}")

    print('\n')
    print('the files are: ')
    for f in files:
        print(f"file: {f}")
    print('\n')