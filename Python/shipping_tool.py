premium_shipping=125

def cost_ground_ship(weight):
  if weight <= 2:
    return ((1.50*weight) + 20)
  elif weight > 2 and weight <= 6:
    return ((3.00*weight) + 20)
  elif weight > 6 and weight <= 10:
    return ((4.00*weight) + 20)
  else:
    return ((4.75*weight) + 20)
  
def cost_drone_ship(weight):
  if weight <= 2:
    return (4.50*weight)
  elif weight > 2 and weight <= 6:
    return (9.00*weight)
  elif weight > 6 and weight <= 10:
    return (12.00*weight)
  else:
    return (14.25*weight)

def optimal_shipment(weight):
  if cost_ground_ship(weight) < cost_drone_ship(weight) and cost_ground_ship(weight) < premium_shipping:
    print("Ground Shipping is cheaper than Drone Shipping and Premium Shipping." + " It will cost $" + str(cost_ground_ship(weight)) + ".")
  elif cost_drone_ship(weight) < cost_ground_ship(weight) and cost_drone_ship(weight) < premium_shipping:
    print("Drone Shipping is cheaper than Ground Shipping and Premium Shipping." + " It will cost $"+ str(cost_drone_ship(weight)) + ".")
  else:
    print("Premium Shipping is cheaper than Ground Shipping and Premium Shipping." + " It will cost $" + str(premium_shipping) + ".")
  

print(optimal_shipment(4.8))

print(optimal_shipment(41.5))


  