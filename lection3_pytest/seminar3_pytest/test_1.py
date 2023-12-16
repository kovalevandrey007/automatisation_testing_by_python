import random
import pytest
import yaml
import string
from checkers import checkout, getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def make_folders():
    return checkout("mkdir {} {} {} {}".format(data['folder_in'], data['folder_out'], data['folder_ext'], data['folder_ext2']), "")

@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data['folder_in'], data['folder_out'], data['folder_ext'], data['folder_ext2']), "")

@pytest.fixture()
def make_files():
    list_off_files = [ ]
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename, data["bs"]), ""):
            list_off_files.append(filename)
    return list_off_files

@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not checkout("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername, testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename
def test_step1():
    # test1
    res1 = checkout("cd {}; 7z a {}/arx2".format(data['folder_in'], data['folder_out']), "Everything is Ok")
    res2 = checkout("ls {}".format(data['folder_out']), "arx2.7z")
    assert res1 and res2, "test1 FAIL"

def test_step2():
    # test2
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(data['folder_out'], data['folder_ext']), "Everything is Ok")
    res2 = checkout("ls {}".format(data['folder_ext']), "test1")
    res3 = checkout("ls {}".format(data['folder_ext']), "test2")
    assert res1 and res2 and res3, "test2 FAIL"

def test_step3():
    # test3
    assert checkout("cd {}; 7z t arx2.7z".format(data['folder_out']), "Everything is Ok"), "test3 FAIL"

def test_step4():
    # test4
    assert checkout("cd {}; 7z u arx2.7z".format(data['folder_in']), "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    res1 = checkout("cd {}; 7z l arx2.7z".format(data['folder_out'], data['folder_ext']), "test1.txt")
    res2 = checkout("cd {}; 7z l arx2.7z".format(data['folder_out'], data['folder_ext']), "test2.txt")
    assert res1 and res2, "test5 FAIL"

def test_step6():
    # test6
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(data['folder_out'], data['folder_ext2']), "Everything is Ok")
    res2 = checkout("ls {}".format(data['folder_ext2']), "test1")
    res3 = checkout("ls {}".format(data['folder_ext2']), "test2")
    res4 = checkout("ls {}".format(data['folder_ext2']), "testfldr")
    res5 = checkout("ls {}".format(data['folder_ext2']), "test3")
    assert res1 and res2 and res3 and res4 and not res5, "test6 FAIL"

def test_step7():
    # test7
    assert checkout("cd {}; 7z d arx2.7z".format(data['folder_out']), "Everything is Ok"), "test7 FAIL"

def test_step8():
    # test8
    res1 = checkout("cd {}; 7z h test1.txt".format(data['folder_in']), "Everything is Ok")
    hash = getout("cd {}; crc32 test1.txt".format(data['folder_in'])).upper()
    res2 = checkout("cd {}; 7z h test1.txt".format(data['folder_in']), hash)
    assert res1 and res2, "test8 FAIL"