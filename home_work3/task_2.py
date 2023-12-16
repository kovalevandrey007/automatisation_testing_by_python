from test_seminar2 import check_command, get_hash
import pytest
import yaml

with open('config.yaml', encoding = 'utf-8') as f:
    data = yaml.safe_load(f)

@pytest.mark.usefixtures('make_folder', 'make_files', 'del_folder','add_data_in_txt')
class TestSeminar:

    def test_step1(self):
        assert check_command(f'cd {data.get("folder_in")}; 7z a {data.get("folder_out")}/archive1; {data.get("type")} *', 'Everything is Ok')

    def test_step2(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z rn archive1 file1.txt file2.txt', 'Everything is Ok')

    def test_step3(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z i archive1', '0  ED  6F00181 AES256CBC')

    def test_step4(self):
        output = str(get_hash(f'cd {data.get("folder_out")}; crc32 archive1.7z')).upper()[2:]
        assert check_command(f'cd {data.get("folder_out")}; 7z h archive1.7z', output)

    def test_step_5(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z x archive1.7z A', 'Everything is Ok')

if __name__=='__main__':
    pytest.main(['-vv'])