'''
    Game Object Template Class
    Built for later inclusion of functionality
    Will behave as a list of Behaviours
    For now, it has a position (we'll talk about
    transforms in a future class)

    Ultimately, the screens will be responsible for
    managing Game Objects and their behaviours
'''
class GameObject:
    def __init__ (self, _x, _y):
        #We will include functionality here
        pass
    def update (self):
        #We will include functionality here
        pass
    def render(self):
        #We will include functionality here
        pass
    def add_behaviour(self, behaviour):
        #Functionality will be explained in class
        pass
