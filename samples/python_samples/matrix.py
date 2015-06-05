#!/usr/bin/python

def NewPrintMatrix(matrix):
  new_row=[]
  
  # m is row; n is column
  for m in range(len(matrix)):
    #print "range(len(matrix[m])) " + str(range(len(matrix[m])))
    k=m
    for n in range(len(matrix[m])):
      try:
        new_row.append(matrix[n][k])
        k=k+1
      except IndexError:
        pass
    print new_row
    new_row=[]

  i=n=0
  for m in range(1, len(matrix)):
    i=m
    for n in range(len(matrix[m])):
      try:
        print "(i,n) : " + str(i) + str(n)
        new_row.append(matrix[i][n])
        i=i+1
      except IndexError:
        exit
    print new_row
    new_row=[]

if __name__ == '__main__':
    matrix = [
		 	['a', 'b', 'c'],
			['d', 'e', 'f', 'g'],
			['h', 'i', 'j', 'k'],
	     	]
    NewPrintMatrix(matrix)
