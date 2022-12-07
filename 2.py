import subprocess
from pexpect import popen_spawn
import pexpect


token = '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'
git_url = 'github.com/huojiayang/test123.git'
cmd = "cd /Users/zhongfener/Desktop/python/BookSystem"
returned_value = subprocess.call(cmd, shell=True)

cmd = 'git init'
subprocess.call(cmd, shell=True)

cmd = "git add ."
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "just test！！！"'
subprocess.call(cmd, shell=True)

cmd = 'git checkout -b dev'
subprocess.call(cmd, shell=True)

cmd = 'git remote remove origin'
subprocess.call(cmd, shell=True)

cmd = "git remote add origin https://{}@{}".format(token, git_url)

subprocess.call(cmd, shell=True)

cmd = "git push -u origin dev -f"
subprocess.call(cmd, shell=True)

print(cmd, 66666)