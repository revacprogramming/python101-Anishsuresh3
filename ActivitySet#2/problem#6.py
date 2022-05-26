

class Menu:
  price=[]
  name=[]
  def add(self,name,price):
    self.name.append(name)
    self.price.append(price)
  def show(self):
    print(self.name[0],self.price[0])
    print(self.name[1],self.price[1])
    
  


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()

