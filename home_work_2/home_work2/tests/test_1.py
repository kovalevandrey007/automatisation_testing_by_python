from home_work2 import check_command, std_in, std_out, std_ex
import pytest

def test_case1():
    assert check_command(f'cd {std_in}; 7z a arch1', 'Everything Ok'), 'test1 Fail'
    
def test_case2():
    assert check_command(f'cd {std_out}; 7z e arx2.7z -o/home/andy/folder1 -y', 'Everything is Ok'), 'test2 FAIL'
    
def test_case3():
    assert check_command(f'cd {std_ex}; 7z e arx3.7z -o/home/andy/folder1 -y', 'Everything is Ok'), 'test2 FAIL'