## Given an image represented by an NxN matrix, where each pixel in the image is 4
## bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

## 3 5 0 == 1 8 3 ##
## 8 4 2 == 6 4 5 ##
## 1 6 9 == 9 2 0 ##

m = [[3, 5, 0],
     [8, 4, 2],
     [1, 6, 9]]

def rotate_matrix(m):
     for i in range(len(m)):
          for k in range(len(m)):
               tmp = m[i][k]
               m[i][k] = m[k][len(m)-i-1]
               m[k][len(m)-i-1] = tmp
     return m
