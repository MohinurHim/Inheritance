# Задача "Съедобное, несъедобное":
class Animal(): #класс животных
    alive = True  # живой
    fed = False  # накормленный
    def __init__(self, name):
        self.name = name # индивидуальное название каждого животного
    def eat(self, food):
        if food.edible: # если съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Mammal(Animal): #класс млекопитающих
    pass

class Predator(Animal): #класс хищников
    pass

class Plant(): # класс растений
    edible = False  # съедобность
    def __init__(self, name):
        self.name = name # индивидуальное название каждого растения

class Flower(Plant): # класс цветов
    pass

class Fruit(Plant): # класс фруктов
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = True # Переопределяем атрибут




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1) 
a2.eat(p2)
print(a1.alive)
print(a2.fed)
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытил