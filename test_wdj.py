import subprocess

cmd = 'pwd'
a = subprocess.getstatusoutput(cmd)

print(type(a))
print(a[0])
print(a[1])
