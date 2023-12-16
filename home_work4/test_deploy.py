from sshcheckers import ssh_checkout, ssh_upload_files
from conftest import make_folder,del_folder, make_files, del_file
import yaml
import pytest

with open("config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# @pytest.mark.usefixtures('test_make_dir')
class Test_HW4:
    def test_deploy(self, make_folder, make_files):
        result = []
        ssh_upload_files(f'{data.get("host")}', f'{data.get("login_by_user2")}', f'{data.get("passwd")}',
                                        f'{data.get("host_path")}{data.get("file1")}',
                                         f'{data.get("guest_path")}{data.get("file1")}')
        result.append(ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}',
                                                       f'{data.get("passwd")}', f'echo "11" | sudo -S dpkg -i {data.get("host_path")}{data.get("file1")}',
                                                       "Настраивается пакет"))
        result.append(ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}',
                                                   f'{data.get("passwd")}', "echo '11' | sudo -S dpkg -s p7zip-full",
                                                   "Status: install ok installed"))
        assert all(result)

    def test_info_packag(self, del_folder, del_file):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}',
                            f'{data.get("passwd")}', "echo '11' | dpkg-query -l | grep p7zip-full",
                            "p7zip-full")
    def test_delete(self, del_folder, del_file):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login_by_user2")}',
                                   f'{data.get("passwd")}', "echo '11' | sudo -S dpkg -r p7zip-full",
                                   "Удаляется")

if __name__=='__main__':
    pytest.main(['-vv'])
