import subprocess


std_in = '/home/andy/in'
std_out = '/home/andy/out'
std_ex = '/home/andy/ex'

def check_command(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out and result.returncode == 0:
        return True
    else:
        return False
    
if __name__=='__main__':
    check_command(f'cd {std_in}; 7z a arch1', 'Everything Ok')