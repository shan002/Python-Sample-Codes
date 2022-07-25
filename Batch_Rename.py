import os

os.chdir(r'S:\Path_Way_to_Machine_Learning\Learning to program with Python 3 (py 3.7)')
# print(os.getcwd())

for file in os.listdir():
    name, ext = os.path.splitext(file)
    # print(name)
    name_li = name.split('p.')
    if len(name_li) == 2:
        name_li[1] = name_li[1].zfill(2)
        name_li[0] = name_li[0].split('- Python')[0].strip()
        new_name = f'{name_li[1]}. {name_li[0]}{ext}'
        print(new_name)
        # os.rename(file, new_name)
