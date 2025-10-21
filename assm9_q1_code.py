# ============================================================
# CV5100 – Modelling, Uncertainty, and Data for Engineers (MUDE)
# Assignment 9 – Signal Processing (Fourier Series)
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------------
# Task 1: Load forcing data and plot
# ------------------------------------------------------------
def task1_load_and_plot(filename):
    npzfile = np.load(filename)
    
    # Check variable names
    print("Available variables:", npzfile.files)
    
    # Adjust variable name as per your saved file (forcing1.npz)
    tspan = npzfile['tspan']
    force = npzfile['force']
    
    plt.figure(figsize=(10,4))
    
    # YOUR CODE HERE: hint : plt.plot plots array x vs array y as plot(x,y)
    plt.plot()
    plt.xlabel('Time (s)')
    plt.ylabel('Applied Force (N)')
    plt.title(f'Applied Force vs Time ({filename})')
    plt.grid(True)
    
    # YOUR CODE HERE: hint : you can use np.max of np.abs
    amplitude = 
    print(f"Amplitude of signal ≈ {amplitude:.3f}")
    
    dt = tspan[1] - tspan[0]
    
    # YOUR CODE HERE
    T0 = 
    return tspan, force, dt, T0


# ------------------------------------------------------------
# Task 2: Extract one period of the signal
# ------------------------------------------------------------
def task2_extract_one_period(tspan, force, T0):
    # YOUR CODE HERE 
    indices = np.where()
    
    t_one_period = tspan[indices]
    f_one_period = force[indices]
    
    plt.figure(figsize=(10,4))
    plt.plot(t_one_period, f_one_period, 'r', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Force (N)')
    plt.title('Force over One Period')
    plt.grid(True)
    
    return t_one_period, f_one_period


# ------------------------------------------------------------
# Task 3: Compute Fourier coefficients
# ------------------------------------------------------------
def task3_fourier_coefficients(t_one_period, f_one_period, T0, N=15):
    dt = t_one_period[1] - t_one_period[0]
    
    # YOUR CODE HERE : hint: look at the expression given in the assignment
    a0 = 
    aj = np.zeros(N)
    bj = np.zeros(N)
    
    # YOUR CODE HERE: hint: look at the expression given in the assignment
    for j in range(1, N+1):
        aj[j-1] = 
        bj[j-1] = 
    
    plt.figure(figsize=(10,4))
    plt.stem(range(1, N+1), aj, basefmt=" ")
    plt.xlabel('j')
    plt.ylabel('a_j')
    plt.title('Fourier Coefficients a_j')
    plt.grid(True)

    plt.figure(figsize=(10,4))
    plt.stem(range(1, N+1), bj, basefmt=" ")
    plt.xlabel('j')
    plt.ylabel('b_j')
    plt.title('Fourier Coefficients b_j')
    plt.grid(True)
    
    f_recon = np.zeros(np.size(f_one_period));
    f_recon = a0;
    for j in range(1, N+1):
        omega = 2*np.pi*j/T0
        f_recon += aj[j-1] * np.cos(omega*t_one_period) + bj[j-1] * np.sin(omega*t_one_period)
    
    plt.figure(figsize=(10,4))
    plt.plot(t_one_period,f_one_period, 'b', linewidth=2)
    plt.plot(t_one_period, f_recon, 'r--', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Force')
    plt.title('Comparison of actual force and reconstructed force')
    plt.grid(True)
    plt.legend(['Original', 'Reconstructed'])
    
    
    return a0, aj, bj


# ------------------------------------------------------------
# Task 4: Compute SDOF response
# ------------------------------------------------------------
def task4_sdof_response(t_one_period, T0, aj, bj, m=1.0, k=45.0, N=15):
    
    omega_n = np.sqrt(k/m)
    Xj = np.zeros(N)
    Yj = np.zeros(N)
    x_t = np.zeros_like(t_one_period)
    
    for j in range(1, N+1):
        omega = 2*np.pi*j/T0
    # YOUR CODE HERE: hint: look at the expression given in the assignment
        Xj[j-1] = 
        Yj[j-1] = 
        x_t += Xj[j-1] * np.cos(omega*t_one_period) + Yj[j-1] * np.sin(omega*t_one_period)
        
    
    plt.figure(figsize=(10,4))
    plt.plot(t_one_period, x_t, 'b', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Response x(t)')
    plt.title('SDOF System Response')
    plt.grid(True)
    
    
    return x_t


# ------------------------------------------------------------
# Task 5: Repeat for forcing2.npz and compare
# ------------------------------------------------------------
def task5_repeat_forcing(filename, N=15):
    tspan, force, dt, T0 = task1_load_and_plot(filename)
    T0 = 1/0.99
    t_one_period, f_one_period = task2_extract_one_period(tspan, force, T0)
    a0, aj, bj = task3_fourier_coefficients(t_one_period, f_one_period, T0, N)
    x_t = task4_sdof_response(t_one_period, T0, aj, bj) 
    return x_t


# ------------------------------------------------------------
# MAIN EXECUTION BLOCK
# ------------------------------------------------------------
if __name__ == "__main__":
    # === Forcing 1 ===
   
    # TASK 1: Replace with your calculated or observed period
    # tspan, force1, dt, T0 = task1_load_and_plot('forcing1.npz')
    
    # TASK 2
    # t_one_period, f_one_period = task2_extract_one_period(tspan, force1, T0)
    
    # TASK 3
    # a0, aj, bj = task3_fourier_coefficients(t_one_period, f_one_period, T0)
    
    # TASK 4
    # x_t1 = task4_sdof_response(t_one_period, T0, aj, bj)
    
    # === Forcing 2 ===
    # x_t2 = task5_repeat_forcing('forcing2.npz')
    