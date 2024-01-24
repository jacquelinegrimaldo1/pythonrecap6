import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")


#these lines of code will be on the quiz 
#1st step: create a VE for mac it is python3 -m venv myvenv
#2nd step: Activate the VE for mac it is source myvenv/bin/activate 
#3rd step: Install 3rd party library/module and the name is pip3 install matplotlib
# there is also pip 3 uninstall which removes the library 