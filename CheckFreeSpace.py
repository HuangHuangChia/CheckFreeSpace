import ctypes
import os
import platform
import sys
import socket

def get_space_GB(folder):
# Return folder/drive free space (in bytes)
    if platform.system() == 'Windows':
        total_bytes= ctypes.c_ulonglong(0)
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None,ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
        if total_bytes.value>0:
            return [free_bytes.value/1024/1024/1024,total_bytes.value/1024/1024/1024,free_bytes.value/total_bytes.value]
        else:
            return [free_bytes.value/1024/1024/1024,total_bytes.value/1024/1024/1024,0]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        linetoken=sys.argv[2]
        level=float(sys.argv[1])
    else :
        linetoken="CyBkMwsePVYW16lbOlRqtLEmg3O05HSBssTMgd2Vwjm"
        level=0.2
        print('CheckFreeSpace 最小剩餘空間比  line_token\nex:"CheckFreeSpace 0.2 CyBkMwsePVYW16lbOlRqtLEmg3O05HSBssTMgd2Vwjm')

hostname = socket.gethostname()
drive=["C:\\","D:\\","E:\\","F:\\","G:\\","H:\\"]
for path in drive:
    space=get_space_GB(path)
    if space[1]>0 and space[2]<level:
       
        lineMessage=hostname+"%E7%A9%BA%E9%96%93%E4%B8%8D%E8%B6%B3 "+path[0:2]+" free:"+str("%.1f" %space[0])+"GB total:"+str("%.1f" %space[1])+"GB free%25:"+str(int(space[2]*100))+"%25"
        # curl中文亂碼問題 : 中文使用在線編碼  https://tool.oschina.net/encode?type=4   
        # %用%25代替
        # 空間不足 %E7%A9%BA%E9%96%93%E4%B8%8D%E8%B6%B3
        # curl無法傳\ 故只傳前兩碼
       
        linenotify='curl -H  "Authorization: Bearer '+linetoken+'" -d "message='+lineMessage+'" https://notify-api.line.me/api/notify'
        os.system(linenotify)
