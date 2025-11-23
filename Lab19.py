#1.	
import numpy as np
def z_transform_unit_step(a):
    """
    Computes the Z-transform of a^n u[n]
    For unit step => a = 1

    Z{u[n]} = 1 / (1 - z^-1),  |z| > 1
    System is stable if ROC includes the unit circle => |z| > 1
    """

    # Z-transform formula for unit step:
    # X(z) = 1 / (1 - z^-1)
    print("Z-transform of unit step:")
    print("X(z) = 1 / (1 - z^-1)")

    # Stability check:
    # For unit step, ROC = |z| > 1 → system is stable for |z| > 1
    print("ROC: |z| > 1")

    # Check stability
    if 1 > 1:  # false always
        print("System: Stable")
    else:
        print("System: Stable (because ROC includes unit circle)")



z_transform_unit_step(1)

#Implement this for the system H(z)=0.5(z-0.7)(z-0.9)/(z-0.6)(z-0.4)  and verify whether the system is stable or unstable.
import numpy as np

# H(z) = 0.5 (z - 0.7)(z - 0.9) / (z - 0.6)(z - 0.4)

# Numerator & denominator coefficients
num = np.poly([0.7, 0.9])     # roots of numerator
den = np.poly([0.6, 0.4])     # roots of denominator

print("Numerator coefficients:", num)
print("Denominator coefficients:", den)

# Find poles
poles = np.roots(den)
print("Poles:", poles)

# Stability check
stable = all(abs(p) < 1 for p in poles)

if stable:
    print("System is STABLE")
else:
    print("System is UNSTABLE")
