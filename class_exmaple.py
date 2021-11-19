class person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        # print('Hello')
        # print(self.hello)
        print('{0} 저는 {1}입니다. 나이는 {2}이고, 주소는 {3}입니다.'.format(self.hello, self.name, self.age, self.address))

    # def hello(self):
    #     self.greeting()

# james = person()
# james.greeting() # >>> 안녕하세요
# james.hello()
# isinstance(james, person)

maria = person('마리아', 30, '서울시 서초구 반포동')
maria.greeting()


def factorial(n):
    if not isinstance(n, int) or n < 0: # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)
