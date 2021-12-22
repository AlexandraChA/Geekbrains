import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

new_path = os.path.join(os.getcwd(), dir_name)
os.chdir(new_path)

folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in folders:
    dir_folder = folder
    if not os.path.exists(dir_folder):
        os.mkdir(dir_folder)