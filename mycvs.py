import os
import sys
import shutil

command = sys.argv[1]
source_dir = os.path.dirname(os.path.abspath(__file__))

if command == 'init':
    os.mkdir('mycvs')
    os.chdir('mycvs')
    number = open('number.txt', 'w')
    number.write('0\n')

if command == 'commit':
    #create a directory for commit
    os.chdir('mycvs')
    number = open('number.txt', 'r+')
    commit_number = int(number.readlines()[-1])
    os.mkdir('v' + str(commit_number + 1))
    number.write(str(commit_number + 1) + '\n')
    number.close()

    #copy file to the directory
    commit_directory = '/mycvs' + '/v' + str(commit_number + 1)
    shutil.copy(source_dir + '/main.py', source_dir + commit_directory)

if command == 'checkout':
    version = sys.argv[2]
    os.remove('main.py')
    version_dir = '/mycvs/' + version
    shutil.copy(source_dir + version_dir + '/main.py', source_dir)
