import numpy as np

def calculate(list):

  if len(list) != 9 :
    raise ValueError('List must contain nine numbers.')
  
  a = np.array([ [ list[0],list[1],list[2] ] , [ list[3],list[4],list[5]] , [ list[6],list[7],list[8] ] ])

  mean = [ [np.mean(a[ : , 0:1]) , np.mean(a[ : , 1:2]) , np.mean(a[ : , 2:3])] , [np.mean(a[0]),np.mean(a[1]),np.mean(a[2])] , np.mean(a) ]

  variance = [ [np.var(a[ : , 0:1]) , np.var(a[ : , 1:2]) , np.var(a[ : , 2:3])] , [np.var(a[0]),np.var(a[1]),np.var(a[2])] , np.var(a) ]

  standart = [ [np.std(a[ : , 0:1]) , np.std(a[ : , 1:2]) , np.std(a[ : , 2:3])] , [np.std(a[0]),np.std(a[1]),np.std(a[2])] , np.std(a) ]

  max = [ [np.max(a[ : , 0:1]) , np.max(a[ : , 1:2]) , np.max(a[ : , 2:3])] , [np.max(a[0]),np.max(a[1]),np.max(a[2])] , np.max(a) ]

  min = [ [np.min(a[ : , 0:1]) , np.min(a[ : , 1:2]) , np.min(a[ : , 2:3])] , [np.min(a[0]),np.min(a[1]),np.min(a[2])] , np.min(a) ]

  sum = [ [np.sum(a[ : , 0:1]) , np.sum(a[ : , 1:2]) , np.sum(a[ : , 2:3])] , [np.sum(a[0]),np.sum(a[1]),np.sum(a[2])] , np.sum(a) ]

  dic = { 'mean': mean , 'variance': variance , 'standard deviation': standart , 'max': max , 'min': min , 'sum': sum}
  
  return dic