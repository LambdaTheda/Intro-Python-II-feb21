# Implement a class to hold room information. This should have name and
# description attributes.
  ##RAINBOW BRACERS 

#ROOM MADE YAY!
class Room:
  def __init__ (self, name, description):
    self.name = name
    self.description = description
    
    self.s_to = None
    self.n_to = None
    self.e_to = None
    self.w_to = None
 
  def __str__ (self):
    return f"{self.description}"