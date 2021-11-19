class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff) # 클래스 이름으로 클래스 속성에 접근

james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('cosmetic')

print(james.bag)
print(maria.bag)
print(Person.bag)


