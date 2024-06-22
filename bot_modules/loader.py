import os
import aiogram.types
from aiogram.types.input_file import FSInputFile

def loader_file(file_name: str | None = None) -> FSInputFile:
    # path_to_loader = __file__   
    # print(f"\n{path_to_loader}\n")
    # path_to_bot_modules = os.path.abspath(path_to_loader + '/..') 
    # print(f"\n{path_to_bot_modules}\n")
    # path_to_final_bot = os.path.abspath(path_to_bot_modules + '/..')
    # print(f"\n{path_to_final_bot}\n")
    # path_to_image = os.path.abspath(path_to_final_bot + f"/images/{file_name}")
    # print(f"\n{path_to_image}\n")
    path_to_image = os.path.abspath(__file__ + f'/../../images/{file_name}')
    image = aiogram.types.input_file.FSInputFile(path= path_to_image)
    return image

# loader_file(file_name= 'orig.png')