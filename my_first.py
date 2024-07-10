import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# a function that return the sum of two numbers
def addition(p_a: float, p_b: float) -> float:
  return p_a+p_b

# test
a = 5.0
b = 6.9
c = addition(a,b)

class Number :
  def __init__(self, value: float):
    self.value = value

  def __add__(self, other: Number):
    value = self.value + other.value
    return Number(value)

# test 
nb1 = Number(1.99)
nb2 = Number(4)
nb3 = nb1+nb2
    
  
