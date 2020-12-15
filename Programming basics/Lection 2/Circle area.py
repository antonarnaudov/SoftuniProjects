#import math

from cmath import pi

from math import pow

r = float(input())
peri = 2*(pi)*r   #ako e math.pi i math.pow se pishe import math
lice = (pi)*(pow(r,2))  #ako importna samo pi i pow nqma nujda da pisha math.pi/math.pow

print(f"{lice:.2f}")
print(f"{peri:.2f}")

#.2f - formatira do vtoro chislo
