train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp=(f_temp-32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp=c_temp * (9/5) + 32
  return f_temp

def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass):
  c=3*10**8
  return mass * c**2

def get_work(mass, acceleration, distance):
  work=get_force(mass, acceleration)*distance
  return work

f100_in_celsius=f_to_c(100)
c0_in_fahrenheit=c_to_f(0)
train_force= get_force(train_mass,train_acceleration)
train_work=get_work(train_mass, train_acceleration, train_distance)
bomb_energy=get_energy(bomb_mass)

#Temperature Conversion
print("100F equals " + str(round(f100_in_celsius, 1)) + " Celsius")
print("0C equals " + str(c0_in_fahrenheit) + " Farenheit\n")

#Train Force
print("Train force = " + str(train_force))
print("The GE train supplies " + str(train_force) +" Newtons of force.\n")

#Train Work
print("Train work = " + str(train_work))
print("The GE train does "+ str(train_work) + " Joules of work over " + str(train_distance) + " meters.\n")

#Bomb Energy
print("Bomb energy = " + str(bomb_energy))
print("A 1kg bomb supplies "+ str(bomb_energy) + " Joules.")

