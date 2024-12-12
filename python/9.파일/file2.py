#이차원 리스트 만들기
import random

with open("word.txt", 'w') as f: #word 찾기 : ctrl+shift+f
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'grape', 'garlic', 'onion', 'potato']
    for i in word:
        f.write(i + ' ')

with open("word.txt", 'r') as f:
    data = f.read().split()
    word = random.choice(data)
    print(word)

