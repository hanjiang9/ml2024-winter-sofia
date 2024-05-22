from sklearn.neighbors import KNeighborsRegressor
import numpy as np

def get_user_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      if value > 0:
        return value
      else:
        print("Negative values not accepted.")
    except ValueError:
      print("Input is not an integer.")

def get_point():
  while True:
    try:
      x = float(input("Enter x: "))
      y = float(input("Enter y: "))
      return np.array([x, y])
    except ValueError:
      print("x or y is not real numbers")

def main():
  N = get_user_input("Enter the number of data points (N): ")
  k = get_user_input("Enter the number of neighbors (k): ")
  if k > N:
    print("Error: k cannot be greater than N.")
    return
  data = np.zeros((N, 2))
  labels = np.zeros(N)
  print("Enter data points (x, y) one by one:")
  for i in range(N):
    data[i] = get_point()
    labels[i] = data[i, 1]
  y_variance = np.var(labels)
  print("Variance of y values as labels:", y_variance)
  model = KNeighborsRegressor(n_neighbors=k)
  model.fit(data[:, 0:1], labels)
  X = float(input("Enter X value for prediction: "))
  X_pred_array = np.array([[X]])
  y_pred_array = model.predict(X_pred_array)
  print("Predicted Y value:", y_pred_array[0])

if __name__ == "__main__":
  main()
