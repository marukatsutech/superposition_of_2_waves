# Superposition of 2 waves 2D
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np


def change_k1(value):
    global k1
    k1 = float(value)


def change_k2(value):
    global k2
    k2 = float(value)


def change_o1(value):
    global omega1
    omega1 = float(value)


def change_o2(value):
    global omega2
    omega2 = float(value)


def change_a1(value):
    global a1
    a1 = float(value)


def change_a2(value):
    global a2
    a2 = float(value)


def reset_parameter():
    global k1, k2, omega1, omega2, a1, a2
    k1 = 1.
    k2 = 1.
    omega1 = omega_max
    omega2 = omega_min
    a1 = a_max
    a2 = a_max
    # Set Initial value of spinbox
    var_a1.set(a1)
    var_k1.set(k1)
    var_o1.set(omega1)
    var_a2.set(a2)
    var_k2.set(k2)
    var_o2.set(omega2)


def set_axis():
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_title('Sine waves; A * sin(k*x -omega*t)')
    ax1.set_ylabel('y')
    ax1.grid()

    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(y_min, y_max)
    ax2.set_title('Superposed wave')
    ax2.set_xlabel('x (* pi)')
    ax2.set_ylabel('y')
    ax2.grid()


def update(f):
    ax1.cla()  # Clear ax
    ax2.cla()  # Clear ax
    set_axis()

    ax1.text(x_min, y_max * 0.9, "Step(as t)=" + str(f))
    if k1 != 0:
        vp1 = omega1 / k1
        ax1.text(x_min, y_max * 0.7, "Phase velocity1(omega1/k1)=" + str(vp1))
    if k2 != 0:
        vp2 = omega2 / k2
        ax1.text(x_min, y_max * 0.5, "Phase velocity2(omega2/k2)=" + str(vp2))
    if (k1 - k2) != 0:
        vg = (omega1 - omega2) / (k1 - k2)
        ax2.text(x_min, y_max * 0.9, "Group velocity(d_omega/dk)=(omega1-omega2)/(k1-k2)=" + str(vg))
    else:
        ax2.text(x_min, y_max * 0.9, "None group velocity")

    # Draw sin curve
    y1 = a1 * np.sin((k1 * x - omega1 * f) * np.pi)  # sin(kx - omega*t)
    y2 = a2 * np.sin((k2 * x - omega2 * f) * np.pi)  # sin(kx - omega*t)
    y_superposed = y1 + y2
    ax1.plot(x, y1, linestyle='-', label="A1=" + str(a1) + ", k1=" + str(k1) + ", omega1=" + str(omega1))
    ax1.plot(x, y2, linestyle='-', label="A2=" + str(a2) + ", k2=" + str(k2) + ", omega2=" + str(omega2))
    ax1.legend(prop={"size": 8}, loc="best")
    ax2.plot(x, y_superposed, linestyle='-')


# Global variables
x_min = 0.
x_max = 8.
y_min = -2.
y_max = 2.

# Parameter of sine wave
k1 = 1.
k2 = 1.
k_min = 0.
k_max = 20.
k_step = 1.
omega1 = 0.25
omega2 = -0.25
omega_min = -0.25
omega_max = 0.25
omega_step = 0.01
a1 = 1.
a2 = 1.
a_min = 0.
a_max = 1.
a_step = 0.1

# Generate line space
x = np.linspace(0, x_max, 1000)

# Generate tkinter
root = tkinter.Tk()
root.title("Superposition of 2 waves")

# Generate figure and axes
fig = Figure(figsize=(8, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Embed a figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()

# Animation
anim = animation.FuncAnimation(fig, update, interval=50)

# Toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()

# Label and spinbox for a1
label_a1 = tkinter.Label(root, text="A1")
label_a1.pack(side='left')
var_a1 = tkinter.StringVar(root)  # variable for spinbox-value
var_a1.set(a1)  # Initial value
s_a1 = tkinter.Spinbox(
    root, textvariable=var_a1, format="%.1f", from_=a_min, to=a_max, increment=a_step,
    command=lambda: change_a1(var_a1.get()), width=5
    )
s_a1.pack(side='left')
# Label and spinbox for k1
label_k1 = tkinter.Label(root, text="k1")
label_k1.pack(side='left')
var_k1 = tkinter.StringVar(root)  # variable for spinbox-value
var_k1.set(k1)  # Initial value
s_k1 = tkinter.Spinbox(
    root, textvariable=var_k1, format="%.1f", from_=k_min, to=k_max, increment=k_step,
    command=lambda: change_k1(var_k1.get()), width=5
    )
s_k1.pack(side='left')
# Label and spinbox for omega1
label_o1 = tkinter.Label(root, text="omega1")
label_o1.pack(side='left')
var_o1 = tkinter.StringVar(root)  # variable for spinbox-value
var_o1.set(omega1)  # Initial value
s_o1 = tkinter.Spinbox(
    root, textvariable=var_o1, format="%.2f", from_=omega_min, to=omega_max, increment=omega_step,
    command=lambda: change_o1(var_o1.get()), width=5
    )
s_o1.pack(side='left')

# Label and spinbox for a2
label_a2 = tkinter.Label(root, text=", A2")
label_a2.pack(side='left')
var_a2 = tkinter.StringVar(root)  # variable for spinbox-value
var_a2.set(a2)  # Initial value
s_a2 = tkinter.Spinbox(
    root, textvariable=var_a2, format="%.1f", from_=a_min, to=a_max, increment=a_step,
    command=lambda: change_a2(var_a2.get()), width=5
    )
s_a2.pack(side='left')
# Label and spinbox for k2
label_k2 = tkinter.Label(root, text="k2")
label_k2.pack(side='left')
var_k2 = tkinter.StringVar(root)  # variable for spinbox-value
var_k2.set(k1)  # Initial value
s_k2 = tkinter.Spinbox(
    root, textvariable=var_k2, format="%.1f", from_=k_min, to=k_max, increment=k_step,
    command=lambda: change_k2(var_k2.get()), width=5
    )
s_k2.pack(side='left')
# Label and spinbox for omega2
label_o2 = tkinter.Label(root, text="omega2")
label_o2.pack(side='left')
var_o2 = tkinter.StringVar(root)  # variable for spinbox-value
var_o2.set(omega2)  # Initial value
s_o2 = tkinter.Spinbox(
    root, textvariable=var_o2, format="%.2f", from_=omega_min, to=omega_max, increment=omega_step,
    command=lambda: change_o2(var_o2.get()), width=5
    )
s_o2.pack(side='left')
# button
b_reset = tkinter.Button(root, text="Reset", command=reset_parameter)
b_reset.pack(side='left')

# main loop
set_axis()
tkinter.mainloop()
