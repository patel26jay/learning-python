def displayInventory(inv):
  print "Inventory:"
  total = 0
  for k,v in inv.items():
    print "%s %s" %(v,k)
    total = total+v
  print "Total number of items: %d" %total

def addToInventory(inventory, addedItems):
  for item in addedItems:
    if item not in inventory.keys():
      inventory.setdefault(item,0)
    inventory[item] += 1
  return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#displayInventory(stuf)
