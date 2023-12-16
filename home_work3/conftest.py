import pytest
import yaml
from task_2 import check_command
from datetime import datetime
import os

with open('config.yaml', encoding = 'utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope = 'class')
def make_folder():
    return check_command(f'mkdir -v {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', 'создан каталог')

@pytest.fixture(scope = 'class')
def del_folder():
    yield
    return check_command(f'rm -rfv {data.get("folder_in")}  {data.get("folder_out")} {data.get("folder_ex")}', 'удалён каталог')

@pytest.fixture(scope = 'class')
def make_files():
    return check_command(f'cd {data.get("folder_in")}; touch file1.txt file2.txt file3.txt', '')

@pytest.fixture(scope = 'class')
def add_data_in_txt():
    with open('stat.txt', 'a+', encoding = 'utf-8') as s:
        lst = []
        date = datetime.now().isoformat()
        file_size = os.path.getsize ( "./conftest.py")
        count_files = 0
        for root_dir, cur_dir, files in os.walk(r'./'):
            count_files += len(files)
        lst.append(f'Время создания: {date}')
        lst.append(f'Размер файла conftest.py = {file_size} byte')
        lst.append(f'Количество файлов в текущем каталоге = {count_files}')
        for file in lst:
            s.write(str(file)+'\n')
        return check_command ( 'cd ./; less stat.txt' , '' )



