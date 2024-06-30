# Reference: https://zenn.dev/robes/articles/241f6c3fac1486

import math

data = [
  [3,0,0,1,3],
  [1,2,0,1,2],
  [1,1,1,0,0],
  [1,1,0,0,0]
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
  
  def cos_sim(self, y):
    sim = []
    for yy in range(len(data)):
      AdB = 0.0
      A2 = 0.0
      B2 = 0.0
      for xx in range(len(data[0])):
        a = self.data[y][xx]
        b = self.data[yy][xx]
        AdB += a * b
        A2 += a * a
        B2 += b * b
      sim.append(AdB/(math.sqrt(A2)*math.sqrt(B2)))
    return sim
    
if __name__ == '__main__':
  tf_idf_natural = TfIdf(data)
  tf_idf_base10 = TfIdf(data, 10)

  ly = len(data)
  lx = len(data[0])

  for y in range(ly):
    for x in range(lx):
      print(x, y, f'{tf_idf_natural.calc(x,y):.2f}')
 
  print('---')

  for y in range(ly):
    print(y, tf_idf_natural.cos_sim(y))

  print('---')

  for y in range(len(data)):
    for x in range(lx):
      print(x, y, f'{tf_idf_base10.calc(x,y):.2f}')

'''
0 0 0.43
1 0 0.00
2 0 0.00
3 0 0.24
4 0 0.73
0 1 0.17
1 1 0.43
2 1 0.00
3 1 0.28
4 1 0.56
0 2 0.33
1 2 0.43
2 2 0.80
3 2 0.00
4 2 0.00
0 3 0.50
1 3 0.64
2 3 0.00
3 3 0.00
4 3 0.00
---
0 [0.9999999999999998, 0.7254762501100116, 0.39735970711951313, 0.4866642633922875]
1 [0.7254762501100116, 0.9999999999999998, 0.5477225575051661, 0.6708203932499369]
2 [0.39735970711951313, 0.5477225575051661, 1.0000000000000002, 0.8164965809277259]
3 [0.4866642633922875, 0.6708203932499369, 0.8164965809277259, 0.9999999999999998]
---
0 0 0.43
1 0 0.00
2 0 0.00
3 0 0.19
4 0 0.56
0 1 0.17
1 1 0.37
2 1 0.00
3 1 0.22
4 1 0.43
0 2 0.33
1 2 0.37
2 2 0.53
3 2 0.00
4 2 0.00
0 3 0.50
1 3 0.56
2 3 0.00
3 3 0.00
4 3 0.00
'''