import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    x = np.arange(1,10)
    y = np.arange(1,10)
    
    plt.grid(True)
    plt.plot(x, y*y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Just a simple square relation")
    plt.show()
