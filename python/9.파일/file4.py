with open("./output/input.txt", "w") as f: #./ : 파일을 찾는다는 듯
    while True:
        text = input("저장할 내용 입력(종료-z)")
        if text == 'z' or text == 'Z':
            break
        f.write(text + '\n')
        f.close()
        
#text.txt 파일과 연결