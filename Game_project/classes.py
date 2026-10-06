#chesty do których można dodać funkcje takie jak otwieranie, zamykanie, blokowanie i odblokowywanie, głównie do lootowania przedmiotów.
class chest:
    def __init__(self, name, description, items, locked=False):
        self.name = name
        self.description = description
        self.items = items
        self.locked = locked

    def open(self):
        if self.locked:
            print(f"The {self.name} is locked!")
        else:
            print(f"You open the {self.name} and find:")
            for item in self.items:
                print(f"- {item}")

    def unlock(self):
# if masz klucz to możesz odblokować skrzynię, jeśli nie masz klucza to nie możesz jej odblokować, 
# chyba że masz wytrych to możesz spróbować ją otworzyć ale masz na to 50% szansy, przy nieudanej próbie tracisz wytrych
        if self.locked:
            self.locked = False
            print(f"You unlock the {self.name}.")
        else:
            print(f"The {self.name} is already unlocked.")

#po prostu przedmioty
class item:
    def __init__(self, name, kind, description):
        self.name = name
        self.kind = kind
        self.description = description

    def use(self):
        print(f"You use the {self.name}. {self.description}")

#Drzwi do których można dodać funkcje takie jak otwieranie, zamykanie, blokowanie i odblokowywanie.
class door:
    def __init__(self, name, description, locked=False):
        self.name = name
        self.description = description
        self.locked = locked

    def open(self):
        if self.locked:
            print(f"The {self.name} is locked!")
        else:
            print(f"You open the {self.name}.")

    def unlock(self):
        if self.locked:
            self.locked = False
            print(f"You unlock the {self.name}.")
        else:
            print(f"The {self.name} is already unlocked.")

    def brake(self):
        if self.locked:
            print(f"You break the {self.name}.")
            self.locked = False

        else:
            print(f"The {self.name} is already unlocked.")


#do otrzymania obrażeń od przeciwnika, który zadaje obrażenia graczowi / Albo w przypadku akcji czy pułapki, która zadaje obrażenia graczowi.
class damage:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def taken(self):
        print(f"You take damage from the {self.name}. {self.description} It deals {self.damage} damage.")
        health = 100 - self.damage
        if health <= 0:
            print("You have died. Game over.")
        return health
    def death(self):
        print(f"You have died from the {self.name}. {self.description} It dealt {self.damage} damage.")
        return 0

class place:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions

    def enter(self):
        print(f"You enter the {self.name}. {self.description}")
        for action in self.actions:
            print(f"- {action}")

    def decide_with_two_options(self, action):
        if action in self.actions:
            print(f"You decide to {action}.")
        else:
            print(f"You can't do that here.")

    def decide_with_multiple_options(self, action):
        if action in self.actions:
            print(f"You decide to {action}.")
        else:
            print(f"You can't do that here.")