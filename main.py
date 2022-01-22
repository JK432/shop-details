# Create a class Shop with the following attributes and methods :
# Attributes: ItemId, ItemName, and quantity
# Methods: buy(), sell() and total_items()

# Create two instances of the class and call the methods for each instance . The quantity of the Shop object should be updated each time when it calls its corresponding methods 
class shop:
  def __init__(self):
    self.ItemId=input()
    self.ItemName=input()
    self.quantity=int(input())

  def buy(self,quan):
    self.quantity=self.quantity+int(quan)
  def sell(self,quan):
    self.quantity=self.quantity-quan
  def tot(self):
    print("ItemId =",self.ItemId)
    print("ItemName =",self.ItemName)
    print("Quantity =",self.quantity)

p1=shop()
p1.buy(10)
p1.sell(5)
p1.tot()