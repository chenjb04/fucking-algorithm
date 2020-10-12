"""
 猫狗队列 :
 * 用户可以调用add方法将cat类或dog类的 实例放入队列中；
 * 用户可以调用pollAll方法，将队列中所有的实例按照进队列 的先后顺序依次弹出；
 * 用户可以调用pollDog方法，将队列中dog类的实例按照 进队列的先后顺序依次弹出；
 * 用户可以调用pollCat方法，将队列中cat类的实 例按照进队列的先后顺序依次弹出；
 * 用户可以调用isEmpty方法，检查队列中是 否还有dog或cat的实例； 用户可以调用isDogEmpty方法，
 * 检查队列中是否有dog 类的实例； 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例

"""


class Pet:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        super().__init__('dog')


class Cat(Pet):
    def __init__(self):
        super().__init__('cat')


class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_pet(self):
        return self.pet

    def get_count(self):
        return self.count

    def get_type(self):
        return self.pet.get_type()


class CatDogQueue:
    def __init__(self):
        self.dog = []
        self.cat = []
        self.count = 0

    def add(self, pet):
        if pet.get_type() == 'dog':
            self.count += 1
            self.dog.append(PetEnterQueue(pet, self.count))
        elif pet.get_type() == 'cat':
            self.count += 1
            self.cat.append(PetEnterQueue(pet, self.count))
        else:
            raise RuntimeError('error')

    def poll_all(self):
        if self.dog and self.cat:
            if self.dog[0].get_count() < self.cat[0].get_count():
                return self.dog.pop(0).get_pet()
            else:
                return self.cat.pop(0).get_pet()
        elif self.dog:
            return self.dog.pop(0).get_pet()
        elif self.cat:
            return self.cat.pop(0).get_pet()
        else:
            raise RuntimeError('error')

    def poll_dog(self):
        if self.dog:
            return self.dog.pop(0).get_pet()
        else:
            raise RuntimeError('error')

    def poll_cat(self):
        if self.cat:
            return self.cat.pop(0).get_pet()
        else:
            raise RuntimeError('error')

    def is_Empty(self):
        if self.is_DogEmpty() and self.is_CatEmpty():
            return True
        else:
            return False

    def is_DogEmpty(self):
        if not self.dog:
            return True
        else:
            return False

    def is_CatEmpty(self):
        if not self.cat:
            return True
        else:
            return False

    def show(self):
        if not self.is_DogEmpty():
            print("狗队列:")
        for i in self.dog:
            print((i.get_type(), i.get_count()), end=" ")
        print("")

        if not self.is_CatEmpty():
            print("猫队列:")
            for j in self.cat:
                print((j.get_type(), j.get_count()), end=" ")
        print("")


if __name__ == '__main__':
    cat_dog_queue = CatDogQueue()
    cat_dog_queue.add(Dog())
    cat_dog_queue.add(Dog())
    cat_dog_queue.add(Cat())
    print("入队结果:")
    cat_dog_queue.show()

    print(cat_dog_queue.poll_dog().get_type())
    print(cat_dog_queue.poll_all().get_type())
    print(cat_dog_queue.poll_all().get_type())
