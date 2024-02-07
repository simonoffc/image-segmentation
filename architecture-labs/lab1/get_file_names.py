import os


def get_file_names(directory: str) -> list:
    files = os.listdir(directory)
    files = [file for file in files if os.path.isfile(os.path.join(directory, file))]
    return files


if __name__ == '__main__':
    files_list: list = get_file_names(os.getcwd() + '\\images\\input')
    for file_name in files_list:
        print(file_name)
