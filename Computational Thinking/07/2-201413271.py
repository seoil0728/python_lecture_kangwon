print('201413271 김석우')

poem = """흔들리며 피는 꽃
도종환 /

흔들리지 않고 피는 꽃이 어디 있으랴
이 세상 그 어떤 아름다운 꽃들도
다 흔들리면서 피었나니
흔들리면서 줄기를 곧게 세웠나니
흔들리지 않고 가는 사랑이 어디 있으랴
젖지 않고 피는 꽃이 어디 있으랴
이 세상 그 어떤 빛나는 꽃들도
다 젖으며 젖으며 피었나니
바람과 비에 젖으며
꽃잎 따뜻하게 피웠나니
젖지 않고 가는 삶이 어디 있으랴
"""

print(poem[:55] + '\n ... 중략 ... \n')

while True:
    word = input('수정될 단어 입력 : ')
    replace = input('수정할 단어 입력 : ')

    poem = poem.replace(word, replace)
    print(poem)