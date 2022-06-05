class Menu(dict):
    """fill in class definition here"""
  def __dict__(self,key='',value=0):
    self.__dict__[key]=value
  def __str__(self):
    return ('\n'.join([str(a+' '+str(b)) for a,b in self.__dict__.items()]))
    
class Order(dict,Menu):
    """fill in class definition here"""
  def __dict__(self,key1='',value1=0):
    self.__dict__[key1]=value1
    
  
  
  


class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
