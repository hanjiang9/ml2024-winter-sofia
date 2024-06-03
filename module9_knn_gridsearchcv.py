from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import numpy as np

N = int(input("Enter the number of training points (N): "))

X_train = np.zeros((N, 2), dtype=float)
y_train = np.zeros(N, dtype=int)

print("Each point's X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.")

for i in range(N):
  print(f"Enter training point {i+1} (x, y): ")
  x = float(input("x: "))
  y = int(input("y: "))
  X_train[i] = [x, y]
  y_train[i] = y

M = int(input("Enter the number of test points (M): "))

X_test = np.zeros((M, 2), dtype=float)
y_test = np.zeros(M, dtype=int)

for i in range(M):
  print(f"Enter test point {i+1} (x, y): ")
  x = float(input("x: "))
  y = int(input("y: "))
  X_test[i] = [x, y]
  y_test[i] = y

param_grid = {'n_neighbors': range(1, 11)}

knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nBest k:", best_model.n_neighbors)
print("\nTest accuracy:", accuracy)