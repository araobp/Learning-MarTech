# Reference: https://zenn.dev/robes/articles/241f6c3fac1486

import math

data = [
  [3,0,0],
  [1,2,0],
  [1,1,1]
]

class TfIdf:
  def __init__(self, data, base=math.e):
    self.data = data
    self.base = base

  def _tf(self, x, y):
    return self.data[y][x]/sum(self.data[y])

  def _idf(self, x):
    l = [1 for d in self.data if d[x] > 0]
    return math.log(len(self.data)/sum(l), self.base) + 1
  
  def calc(self, x, y):
    return self._tf(x, y) * self._idf(x)
    

if __name__ == '__main__':
  tf_idf_natural = TfIdf(data)
  tf_idf_base10 = TfIdf(data, 10)

  for y in range(3):
    for x in range(3):
      print(x, y, f'{tf_idf_natural.calc(x,y):.2f}')
 
  print('---')
  for y in range(3):
    for x in range(3):
      print(x, y, f'{tf_idf_base10.calc(x,y):.2f}')
