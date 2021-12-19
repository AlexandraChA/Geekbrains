import os

dir_name = 'my_project_2'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

new_path = os.path.join(os.getcwd(), dir_name)
os.chdir(new_path)

folders = ['settings', 'mainapp', 'authapp']
files_set = ['__init__.py', 'dev.py', 'prod.py']
files_app = ['__init__.py', 'models.py', 'views.py']
files_template = ['base.html', 'index.html']

for folder in folders:
    if folder == 'settings':
        dir_folder = folder
        if not os.path.exists(dir_folder):
            os.mkdir(dir_folder)
        new_fold_path = os.path.join(new_path, folder)
        os.chdir(new_fold_path)
        for file in files_set:
            if not os.path.exists(file):
                my_file = open(file, 'w')
                my_file.close()
        os.chdir(new_path)
    else:
        dir_folder = os.path.join(folder, 'templates', folder)
        if not os.path.exists(dir_folder):
            os.makedirs(dir_folder)
        new_fold_path = os.path.join(new_path, folder)
        os.chdir(new_fold_path)
        for file in files_app:
            if not os.path.exists(file):
                my_file = open(file, 'w')
                my_file.close()
        path_temp = os.path.join(new_fold_path, 'templates')
        path_temp_fold = os.path.join(path_temp, folder)
        os.chdir(path_temp_fold)
        for file in files_template:
            if not os.path.exists(file):
                my_file = open(file, 'w')
                my_file.close()
        os.chdir(new_path)

