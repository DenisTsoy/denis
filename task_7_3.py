import os
import shutil

root_dir = './my_project' #текущий проект
template_folder='templates' #папка шаблонов
os.mkdir(os.path.join(root_dir, template_folder)) #создаем папку в в текущем проекте
template_path = os.path.join(root_dir,template_folder) #путь в текущем проекте

for root, dirs, files in os.walk(root_dir):
    if template_folder in set(dirs):  #в рабочем проекте ищем все папки templates
        dirictory =os.path.join(root, template_folder)
        list_dirs =os.listdir(dirictory)
        for aktual_dirs in list_dirs:
            os.mkdir(os.path.join(template_path, aktual_dirs)) # переносим название папок в новый проект
            current_folder = os.path.join(root, template_folder, aktual_dirs) #текущая папка с фаилами
            new_folder = os.path.join(template_path, aktual_dirs) #новая папка с файлами
            for root, dirs, files in os.walk(current_folder):
                for file in files:
                    shutil.copy2(os.path.join(current_folder, file), new_folder) #копирование фаилов
