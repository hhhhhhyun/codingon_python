#<20241205>

#2차원 리스트
gugu = [
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    [3, 7],
    [3, 8],
    [3, 9]
]
for x, y in gugu :
    print(f"{x} * {y} = {x*y}")

# " for i in~ 사용해서 똑같이 출력
gugu = [
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    [3, 7],
    [3, 8],
    [3, 9]
]
for i in gugu :
    print(f"{i[0]} * {i[1]} = {i[0]*i[1]}")