#import ctypes
import os
#import platform
import sys
#import socket
import pathlib


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path=sys.argv[1]
        linetoken=sys.argv[2]
    else :
        linetoken="CyBkMwsePVYW16lbOlRqtLEmg3O05HSBssTMgd2Vwjm"
        path=str(pathlib.Path().absolute())+"\\"+"freespace.txt"
        print('Curl_LineNotify 路徑+檔名  LinrToken\nex:"Curl_LineNotify d:test.txt CyBkMwsePVYW16lbOlRqtLEmg3O05HSBssTMgd2Vwjm ')

#currentpath=str(pathlib.Path().absolute())+"\\"
#path_status=currentpath+"freespace.txt"

        
if(os.path.isfile(path)): 
    with open(path, mode='r',encoding='UTF-8') as f:
        content=f.readlines()
        linenotify='curl -H  "Authorization: Bearer '+linetoken+'" -d "message='+content[0]+'" https://notify-api.line.me/api/notify'
        os.system(linenotify)
