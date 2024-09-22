import sys
import math

if len(sys.argv) != 3:
    print("Введіть радіус і висоту ")
    sys.exit(1)

r = int(sys.argv[1])
h = int(sys.argv[2])

volume = (1/3) * math.pi * r**2 * h

print(f"Об'єм конуса: {volume}")

