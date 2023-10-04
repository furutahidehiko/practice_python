# import string
import os
import pathlib
import glob
import shutil
import tarfile
import zipfile
import tempfile
import subprocess
import datetime

# s = """\
# AAAA
# BBBB
# CCCC
# DDDD
# """
# with open('test.txt','r+') as f:
#   f.write(s)
#   f.seek(0)
#   print(f.read())
  # print('I am print',file=f)
  # f.close()

# with open('test.txt','r') as f:
#     # print(f.read())
#     # while True:
#     #     chunk = 2
#     #     line = f.read(chunk)
#     #     print(line)
#     #     if not line:
#     #         break
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))

# with open('design/email_template.txt') as f:
#   t = string.Template(f.read())
# contents = t.substitute(name='Mike',contents='How are you')
# print(contents)


# ファイル操作
# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('design'))
# os.rename('test.txt','rename.txt')
# os.symlink('rename.txt','symlink.txt')
# os.mkdir('test_dir')
# os.rmdir('test_dir')
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/sub_test.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt','test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))
# shutil.rmtree('test_dir')
# print(os.getcwd())

# with tarfile.open('test.tar.gz','w:gz') as tr:
#     tr.add('test_dir')

# with tarfile.open('test.tar.gz','r:gz') as tr:
#     # tr.extractall(path='test_tar')
#     with tr.extractfile('test_dir/test_dir2/sub_test.txt') as f:
#         print(f.read())

# with zipfile.ZipFile('test.zip','w') as z:
#     # z.write('test_dir')
#     # z.write('test_dir/test_dir2/empty.txt')
#     # z.write('test_dir/test_dir2/empty2.txt')
#     # z.write('test_dir/test_dir2/sub_test.txt')
#     for f in glob.glob('test_dir/**',recursive=True):
#         print(f)
#         z.write(f)

# with zipfile.ZipFile('test.zip','r') as z:
#     # z.extractall('test2_dir')
#     with z.open('test_dir/test_dir2/sub_test.txt') as f:
#         print(f.read())

# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())

# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name,'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())

# with tempfile.TemporaryDirectory() as td:
#     print(td)

# tmp_dir = tempfile.mkdtemp()
# print(tmp_dir)

# subprocess.run(['ls','-al'])
# r = subprocess.run('ls',shell=True,check=True)
# print('end')

# p1 = subprocess.Popen(['ls','-al'],stdout=subprocess.PIPE)
# p2 = subprocess.Popen(
#     ['grep','test'],
#     stdin=p1.stdout,
#     stdout=subprocess.PIPE)
# p1.stdout.close()
# output = p2.communicate()[0]
# print(output)

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(now.strftime('%d/%m/%y'))
