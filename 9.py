import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
def lwr(x,y,x0,tau):
    m=len(x)
    X=np.c_[np.ones(m),x]
    
    X0=np.array([1,x0])
    w=np.exp(-(x-x0)**2/(2*tau**2))
    W=np.diag(w)
    thetha=np.linalg.pinv(X.T@W@X)@X.T@W@y
    return X0@thetha


x=np.linspace(0,10,100)
y=np.sin(x)+np.random.randn(100)*0.3
x_t=np.linspace(0,10,300)
y_t=np.array([lwr(x,y,x0,tau=0.3) for x0 in x_t])

plt.figure(figsize=(8,4))
plt.title("LWR")
plt.scatter(x,y,color="green")
plt.plot(x_t,y_t,color="red")
plt.show()
    
