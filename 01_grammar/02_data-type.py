print('hello \a world')

# 문자열

# 1. 큰따옴표로 양쪽 둘러싸기
"Hello World"
"he's name is "
# 2. 작은따옴표로 양쪽 둘러싸기
'"Python is fun"'
# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."



# List

odd = [1, 3, 5, 7, 9]

# 삼중 리스트
threeA = [1, 2, ['a', 'b', ['Life', 'is']]]

print(threeA[2][2][0])


## 함수

a_list = [3, 4, 62, 27, 83, 956, 26, 58, 3, 78, 168, 64, 78]

def print_list(a):  # 지금부터 print_list 함수를 만들겠다는 뜻
    for i in a:
        print(i)

print_list(a_list)

# if 
a = 5

if a == 5 :
    print('5입니다')

car = ['k5', 'sonata', 'e-class']

if 'k5' in car :
    print('재고 있음')


numbers = 1000

if 1000 in numbers :