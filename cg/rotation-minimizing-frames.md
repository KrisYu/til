# Parallel Transport

[Computation of rotation minimizing frame](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Computation-of-rotation-minimizing-frames.pdf) Section 4.2 


```
#!/usr/bin/env python3
import numpy as np



import matplotlib.pyplot as plt
import matplotlib as mpl

from scipy.spatial.transform import Rotation as R

# https://github.com/bzamecnik/gpg/blob/master/rotation-minimizing-frame/rmf.py

# Computing rotation minimization frames using the double reflection method
#
# Author: Bohumir Zamecnik <bohumir [dot] zamecnik [at] gmail [dot] com>
# Date: 2011/02/24
#
# References:
# [1] W. Wang, B. Juttler, D. Zheng, Y. Liu: Computation of Rotation Minimizing
#     Frame in Computer Graphics, 2007
# 


def normalize(v):
	norm=np.linalg.norm(v)
	assert norm != 0
	return v/norm

# ----- Frame computation -----

# Moving frame.
# A right-handed orthonormal system containing three orthogonal unit vectors:
#   r = reference (normal)
#   t = tangent
#   s = bitangent (s = t x r)
#
# The reference vector is projected so that it is made orthogonal to the
# tangent vector. The bitangent vector is made orthogonal to the others.
# All vectors are then normalized. This is one step of the Gram-Schmidt
# orthogonalization.
class Frame:
	def __init__(self, reference, tangent):
		self.t = normalize(tangent)
		# make reference vector orthogonal to tangent
		proj_r_to_t = np.dot(reference, tangent) / np.dot(tangent, tangent)  * tangent
		self.r = normalize(reference - proj_r_to_t)
		# make bitangent vector orthogonal to the others
		self.s = normalize(np.cross(self.t, self.r)) 
		
	def __str__(self):
		return "Frame[r: {}, s: {}, t: {}]".format(self.r, self.s, self.t)
# Compute rotation minimizing frames for a set of points and associated
# tangent vector using the double reflection method.
#
# points - list of vectors
# tangents - list of vectors; must be of the same size as points
# initFrame - initial frame, Frame
def doubleReflection(points, tangents, initFrame):
	n = len(points)
	assert n == len(tangents)
	# computed frames with minimal rotation
	frames = [initFrame]
	for i in range(0, n - 1):
		# compute reflection vector of R_1
		v1 = points[i + 1] - points[i]
		c1 = np.dot(v1, v1)
		# compute r_i^L = R_1 * r_i
		ref_L_i = frames[i].r - (2 / c1) * np.dot(v1, frames[i].r) * v1
		# compute t_i^L = R_1 * t_i
		tan_L_i = frames[i].t - (2 / c1) * np.dot(v1, frames[i].t) * v1
		# compute reflection vector of R_2
		v2 = tangents[i+1] - tan_L_i
		c2 = np.dot(v2, v2)
		# compute r_(i+1) = R_2 * r_i^L
		ref_next = ref_L_i - (2 / c2) * np.dot(v2, ref_L_i) * v2
		frames.append(Frame(ref_next, tangents[i+1]))
	return frames




def generate_helix_points(n = 50):
	
	t = np.linspace(0, 4 * np.pi, n )
	
	xs = 10 * np.cos(t)
	ys = 10 * np.sin(t)
	zs = 2 * t
	
	
	points = np.zeros((n, 3))
	
	points[:, 0] = xs
	points[:, 1] = ys
	points[:, 2] = zs
	
	return points


def generate_circle_points(n = 20):
	
	
	t = np.linspace(0, 2 * np.pi, n )
	
	xs = 10 * np.cos(t)
	ys = 10 * np.sin(t)
	zs = 0
	
	
	points = np.zeros((n, 3))
	
	points[:, 0] = xs
	points[:, 1] = ys
	points[:, 2] = zs
	
	return points

def generate_straight_line( n = 20):
	
	def lerp(r, point1, point2):
		point1 = np.asarray( point1 )
		point2 = np.asarray( point2 )
		
		return (1 - r) * point1 + r * point2
	
	ts = np.linspace(0, 1, n )
	p0 = [0, 0, 0]
	p1 = [20, 20, 20]
	
	points = [ lerp(t, p0, p1) for t in ts]
	
	return points

def generate_corner_points():
	
	p0 = [0, 0, 0]
	p1 = [10, 0, 0]
	p2 = [10, 10, 0]
	p3 = [10, 10, 10]
	
	
	
	points = [p0, p1, p2, p3]
	
	return np.asarray(points)


def fem_tangents(points):
	'''
	forward finite difference to calculate tangents	
	Given :	
		points
	Return:
		tangents
	'''
	t = []
	for i in range(len(points) -1 ):
		t.append( (points[i+1] - points[i]) / np.linalg.norm(points[i+1] - points[i]) )
	t.append( t[-1] )

	return t



def orthogonal( v ):
	'''
	'''
	v = np.asarray( v )
	
	mini = 0
	
	if np.abs(v[1]) < np.abs(v[mini]):
		mini = 1
	if np.abs( v[2] ) < np.abs( v[mini]):
		mini = 2
		
	other = np.array([0, 0, 0])
	other[mini] = 1
	
	return np.cross(v, other )


n = 50 

points = generate_helix_points()
points = generate_circle_points()
points = generate_straight_line()
points = generate_corner_points()

points = np.asarray(points)

xs = points[:,0]
ys = points[:,1]
zs = points[:,2]

tangents = fem_tangents(points)

t0 = tangents[0]
print('t0', t0)

r0 = normalize( orthogonal(t0) )
print('r0', r0)


print('np.dot(t0, n0)', np.dot(t0, r0))
initFrame = Frame(r0, t0)
print(initFrame)


frames = doubleReflection(points, tangents, initFrame)

normals = [frame.r for frame in frames]
bitangents = [frame.s for frame in frames]



# draw the curve 
fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(111, projection='3d')
#ax.view_init(vertical_axis='y', elev=30, azim=135)
ax.set_aspect('equal')



T = np.asarray(tangents)
N = np.asarray( normals )
B = np.asarray(bitangents)



ax.plot(xs, ys, zs, color = 'black')


for i in range(len(points)):
	x, y, z = points[i]
	nx, ny, nz = N[i]
	bx, by, bz = B[i]
	tx, ty, tz = T[i]
	ax.quiver(x, y, z, tx, ty, tz, length = 2, color = 'red')
	ax.quiver(x, y, z, nx, ny, nz, length = 2, color = 'green')
	ax.quiver(x, y, z, bx, by, bz, length = 2, color = 'blue')
	

plt.axis('off')
plt.axis('equal')
plt.show()
```


