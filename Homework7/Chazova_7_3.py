import  os
import shutil
new_path = os.path.join(os.getcwd(), 'my_project_2')
os.chdir(new_path)
dir_name = 'templates'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
new_path_temp = os.path.join(new_path, 'templates')
paths = []

for root, dirs, files in os.walk(new_path):
    if dirs == ['templates']:
        path_temp = os.path.join(root, 'templates')
        paths.append(path_temp)
    if root in paths:
        path_fold = os.path.join(root, dirs[0])
        path_new_fold = os.path.join(new_path_temp, f'{dirs[0]}')
        try:
            shutil.copytree(path_fold, path_new_fold)
        except:
            print('Такой файл уже создан')