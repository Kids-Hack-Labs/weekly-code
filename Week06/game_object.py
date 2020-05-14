'''
    Game Object Template Class
    Built for later inclusion of functionality
    Will behave as a list of Behaviours
    OBS: thinking of converting into a dictionary
         of behaviours
    For now, it has a position (we'll talk about
    transforms in a future class)

    Ultimately, the screens will be responsible for
    managing Game Objects and their behaviours
'''
class GameObject:
    def __init__ (self, _x, _y):
        #We will include functionality here
        self.x = _x
        self.y = _y
        self.is_active = True
        self.behaviours = []
    def update (self):
        #We will include functionality here
        for behaviour in self.behaviours:
            if behaviour.is_active:
                behaviour.update()
    def render(self):
        #We will include functionality here
        for behaviour in self.behaviours:
            if behaviour.is_active:
                behaviour.render()
    def add_behaviour(self, behaviour):
        #Functionality will be explained in class
        if behaviour not in self.behaviours:
            behaviour.game_object = self
            self.behaviours.append(behaviour)
