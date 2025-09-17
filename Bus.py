class vehicle:
 def __init__(self, name, maxspeed, mileage):
  self.name = name 
  self.maxspeed = maxspeed
  self.mileage = mileage 
class bus (vehicle):
 pass 
schoolbus =bus ("School Lakers ",180, 12)
print ("Vehicle name: ", schoolbus.name,"speed:",schoolbus.maxspeed,"mileage:",schoolbus.mileage)