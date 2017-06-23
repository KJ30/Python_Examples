import os
import cat_service
import platform
import subprocess


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder:' + folder)
    download_cats(folder)
    display_cats(folder)


# Prints Header

def print_header():
    print('------------------')
    print('   Cat Factory')
    print('------------------')


# get or create output folder

def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Directory {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


# download cats

def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat' + name)
        cat_service.get_cat(folder, name)


# display cats

def display_cats(folder):
    print('Displaying cats in OS window')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Window':
        subprocess.call(['start', folder], shell=True)
    elif platform.system() == 'Linux:':
        subprocess.call(['xdg-open', folder])
    else:
        print("we don't support your os:" + platform.system())


if __name__ == '__main__':
    main()
