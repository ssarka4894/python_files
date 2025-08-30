import numpy as np
from scipy.linalg import solve_continuous_are

def lqr(A, B, Q, R):
    """Solve the continuous time LQR controller.
       dx/dt = A x + B u
       cost = integral (x.T*Q*x + u.T*R*u) dt
    """
    # Solve Riccati equation
    X = solve_continuous_are(A, B, Q, R)

    # Compute LQR gain
    K = np.linalg.inv(R).dot(B.T.dot(X))

    eigVals, eigVecs = np.linalg.eig(A - B.dot(K))

    return K, X, eigVals


A = np.array([[0,1],[47.77,0]])
B = np.array([[  0.  ],
       [ 10.52]])
Q = np.array([[ 100,   0],
       [  0, 1000]])
R = np.array([[0.0001]])
K,S,e = lqr(A,B,Q,R)

print("Gain: ", K)
print("Riccati Solution: ", S)
