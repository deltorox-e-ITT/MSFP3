import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0, t0, tend, dt, w, h = 0, 0, 10, 1E-3, 10, 5
N = int(tend/dt) + 1
t = np.linspace(t0, tend, N)
u2 = np.zeros(N)
u2[round(1/dt):round(2/dt)] = 1

# Control
num_ctrl = [100*10e-6, 1-0.25]
den_ctrl = [100*(100e-6+10e-6), 1]
sys_ctrl = ctrl.tf(num_ctrl, den_ctrl)
print(f"FT Control: {sys_ctrl}\n")

# Caso
num_caso = [10e3*10e-6, 1-0.25]
den_caso = [10e3*(100e-6+10e-6), 1]
sys_caso = ctrl.tf(num_caso, den_caso)
print(f"FT Caso: {sys_caso}\n")

# Controlador
kP, kI = 0.22157, 3595.7467
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re

print(f"Cr = {Cr} F")
print(f"Re = {Re:.4f} Ω")
print(f"Rr = {Rr:.4f} Ω\n")

numPID = [Rr*Cr, 1]
denPID = [Re*Cr, 0]
PI = ctrl.tf(numPID, denPID)
print(f"FT Controlador PI: {PI}\n")

# Lazo cerrado
sys_caso_LC = ctrl.feedback(ctrl.series(PI,sys_caso),1,sign=-1)
print(f"FT Caso LC: {sys_caso_LC}\n")

# Respuestas
_, F_ctrl = ctrl.forced_response(sys_ctrl,t,u2,x0)
_, F_caso = ctrl.forced_response(sys_caso,t,u2,x0)
_, PID_caso = ctrl.forced_response(sys_caso_LC,t,F_ctrl,x0)


# Colores
clr1 = np.array([0,114,189])/255
clr2 = np.array([237,177,32])/255
clr3 = np.array([34,139,34])/255
clr4 = np.array([0.5,0.5,0.5])

# Gráfica
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman','DejaVu Serif']

# Figura 1: F(t), Control, Caso y PID
fg1 = plt.figure(1,figsize=(w,h),facecolor='white')

plt.plot(t,u2,'-',linewidth=0.5,color=clr1,label=r'$F(t)$')
plt.plot(t,F_ctrl,'--',linewidth=0.5,color=clr2,label=r'$F_s(t)$: Control')
plt.plot(t,F_caso,'--',linewidth=0.5,color=clr3,label=r'$F_s(t)$: Caso')
plt.plot(t,PID_caso,':',linewidth=1,color=clr4,label=r'$PID(t)$: Tratamiento')

plt.gca().set_facecolor('white')
plt.grid(False)
plt.box(True)

plt.xlim(0,10)
plt.xticks(np.arange(0,11,1))
plt.ylim(-0.1,1.1)
plt.yticks(np.round(np.arange(-0.1,1.11,0.1),1))

plt.xlabel('t [s]')
plt.ylabel('F(t) [V]')

plt.legend(bbox_to_anchor=(0.5,1.08),loc='center',ncol=4,frameon=False,fontsize=10)

plt.show()