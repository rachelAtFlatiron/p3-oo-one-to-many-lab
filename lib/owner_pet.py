import ipdb 
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name="", pet_type="", owner=None):
        self.name = name 
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property 
    def pet_type(self):
        return self._pet_type 
    @pet_type.getter 
    def pet_type(self):
        return self._pet_type 
    @pet_type.setter 
    def pet_type(self, val):
        if val not in Pet.PET_TYPES:
            raise Exception
        else: 
            self._pet_type = val 

class Owner:
    def __init__(self, name=""):
        self.name = name 

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self 
        else: 
            raise Exception
    
    
    def get_sorted_pets(self):
        # (pet) => pet.name
        return sorted(self.pets(), key=lambda pet: pet.name)

owner1 = Owner("Rick")
owner2 = Owner("Michone")
owner3 = Owner("Daryl")
owner4 = Owner("Carl")
owner5 = Owner("Carol")
owner6 = Owner("Maggie")
owner7 = Owner("Negan")

pet1 = Pet("dog", "dog")
pet2 = Pet("danai", "cat", owner2)
pet3 = Pet("gurira", "cat", owner2)
pet4 = Pet("rat", "rodent", owner5)
pet5 = Pet("lion", "exotic", owner5)
pet6 = Pet("lauren", "dog", owner6)
# ipdb.set_trace()