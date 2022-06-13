class Menu(dict):
  """fill in class definition here"""
  def __setitem__(self,key='',value=0):
    if(key in self.__dict__):
        self.__dict__[key]+=value
    else:
        self.__dict__[key]=value
  def __str__(self):
    return ('\n'.join([str(a+' '+str(b)) for a,b in self.__dict__.items()]))
 
  
  
    
class Order(Menu):
  """fill in class definition here"""
  def __setitem__(self,key1='',value1=0):
    if self.__dict__[key1] in Menu.__dict__:
        self.__dict__[key1]=value1
     
  
  def __str__(self):
    return str(self.__dict__)
      
      
    
    
class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20
print(m)
o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

print(o)
#b = Bill(m, o)
#print(b)
