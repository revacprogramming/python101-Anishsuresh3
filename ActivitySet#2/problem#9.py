class Menu(dict):
  """fill in class definition here"""
  def __init__(self):
    self.d={}
  def __setitem__(self,key='',value=0):
    if(key in self.d):
        self.d[key]+=value
    else:
        self.d[key]=value
  def __str__(self):
    return ('\n'.join([str(a+' '+str(b)) for a,b in self.d.items()]))
    
class Order(Menu):
  def __init__(self,class_m):
    self.d1={}
    self.class_m=class_m
  def __setitem__(self,key1='',value1=0):
    if key1 in self.class_m:
        print('True')
        if self.class_m[key1]>=value1:
          self.d1[key1]=value1
        else:
          self.d1[key1]=self.class_m[key1]
          print('Not enough quantity but can provide ',self.class_m[key1])
          
     
  
  def __str__(self):
    return str(self.d1)
      
      
    
    
class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20
print(m)
o = Order(m)
try:
    o["vada"] = 2
    print(o)
    o["pongal"] = 2
    print(o)

except KeyError as e:
    print(e)

print(o)
#b = Bill(m, o)
#print(b)
