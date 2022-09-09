import os
import shutil

def tree_printer(root):
    count = 0
    for root, dirs, files in os.walk(root):
        for d in dirs:
            if 'pycache' in d:
                path = os.path.join(root, d)
                print(path)
                shutil.rmtree(path)
                count += 1

    print(f'\n{count}\n')  
tree_printer('C:\\Users\\hp\\anaconda3')