import os
import shutil
import tempfile
import filecmp

passed = 0
tested = 0
 
SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
MYCVS = SOURCE_DIR + '/mycvs.py'
open('main.py')
 
def start_test():
    TEST_DIR = tempfile.mkdtemp()
    os.chdir(TEST_DIR)
 
def test_init_creates_directory_mycvs_if_not_existed():
    start_test()
 
    global passed
    global tested

    command_line = ('python3 ' if os.name != 'nt' else '') + '"' + MYCVS + '"' + ' init'
    os.system(command_line)

    if os.path.isdir('mycvs'):
        print('Test passed')
        passed += 1
        tested += 1
    else:
        print('Test failed')
        tests_tested += 1


def test_commit_creates_directory_for_new_version():
    start_test()

    global passed
    global tested

    os.mkdir('mycvs')
    os.system(('python3 ' if os.name != 'nt' else '') + '"' + MYCVS + '"' + ' commit')
    os.chdir('mycvs')
    number = open('number.txt', 'r')
    commit_number = str(int(number.readlines()[-1]))

    if os.path.isdir('v' + commit_number):
        print('Test passed')
        passed += 1
        tested += 1
    else:
        print('Test failed')
        tested += 1

def test_checkout_returns_correct_file():
    start_test()

    global passed
    global tested

    os.system(('python3 ' if os.name != 'nt' else '') + '"' + MYCVS + '"' + ' checkout' + ' v1')
    if filecmp.cmp('main.py', '/mycvs/v1/main.py'):
        print('Test passed')
    else:
        print('Test failed')


test_init_creates_directory_mycvs_if_not_existed()
test_commit_creates_directory_for_new_version()
test_checkout_returns_correct_file()

print('tests_passed:', passed, '/', tested)