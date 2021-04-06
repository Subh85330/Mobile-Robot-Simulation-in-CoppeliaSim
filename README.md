# Mobile-Robot-Simulation-in-CoppeliaSim

# OBJECTIVES
1. Build a clean CAD model for 3(2 side + 1 castor) Wheeled Mobile Robot and generate the URDF using SW2URDF exporter Plugin.
2. Export the URDF to the coppeliasim simulator (Vrep).
3. Control The robot with Lua, Python and MATLAB.
4. ROS Coppeliasim Control.

## Building CAD model of wheeled mobile robot
To make the mobile robot with two side and one castor wheel make the following parts in the solidworks.

A. Body :- for body I created a cuboid shape of size 300x200x100 mm and three extend shafts of 15 mm diameter two for rear wheel and front wheel.
<img src="images/body.jpg" weidth="500" height="400"> \

B. Front wheel, wheel holder and rear wheel:- wheel is of 60 mm diameter and 15 mm hole for shaft and rear wheel has a diameter of 200 mm.
<img src="images/front wheel and holder.jpg" weidth="500" height="400"> \
C. Final Assembly:- After assembling all the parts we will get a mobile robot as shown in below figure.
<img src="images/final assembly.jpg" weidth="500" height="400">
