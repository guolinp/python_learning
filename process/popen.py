#!/usr/bin/python -tt

from subprocess import Popen, PIPE

def issue_cmd(cmd):
    p = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    text, err = p.communicate()
    rc = p.returncode
    return rc, text, err


cmd = "ls -al"
print("cmd: {}".format(cmd))
rc, text, err = issue_cmd(cmd)
print("rc: {}".format(rc))
print("output:")
for line in text.split('\n'):
    print(line)
print("err:\n{}".format(err))
print(err)

print("-----------------")

cmd = "ls -al x"
print("cmd: {}".format(cmd))
rc, text, err = issue_cmd(cmd)
print("rc: {}".format(rc))
print("output:")
for line in text.split('\n'):
    print(line)
print("err:\n{}".format(err))
