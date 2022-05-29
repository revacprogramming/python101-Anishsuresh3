class Menu:
  my_menu=[]
  def __init__(self,name='',price=0):
    self.my_menu.append((name,price))
  def __add__(self,a):
    return Menu(a[0],a[1])
  def __str__(self):
    st=''
    sd=self.my_menu[1:]
    for a,b in sd:
      st+=a+' '+str(b)+'\n'
    return st[:-1]

m = Menu()
m = m + ("idly", 10) + ("vada", 20) + ('dosa',50)

# Hint: operator overloading special methods (__add__, __sub__, etc.)
print(m)  # should print the menu properly
