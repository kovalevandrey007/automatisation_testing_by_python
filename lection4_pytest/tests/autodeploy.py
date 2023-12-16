from sshcheckers import ssh_checkout, ssh_upload_files

def deploy():
    result = []
    ssh_upload_files("0.0.0.0" , "user2" , "11" , "7zip.deb" ,
                     "/home/user2/7zip.deb" )
    result.append(ssh_checkout("0.0.0.0", "user2", "11", "echo '11' | sudo -S dpkg -i 7zip.deb",
                               "Настраивается пакет"))
    result.append(ssh_checkout("0.0.0.0", "user2", "11", "echo '11' | sudo -S dpkg -s 7zip",
                               "Status: install ok installed"))
    return all(result)

if deploy():
    print('Деплой успешен!')
else:
    print('Ошибка деплоя!')