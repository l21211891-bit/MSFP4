
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# Datos generales de la simulacion
x0,t0,tend,dt,w,h = 0,0,15,1E-3,8,4.5
N = round(tend/dt)+1
t = np.linspace(t0,tend,N)

# Señal de entrada
u = np.array(pd.read_excel('/Users/montserrat/Downloads/signal-3.xlsx',header=None))
u = signal.resample(u,N,axis=0)
Pa = u[:,0]

# Funcion de transferencia
def cardio(Z,L,R,C):
    num = [L*R,R*Z]
    den = [C*L*R*Z,L*R+L*Z,R*Z]
    sys = ctrl.tf(num,den)
    L = np.roots(den)
    return sys,L

# Hipotenso
Z,L,R,C = 0.010,0.001,1.00,3.500
syshipo,L = cardio(Z,L,R,C)
print('Funcion de transferencia del hipotenso:',syshipo)
print('Polos:',L)

# Normotenso
Z,L,R,C = 0.010,0.001,1.00,1.500
sysnormo,L = cardio(Z,L,R,C)
print('Funcion de transferencia del normotenso:',sysnormo)
print('Polos:',L)

# Hipertenso
Z,L,R,C = 0.010,0.001,1.00,1.000
syshiper,L = cardio(Z,L,R,C)
print('Funcion de transferencia del hipertenso:',syshiper)
print('Polos:',L)

# Controlador PID
def controlador(kP,kI,kD,sys):
    Cr = 1E-6
    Re = 1/(kI*Cr)
    Rr = kP*Re
    Ce = kD/Rr
    numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
    denPID = [Re*Cr,0]
    PID = ctrl.tf(numPID,denPID)
    sysPID = ctrl.feedback(ctrl.series(PID,sys),1,sign=-1)
    return sysPID

# Controlador hipotenso
hipoPID = controlador(458.438,1112094.736,0.00627,syshipo)
print('Hipotenso con PID:',hipoPID)

# Controlador hipertenso
hiperPID = controlador(126.595,293327.703,0.00140,syshiper)
print('Hipertenso con PID:',hiperPID)

# Funcion en lazo abierto
def openloop(t,sys,u):
    _,y = ctrl.forced_response(sys,t,u,x0)
    return y

# Funcion en lazo cerrado
def closedloop(t,sysPID,u):
    _,y = ctrl.forced_response(sysPID,t,u,x0)
    return y

# Respuestas en lazo abierto
PpL = openloop(t,syshipo,Pa)
PpN = openloop(t,sysnormo,Pa)
PpH = openloop(t,syshiper,Pa)

# Respuestas en lazo cerrado
PIDL = closedloop(t,hipoPID,Pa)
PIDH = closedloop(t,hiperPID,Pa)

# Colores
# Colores de las gráficas
clr1 = np.array([119,190,240])/255  # Azul claro
clr2 = np.array([255,203,97])/255   # Amarillo
clr3 = np.array([6,66,50])/255      # Verde oscuro

# Funcion para generar graficas
def grafica(numero,y1,y2,y3,label1,label2,label3,archivo):
    fg = plt.figure(numero,figsize=(w,h))

    plt.plot(t,y1,color=clr1,linewidth=1,linestyle=':',label=label1)
    plt.plot(t,y2,color=clr2,linewidth=1,linestyle=':',label=label2)
    plt.plot(t,y3,color=clr3,linewidth=1,linestyle=':',label=label3)

    plt.xlim(0,15)
    plt.xticks(np.arange(0,16,1))

    plt.ylim(-0.6,1.4)
    plt.yticks(np.arange(-0.6,1.41,0.2))

    plt.xlabel('t [s]')
    plt.ylabel('Vi(t) [V]')

    plt.legend(
        loc='upper center',
        bbox_to_anchor=(0.5,-0.12),
        ncol=3,
        frameon=False
    )

    plt.tight_layout()

    fg.savefig('/Users/montserrat/Downloads/'+archivo,bbox_inches='tight')

# Grafica 1: Lazo abierto
grafica(
    1,
    PpN,PpL,PpH,
    'Normotenso','Hipotenso','Hipertenso',
    'Lazo_abierto_python.pdf'
)

# Grafica 2: Hipotenso con PID
grafica(
    2,
    PpN,PpL,PIDL,
    'Normotenso','Hipotenso','PID Controlador',
    'Hipotenso_python.pdf'
)

# Grafica 3: Hipertenso con PID
grafica(
    3,
    PpN,PpH,PIDH,
    'Normotenso','Hipertenso','PID Controlador',
    'Hipertenso_python.pdf'
)

# Mostrar las tres graficas
plt.show()
