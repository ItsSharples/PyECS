
class Entity:
    _id = 0


class Component:
    yes = 0

    

class System:
    system_component = Component
    internal_list = {}# list(tuple(int, component))

    def __init__(self):
        internal_list = []

    def addEntity(self, entity : int):
        self.internal_list[entity] = self.system_component()

    def doesContain(self, entity:int):
        return entity in self.internal_list

    def getEntity(self, entity:int):
        return self.internal_list[entity]

    def update(self, dt):
        return NotImplemented


    
class AC (Component):
    x,y,z = 0,0,0

class ACSystem(System):
    system_component = AC
    yes = 12

    def update(self, dt):
        for tuples in self.internal_list:
            entt = tuples[1]
            print(entt)
    


class Registry:
    Systems = {}

    def __init__(self):
        self.registerSystem(ACSystem, AC)
        

    def registerSystem(self, sys : System, component : Component):
        if component in self.Systems: return
        self.Systems[component] = sys()

    def addComponent(self, Type, entity):
        self.Systems[Type].addEntity(entity)

    def updateAll(self, dt : float):
        for value in self.Systems.values():  
            print("Updating: " + str(value))
            value.update(dt)

    def getComponent(self, entity):
        sys = {}
        for value in self.Systems.values():
            if value.doesContain(entity):
               sys[value.system_component] = value.getEntity(entity)
        return sys

    def getComponentView(self, entity, types):
        sys = {}
        for type_ in types:
            if type_ in self.Systems:
                value = self.Systems[type_]
                if value.doesContain(entity):
                    sys[value.system_component] = value.getEntity(entity)
        return sys
        
               


    
    
       
