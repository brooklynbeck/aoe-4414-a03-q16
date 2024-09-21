# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# Text explaining script usage
# Parameters:
# o_lat_deg: observatory latitude in degrees
# o_lon_deg: observatory longitude in degrees
# o_hae_km: observatory height above the reference ellipsoid in km
# s_km: south SEZ coordinate of satellite
# e_km: east SEZ coordinate of satellite
# z_km: alitude SEZ coordinate of satellite
# Output:
# Prints x, y, and z components of ECEF in km
#
# Written by Brooklyn Beck
# Other contributors: None
#
# import Python modules
import math # math module
import sys # argv
# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
## calculated denominator
def calc_denom(ecc,lat_rad):
  return math.sqrt(1.0-ecc**2*math.sin(lat_rad)**2)

# initialize script arguments
o_lat_deg = float('nan') #see parameters above for descriptions
o_lon_deg = float('nan')
o_hae_km = float('nan')
s_km = float('nan')
e_km = float('nan')
z_km = float('nan')
# parse script arguments
if len(sys.argv)==7:
  o_lat_deg = float(sys.argv[1])
  o_lon_deg = float(sys.argv[2])
  o_hae_km = float(sys.argv[3])
  s_km = float(sys.argv[4])
  e_km = float(sys.argv[5])
  z_km = float(sys.argv[6])
else:
  print(\
  'Usage: '\
  'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
  )
  exit()
# write script below this line
o_lat_rad = o_lat_deg * math.pi/180.0
o_lon_rad = o_lon_deg * math.pi/180.0

#calculate ecef vector
ecef_x_vec = math.cos(o_lon_rad)*math.sin(o_lat_rad)*s_km + math.cos(o_lon_rad)*math.cos(o_lat_rad)*z_km - math.sin(o_lon_rad)*e_km
ecef_y_vec = math.sin(o_lon_rad)*math.sin(o_lat_rad)*s_km + math.sin(o_lon_rad)*math.cos(o_lat_rad)*z_km + math.cos(o_lon_rad)*e_km
ecef_z_vec = -1*math.cos(o_lat_rad)*s_km + math.sin(o_lat_rad)*z_km

#calculate intermediary values
denom = calc_denom(E_E, o_lat_rad)
C_E = R_E_KM / denom
S_E = R_E_KM * (1.0-E_E**2)/denom

#calculate ecef origin
origin_x = (C_E + o_hae_km)*math.cos(o_lat_rad)*math.cos(o_lon_rad)
origin_y = (C_E + o_hae_km)*math.cos(o_lat_rad)*math.sin(o_lon_rad)
origin_z = (S_E + o_hae_km)*math.sin(o_lat_rad)

#add origin to vector
ecef_x_km = ecef_x_vec + origin_x
ecef_y_km = ecef_y_vec + origin_y
ecef_z_km = ecef_z_vec + origin_z

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
