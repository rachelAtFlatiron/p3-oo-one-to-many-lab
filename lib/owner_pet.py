class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = [] 

    #a Pet has one and only one owner
    #a Pet belongs to an Owner 
    def __init__(self, name, pet_type, owner=None):
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
        if val in Pet.PET_TYPES: 
            #self.pet_type = val will gives us recursion error 
            #self.pet_type = val refers to @pet_type.setter
            self._pet_type = val   
        else: 
            raise Exception

class Owner:
    def __init__(self, name=""):
        self.name = name 

    # Owner has many pets 
    def pets(self):
        # pets = []
        # #loop through all pets
        # for pet in Pet.all:
        #     #find matching owners 
        #     if(pet.owner == self):
        #         pets.append(pet)
        # return pets

        return [pet for pet in Pet.all if(pet.owner == self)]
    
    def add_pet(self, pet):
        #check pet is type Pet 
        if(isinstance(pet, Pet)):
            #add self as pet owner 
            pet.owner = self 
        else: 
            raise Exception
        
    # (el) => el.name 
    # lambda -> keyword for anonymous function 
    # el -> refers to current element sorted() is looking at 
    # el.name -> refers to what property/thing of el we want sorted() to sort by
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda el: el.name)