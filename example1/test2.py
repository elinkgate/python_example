import sys
import time
import elink
print("hello")
vnc = elink.newConnection("10.0.0.1","admin","admin")
time.sleep(5)
l = vnc.remoteFileList("B:\\")
print(l)
n = 1
while n < 100:
    if not (l):
        break
    a = (l.pop(0))
    if a == 0:
        break
    print(a)
    b = (a.pop(0))
    print(b)
    c = "B:\\"+b
    vnc.remoteFileDelete(c)
    n = n+1
vnc.remoteFileUpload("D:\\refind.hdd2","B:\\")
vnc.remoteFileUpload("D:\\elinksetup.isox","B:\\")
vnc.remoteFileUpload("D:\\floppy_uefi.hdd2","B:\\")
time.sleep(10)




