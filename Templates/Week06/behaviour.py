'''
    Behaviour Template Base Class
    Base class from which all components
    (behaviours) must inherit

    This ensures code modularity and consistency
'''
class Behaviour:
    def __init__(self):
        #We will include base functionality here
        pass
    def update(self):
        #Not all behaviours require update functionality
        pass
    def render(self):
        #not all behaviours require a render functionality
        pass
    #Custom functionality can be inherited here
