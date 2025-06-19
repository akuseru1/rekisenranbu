hp = 1000

def attack(Hp):
    Hp -= 100
    return Hp

hp = attack(hp)
print(hp)
hp = attack(hp)
print(hp)
hp = attack(hp)
print(hp)

