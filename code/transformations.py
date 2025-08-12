import numpy as np
import matplotlib.pyplot as plt

def transformation(x, y):

    # x_new = 2*x
    # y_new = 2*y

    x_new = x/(x*x+y*y)
    y_new = y/(x*x+y*y)

    # a=1
    # b=2
    # r=np.sqrt(x*x+y*y)
    # r2=np.maximum(a+r*(b-a)/b,r)
    # cos=x/r
    # sin=y/r
    # x_new=r2*cos
    # y_new=r2*sin

    return x_new, y_new

# Create a grid
roi_len=3
n_cells_area=22
x = np.linspace(-roi_len, roi_len, n_cells_area*roi_len+1)
y = np.linspace(-roi_len, roi_len, n_cells_area*roi_len+1)
X, Y = np.meshgrid(x, y)

# Remove points too close to the origin
tol=0.1
mask = (np.abs(X) < tol) & (np.abs(Y) < tol)  # Mask points near origin
X_masked = np.where(mask, np.nan, X)
Y_masked = np.where(mask, np.nan, Y)

# Apply transformation
X_trans, Y_trans = transformation(X_masked, Y_masked)

# Show both grids overlaid
plt.figure(figsize=(8, 8))

# Plot transformed grid (horizontal and vertical lines)  
plt.plot(X_trans, Y_trans, 'r-', alpha=0.8, linewidth=0.8)
plt.plot(X_trans.T, Y_trans.T, 'r-', alpha=0.8, linewidth=0.8)

# Plot original grid (horizontal and vertical lines)
plt.plot(X, Y, 'b-', alpha=0.5, linewidth=0.8)
plt.plot(X.T, Y.T, 'b-', alpha=0.5, linewidth=0.8)

# Add labels using dummy plots (only one label per grid)
plt.plot([], [], 'b-', alpha=0.5, linewidth=0.8, label='Original')
plt.plot([], [], 'r-', alpha=0.8, linewidth=0.8, label='Transformed')

plt.title('Grid Deformation Visualization')
plt.legend()

plt.axis('equal')
plt.show()
