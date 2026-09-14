"""Preliminary calculated values: inputs are assumed/proposed, never measured."""
from math import *
MM=1e-3
moving_mass_kg=0.80; accel_m_s2=2.0; belt_radius_m=6*MM
axis_force_n=moving_mass_kg*accel_m_s2*2; axis_torque_nm=axis_force_n*belt_radius_m
sensor_range_n=50.; ideal_force_code_n=sensor_range_n/(2**16-1)
E_pa=69e9; load_n=15.; span_m=.08; I_m4=(.020*.040**3-.014*.034**3)/12
deflection_m=load_n*span_m**3/(3*E_pa*I_m4)
pixel_scale_mm=70/1920
power_w={"axes":72,"controller":12,"camera_light":15,"gripper":10,"tester":3}; total_power_w=sum(power_w.values())
cycle_s=4*(4+3+2+3)+12
print("LOOMFORGE PRELIMINARY — CALCULATED/ASSUMED, NOT MEASURED")
print(f"Axis force {axis_force_n:.2f} N; belt torque {axis_torque_nm*1000:.2f} mN·m")
print(f"Ideal ADC code {ideal_force_code_n*1000:.3f} mN (not accuracy/noise)")
print(f"Simplified fixture deflection at 15 N: {deflection_m*1e6:.1f} µm")
print(f"Camera scale {pixel_scale_mm*1000:.1f} µm/px before optical errors")
print(f"24 V proposed peak: {total_power_w} W / {total_power_w/24:.1f} A; select >=8 A after margin")
print(f"Four-wire cycle estimate {cycle_s}s; no physical throughput claim")
