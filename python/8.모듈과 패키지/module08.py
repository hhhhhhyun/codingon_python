#os 모듈
import os

os.chdir("C:\codingon") #터미널에 pwd 치면 파일 주소가 나온다
dir = os.popen('git status')
dir = os.popen('dir')
print(dir.read())
print(os.listdir())
print('-------------------------------------------------------')
