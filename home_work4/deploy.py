from sshcheckers import ssh_checkout, ssh_upload_files
import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    def deploy():
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
        print(result)
        return all(result)


    if deploy():
        print('Деплой успешен!')
    else:
        print('Ошибка деплоя!')
