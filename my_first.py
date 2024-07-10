# a function that return the sum of two numbers
def addition(p_a: float, p_b: float) -> float:
  return p_a+p_b

class Number :
  def __init__(self, value: float):
    self.value = value

  def __add__(self, other):
    value = self.value + other.value
    return Number(value)
  def __str__(self):
    return (str(self.value))

# test 
nb1 = Number(1.99)
nb2 = Number(4)
nb3 = nb1+nb2
print(nb3)

# test
a = nb1.value
b = nb2.value
c = addition(a,b)
print(c)
