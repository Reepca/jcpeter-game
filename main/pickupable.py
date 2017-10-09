class Pickupable(object):
    
    def __init__(self):
        pass
        
    def pickUp(self):
        raise NotImplementedError
        
    def inventoryImage(self):
        raise NotImplementedError