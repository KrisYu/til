# Rigid align point clouds with known correspondence


### Rigid registration of two point clouds with known correspondence

[Rigid registration of two point clouds with known correspondence](https://stackoverflow.com/questions/66923224/rigid-registration-of-two-point-clouds-with-known-correspondence)

Point clouds:

```
P = [p0, p1, ..., pn]
Q = [q0, q1, ..., qn]
```

align P and Q, RP+t = Q

$$
E  = \sum_{i=1}^n \parallel q_i-(Rp_i+  t) \parallel^2 \\
p_i \in P \\
q_i \in Q
$$



Paper: [Arun et al., 1987, Least square fitting of two 3D point sets](https://ieeexplore.ieee.org/document/4767965)

```
import numpy as np

##Based on Arun et al., 1987

#Writing points with rows as the coordinates
p1_t = np.array([[0,0,0], [1,0,0],[0,1,0]])
p2_t = np.array([[0,0,1], [1,0,1],[0,0,2]]) #Approx transformation is 90 degree rot over x-axis and +1 in Z axis

#Take transpose as columns should be the points
p1 = p1_t.transpose()
p2 = p2_t.transpose()

#Calculate centroids
p1_c = np.mean(p1, axis = 1).reshape((-1,1)) #If you don't put reshape then the outcome is 1D with no rows/colums and is interpeted as rowvector in next minus operation, while it should be a column vector
p2_c = np.mean(p2, axis = 1).reshape((-1,1))

#Subtract centroids
q1 = p1-p1_c
q2 = p2-p2_c

#Calculate covariance matrix
H=np.matmul(q1,q2.transpose())

#Calculate singular value decomposition (SVD)
U, X, V_t = np.linalg.svd(H) #the SVD of linalg gives you Vt

#Calculate rotation matrix
R = np.matmul(V_t.transpose(),U.transpose())

assert np.allclose(np.linalg.det(R), 1.0), "Rotation matrix of N-point registration not 1, see paper Arun et al."

#Calculate translation matrix
T = p2_c - np.matmul(R,p1_c)

#Check result
result = T + np.matmul(R,p1)
if np.allclose(result,p2):
    print("transformation is correct!")
else:
    print("transformation is wrong...")
```


similar code -> [rigid\_transform\_3D.py](https://github.com/nghiaho12/rigid_transform_3D/blob/master/rigid_transform_3D.py)



```
#!/usr/bin/python

import numpy as np

# Input: expects 3xN matrix of points
# Returns R,t
# R = 3x3 rotation matrix
# t = 3x1 column vector

def rigid_transform_3D(A, B):
    assert A.shape == B.shape

    num_rows, num_cols = A.shape
    if num_rows != 3:
        raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")

    num_rows, num_cols = B.shape
    if num_rows != 3:
        raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

    # find mean column wise
    centroid_A = np.mean(A, axis=1)
    centroid_B = np.mean(B, axis=1)

    # ensure centroids are 3x1
    centroid_A = centroid_A.reshape(-1, 1)
    centroid_B = centroid_B.reshape(-1, 1)

    # subtract mean
    Am = A - centroid_A
    Bm = B - centroid_B

    H = Am @ np.transpose(Bm)

    # sanity check
    #if linalg.matrix_rank(H) < 3:
    #    raise ValueError("rank of H = {}, expecting 3".format(linalg.matrix_rank(H)))

    # find rotation
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T

    # special reflection case
    if np.linalg.det(R) < 0:
        print("det(R) < R, reflection detected!, correcting for it ...")
        Vt[2,:] *= -1
        R = Vt.T @ U.T

    t = -R @ centroid_A + centroid_B

    return R, t
```
