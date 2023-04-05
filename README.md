# Starfield
 'Simulation' of a camera flying through a field of stars

## Requirements
 - Python >= Python 3.10
 - Ursina >= 5.2.0 (previous versions will probably work, but is untested)
 - Random (built-in)
 
 Install Ursina with `pip3 install Ursina`
 
## Running
 Run `generate.py` with `python3 generate.py`. The window will automatically open.

## How it works
 Creates a default scene in Ursina and generates white spheres on a random plane. From there, all stars are continously moved towards the camera (static position). After they pass the camera or a specific z-coordinate target (max_z) they are disabled then removed. After a certain number of frames / time a random amount of stars are generated at a specified distance from the camera and the process repeats again.
