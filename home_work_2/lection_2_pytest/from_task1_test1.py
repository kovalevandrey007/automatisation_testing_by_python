import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
    
# # 1 variable with seminar1 
# if __name__=='__main__':
#     # test1
#     if checkout('cd /home/andy/test; 7z a ../out/arx1', 'Everything is Ok'):
#         print('test1 SUCCUSS')
#     else:
#         print('test1 FAIL')
#     # test2
#     if checkout('cd /home/andy/out; 7z e arx1.7z -o/home/andy/folder1 -y', 'Everything is Ok'):
#         print('test1 SUCCUSS')
#     else:
#         print('test1 FAIL')
#     # test3
#     if checkout('cd /home/andy/out; 7z t arx1.7z', 'Everything is Ok'):
#         print('test1 SUCCUSS')
#     else:
#         print('test1 FAIL')

# 2 variable to seminar2 by pytest 
# if __name__=='__main__':
#     # test1
#     assert checkout('cd /home/andy/test; 7z a ../out/arx1', 'Everything is Ok'), print('test1 FAIL')
#     # test2
#     assert checkout('cd /home/andy/out; 7z e arx1.7z -o/home/andy/folder1 -y', 'Everything is Ok'), print('test1 FAIL')
#     # test3
#     assert checkout('cd /home/andy/out; 7z t arx1.7z', 'Everything is Ok'), print('test1 FAIL')