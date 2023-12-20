import numpy as np
import matplotlib.pyplot as plt

k = float(input("Введите теплопроводность в Вт/(см*К): "))
T_m = float(input("Введите температуру плавления в градусах Цельсия: "))
T_k = 20
l = float(input("Введите длину стержня в сантиметрах: "))
dx = float(input("Введите шаг по длине стержня в сантиметрах: "))
t0 = float(input("Введите время отсчёта в секундах: "))
dt = 0.5 * (dx**2) / k
n = int(np.ceil(l/dx))
m = int(np.ceil(t0/dt))
p = np.zeros([m+1, n+1])

# Set initial conditions
for i in range(m+1):
    p[i, 0] = T_m/2
    p[i, n] = T_k

for j in range(1, n):
    p[0, j] = T_k

# Explicit finite-difference method
for v in range(m):
    for q in range(1, n):
        p[v+1, q] = dt * k / (dx**2) * (p[v, q+1] - 2*p[v, q] + p[v, q-1]) + p[v, q]

print(p)
print()
print()
t = float(input("Введите время замера в которое хотите получить график зависимости в секундах: "))
d = int(np.ceil(t/dt))
x=[]
y=[]
for l in range(0,n):
    x.append(dx*l)
    y.append(p[d,l])
plt.plot(x,y, 'g')
plt.title(f"График температуры стержня в момент времени t={t} секунд")
plt.xlabel('Длина, см')
plt.ylabel('Температура, °C')
plt.grid(True)
plt.show()
