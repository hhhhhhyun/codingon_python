
#<20241213>
#바이너리 파일
with open("./output/data.bin", "wb") as f :
    txt = "안녕"
    f.write(txt.encode())

with open("./output/data.bin", "rb") as f:
    data = f.read()
    print(data)
    print(data.decode()) #encode과 decode는 한 쌍!

with open("./output/h.png", "rb") as f1 :
    img = f1.read()

with open("./output/h1.png", "wb") as f2:
    f2.write(img)


