from pathlib import Path
from colorama import Fore

def print_dir_structure(dir_path, tabs: int = 0):
    try:
        dir = Path(dir_path).iterdir()

        for path in dir:
            if path.is_dir():
                print(Fore.BLUE + f'{'-- ' * tabs}{path.name}/')
                print_dir_structure(path, tabs = tabs + 1)
            else:
                print(Fore.YELLOW + f'{'-- ' * tabs}{path.name}')

    except Exception as e:
        print(e)