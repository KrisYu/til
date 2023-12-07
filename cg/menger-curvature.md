# Menger Curvature  

[Computation of rotation minimizing frame](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Computation-of-rotation-minimizing-frames.pdf) Section 4.2 


```
def menger_curvature(x, y, z):
    '''
    https://en.wikipedia.org/wiki/Menger_curvature
    Given:
        x, y, z : 3 points
    Return:
        menger curvature    
    '''
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    
    a = np.linalg.norm(x - y)
    b = np.linalg.norm(y - z)
    c = np.linalg.norm(z - x)
    
    area = np.linalg.norm( np.cross(x - y, z - x) )
    
    if area < 1e-20: result = 0
    else: result = 2 * area / ( a * b * c)
        
    return result
```


