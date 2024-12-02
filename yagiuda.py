# Calculator for Yagi-Uda antennae after Karl Rothammel and DL6WU

# design frequency in MHz
f_MHz = 1090.0

# diameter of reflector in mm
drefl_mm = 4

# diameter of radiator in mm
drad_mm = 4

# diameter of parasitic elements (directors) in mm
ddir_mm = 4

# number of parasitic elements (directors)
N_dir = 12

# directors are mounted through the boom as opposed to on top of the boom
dir_through = False

# diameter of boom in mm
# only relevant if directors mounted through the boom
dboom_mm = 5

######################################################
######## End of inputs, start of calculations ########
######################################################



from sys import exit

drefl = drefl_mm/1000 # diatemer of reflector
drad = drad_mm/1000   # diameter of radiator
ddir = ddir_mm/1000   # diameter of parasitic elements
dboom = dboom_mm/1000 # diameter of boom

f = f_MHz*1e6 # design frequency in Hz
c = 299792458 # speed of light
la = c/f # wave length

ratio_refl = drefl/la
ratio_rad = drad/la
ratio_dir = ddir/la

#print("Ratio of reflector diameter to wavelength: {:.5f}".format(ratio_refl))
#print("Ratio of radiator diameter to wavelength: {:.5f}".format(ratio_rad))
#print("Ratio of director diameter to wavelength: {:.5f}".format(ratio_dir))



######################################################
#### Calculation of reflector and radiator length ####
######################################################

# For the numers see Bild 24.1.3 in Rothammels Antennenbaubuch

# diameter over wave length
dola = [ 0.0010, 
         0.0012,
         0.0015,
         0.0018,
         0.0020,
         0.0025,
         0.0030,
         0.0035,
         0.0040,
         0.0050,
         0.006,
         0.007,
         0.008,
         0.009,
         0.010,
         0.012,
         0.015,
         0.018,
         0.020,
         0.025,
         0.030 ]

# reflector length over wave length 
refl_lola = [ 0.493,
              0.493,
              0.493,
              0.493,
              0.4925,
              0.4915,
              0.491,
              0.49,
              0.489,
              0.487,
              0.486,
              0.4845,
              0.483,
              0.482,
              0.481,
              0.48,
              0.477,
              0.476,
              0.475,
              0.471,
              0.4695 ]

# radiator length over wave length
rad_lola = [ 0.476,
             0.475,
             0.474,
             0.4725,
             0.4715,
             0.47,
             0.468,
             0.466,
             0.465,
             0.462,
             0.4595,
             0.457,
             0.455,
             0.453,
             0.451,
             0.449,
             0.444,
             0.4405,
             0.439,
             0.434,
             0.43 ]

# calculate points in Kurvenschar

# calculate reflector length using linear interpolation of length over wave length
length_reflector = 0
if ratio_refl < dola[0] or ratio_refl > dola[-1]:
    print("ERROR: Ratio of reflector diameter to wave length is outside the accurate range for this calculator.")
    exit()
else:
    i = 0
    while ratio_refl > dola[i]:
        i += 1
    k = (refl_lola[i]-refl_lola[i-1])/(dola[i] - dola[i-1])
    y = k * (ratio_refl-dola[i-1]) + refl_lola[i-1] # calc. lin. approx. of optimal l/la
    length_reflector = y * la
    #print("Length of reflector: {:.1f}mm".format(1000*length_reflector))
    
# calculate radiator length using linear interpolation of length over wave length
length_radiator = 0
if ratio_rad < dola[0] or ratio_rad > dola[-1]:
    print("ERROR: Ratio of radiator diameter to wave length is outside the accurate range for this calculator.")
    exit()
else:
    i = 0
    while ratio_rad > dola[i]:
        i += 1
    k = (rad_lola[i]-rad_lola[i-1])/(dola[i] - dola[i-1])
    y = k * (ratio_rad-dola[i-1]) + rad_lola[i-1] # calc. lin. approx. of optimal l/la
    length_radiator = y * la
    #print("Length of radiator: {:.1f}mm".format(1000*length_radiator))
    
    
    
######################################################
##### Calculation of length of parasitic element #####
######################################################

# table of data from Rothammel, Bild 24.1.4
# arranged as list, elements are director position
# each director position list holds l/la over d/la
dola_dir = [0.002, 0.003, 0.004, 0.005, 0.007, 0.01, 0.014]

lola_over_dola_over_pos = [
    [ 0.454,  # e.g. l/la for d/la = 0.002
      0.448,  # -----||-----  d/la = 0.003
      0.443,  # etc.
      0.439,
      0.433,
      0.426,
      0.419 ], # end of director position 1
    [ 0.451,   # begin of director position 2
      0.445,
      0.439,
      0.435,
      0.428,
      0.421,
      0.413 ],
    [ 0.447,   # position 3
      0.44,
      0.435,
      0.43,
      0.424,
      0.415,
      0.406 ],
    [ 0.444,   # position 4
      0.436,
      0.431,
      0.426,
      0.419,
      0.41,
      0.401 ],
    [ 0.44,    # position 5
      0.433,
      0.427,
      0.422,
      0.415,
      0.404,
      0.395 ],
    [ 0.437,   # position 6
      0.43,
      0.423,
      0.417,
      0.4105,
      0.4,
      0.39 ],
    [ 0.435,   # position 7
      0.426,
      0.42,
      0.414,
      0.406,
      0.396,
      0.385 ],
    [ 0.432,   # position 8
      0.423,
      0.416,
      0.411,
      0.4025,
      0.3925,
      0.382 ],
    [ 0.429,   # position 9
      0.42,
      0.414,
      0.407,
      0.399,
      0.389,
      0.378 ],
    [ 0.427,   # position 10
      0.418,
      0.412,
      0.405,
      0.396,
      0.3865,
      0.375 ],
    [ 0.426,   # position 11
      0.417,
      0.409,
      0.403,
      0.395,
      0.385,
      0.373 ],
    [ 0.424,   # position 12
      0.415,
      0.407,
      0.402,
      0.393,
      0.383,
      0.37  ],
    [ 0.423,   # position 13
      0.414,
      0.405,
      0.3995,
      0.391,
      0.381,
      0.367 ],
    [ 0.422,   # position 14
      0.412,
      0.404,
      0.397,
      0.3885,
      0.378,
      0.365 ],
    [ 0.422,   # position 15
      0.4125,
      0.404,
      0.3975,
      0.3885,
      0.378,
      0.365 ],
    [ 0.419,   # position 16
      0.409,
      0.401,
      0.394,
      0.385,
      0.375,
      0.361 ],
    [ 0.417,   # position 17
      0.407,
      0.399,
      0.392,
      0.383,
      0.373,
      0.359 ],
    [ 0.417,   # position 18
      0.407,
      0.398,
      0.39,
      0.381,
      0.37,
      0.356 ],
    [ 0.416,   # position 19
      0.405,
      0.396,
      0.388,
      0.379,
      0.368,
      0.354 ],
    [ 0.415,   # position 20
      0.4045,
      0.395,
      0.387,
      0.378,
      0.366,
      0.351 ]
]

# # Test-print the set of curves
# import matplotlib.pyplot as plt
# for lola in lola_over_dola_over_pos:
#     plt.plot(dola_dir, lola)

# Now calculate the length of each director
# Calculate a linear approximation therefore
length_of_directors = []
for pos in range(0,N_dir,1):
    if 0:
        #TODO check if number of directors and director diameter a reasonable
        exit()
    else:
        i = 0
        while ratio_dir > dola_dir[i]:
            i += 1
            if i >= len(dola_dir):
                print("ERROR: Diameter of directors too large")
                exit()
        # calc. lin. approx. of optimal director length-to-wave-length ratio
        # equation split for readability
        y1 = lola_over_dola_over_pos[pos][i-1]
        y2 = lola_over_dola_over_pos[pos][i]
        x1 = dola_dir[i-1]
        x2 = dola_dir[i]
        k = (y2-y1)/(x2-x1)
        y = k * (ratio_dir-x1) + y1
        length_dir = y * la
        length_of_directors.append(length_dir)
        #print("Length of director {}: {:.1f}mm".format(pos+1, 1000*length_dir))


        
######################################################
########## Calculation of element positions ##########
######################################################

# reflector is per def. at position 0
pos_refl = 0

# all def. distances in terms of wave length
dist_rad = 0.24
pos_rad = dist_rad * la

dist_dir = [0.075, 0.18, 0.215, 0.25, 0.28, 0.3, 0.315, 0.33, 0.345, 0.36, 
            0.375, 0.385, 0.39, 0.395, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

pos = pos_rad
pos_dir = []
for dist in dist_dir[:N_dir]:
    pos = pos + dist*la
    pos_dir.append(pos)
   
    

######################################################
################## correct for boom ##################
######################################################    

if dir_through:
    ratio_boom = dboom/la
    
    # for data see Rothammel Tabelle 24.2
    Dola = [0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05]
    cola = [0.003, 0.005, 0.008, 0.01, 0.016, 0.026, 0.035]
    
    # calculate linear approximation
    i = 0
    while ratio_boom > Dola[i]:
        i += 1
    k = (cola[i]-cola[i-1])/(Dola[i] - Dola[i-1])
    y = k * (ratio_boom - Dola[i-1]) + cola[i-1]
    
    length_reflector += y
    length_radiator += y
    length_of_directors = [length + y for length in length_of_directors]



######################################################
################### print the data ###################
######################################################    

print("Element, position in mm, length in mm")
print("Reflector: 0, {:.1f}".format(length_reflector*la*1000))
print("Radiator: {:.1f}, {:.1f}".format(pos_rad*1000,length_radiator*la*1000))
for i in range(0,N_dir,1):
    print("Director {}: {:.1f}, {:.1f}".format(i+1,pos_dir[i]*1000,length_of_directors[i]*1000))



######################################################
################## draw the antenna ##################
######################################################

import matplotlib.pyplot as plt
#draw the beam
plt.plot([0,pos_dir[-1]],[0,0],'black')

#draw the reflector
plt.plot([0,0],[-length_reflector*la/2,length_reflector*la/2],'blue')

#draw the radiator
plt.plot([pos_rad,pos_rad],[-length_radiator*la/2,length_radiator*la/2],'red')

#draw the directors
for i,pos in enumerate(pos_dir):
    x = pos
    l = length_of_directors[i]*la
    plt.plot([x,x],[-l/2,l/2],'blue')