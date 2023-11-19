import numpy

def editDistance(str1, str2):
  distances = numpy.zeros((len(str1) + 1, len(str2) + 1))
  for s1 in range(len(str1) + 1):
    distances[s1][0] = s1
  for s2 in range(len(str2) + 1):
    distances[0][s2] = s2     
    a = 0
    b = 0
    c = 0
    for s1 in range(1, len(str1) + 1):
      for s2 in range(1, len(str2) + 1):
        if (str1[s1-1] == str2[s2-1]):
          distances[s1][s2] = distances[s1 - 1][s2 - 1]
        else:
          a = distances[s1][s2 - 1]
          b = distances[s1 - 1][s2]
          c = distances[s1 - 1][s2 - 1]
                
          if (a <= b and a <= c):
            distances[s1][s2] = a + 1
          elif (b <= a and b <= c):
            distances[s1][s2] = b + 1
          else:
            distances[s1][s2] = c + 1

  printDistances(distances, len(str1), len(str2))
  return distances[len(str1)][len(str2)]
  
def printDistances(distances, s1Len, s2Len):
    for s1 in range(s1Len + 1):
        for s2 in range(s2Len + 1):
            print(int(distances[s1][s2]), end=" ")
        print()
        
question1 = editDistance("kitten", "sitting")
print("edit distance:", question1);
question2 = editDistance("GAMBOL","GUMBO")
print("edit distance:", question2)