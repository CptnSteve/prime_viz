import numpy as np
import matplotlib.pyplot as plt

def move_right(x,y):
  return x+1, y
def move_left(x,y):
  return x-1, y
def move_up(x,y):
  return x,y+1
def move_down(x,y):
  return x,y-1

def gen_points(end):
  from itertools import cycle
  moves = [move_right, move_down, move_left, move_up]
  _moves = cycle(moves)
  n = 1
  pos = 0,0
  times_to_move = 1

  yield prime_check(n), pos[0], pos[1], n
  
  while True:
    for _ in range(2):
      move = next(_moves)
      for _ in range(times_to_move):
        if n >= end:
          return
        pos = move(*pos)
        n+=1
        yield prime_check(n), pos[0], pos[1], n
    times_to_move+=1

def plotting(x, y):
  plt.scatter(x,y)
  plt.show()

def prime_check(num):
  prime_status = 1
  if (num==1):
    prime_status = 0
  for i in range(2,num):
    if (num % i == 0):
      prime_status = 0
      break
  return prime_status
  
def main():
  GRID_LEN = 150
  grid_area = GRID_LEN * GRID_LEN
  x = []
  y = []
  
  for val in gen_points(grid_area):
    if val[0] == 1:
      x.append(val[1])
      y.append(val[2])
    if val[3] % 100 == 0:
      print("Eval: ", val[3], " out of ", grid_area)
  
  plotting(x,y)
  
  
main()
