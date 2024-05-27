from sklearn.metrics import precision_recall_fscore_support
import numpy as np

N = int(input("Please enter the number of points (N): "))
X = np.zeros(N, dtype=int)
Y = np.zeros(N, dtype=int)
for i in range(N):
  print(f"Enter point {i+1} as pair (x, y): ")
  x = int(input("x: "))
  y = int(input("y: "))
  X[i] = x
  Y[i] = y

precision, recall, f1_score, support = precision_recall_fscore_support(X, Y, average='binary')
print("\nPrecision is:", precision) 
print("\nRecall is:", recall) 