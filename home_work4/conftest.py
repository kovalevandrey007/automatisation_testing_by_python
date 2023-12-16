from sshcheckers import ssh_checkout
import pytest
import yaml
import os

with open('config.yaml', encoding = 'utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture(scope='class')
def make_folder():
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}', f'{data.get("passwd")}',
                                    'mkdir -v test1',
                                     'mkdir: created directory')

@pytest.fixture(scope='class')
def del_folder():
    yield
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}', f'{data.get("passwd")}',
                                    'rmdir -v Test1',
                                     'rmdir: removing directory')

@pytest.fixture(scope='class')
def make_files():
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}', f'{data.get("passwd")}',
                                    'touch file1 | echo "ADD_OK!"',
                                     'ADD_OK!')

@pytest.fixture(scope='class')
def del_file():
    yield
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}', f'{data.get("passwd")}',
                                    'rm file1 | echo "DEL_OK!"',
                                     'DEL_OK!')