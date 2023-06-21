# main generation
import stars as st
import random
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.scripts.noclip_mode import *

# this relies on the Ursina Game Engine (library)

# MAX feasible distance is around 1024 (this is a poor term for it, but things past that are pretty far out and 'twinkle')
# Max -x = 378
# Max y = 260
# X : -378 -> 378
# Y : -260 -> 260

frame_counter = 0
max_z = 15
stars = []

def generate_stars(num_stars: int, d1: int, d2: int):
    for i in range(num_stars):
        stars.append(st.Star(random.randrange(-380, 380), random.randrange(-260, 260), random.randrange(d1, d2)))

def update():
    global frame_counter
    global stars
    bad_stars = []
    for i, star in enumerate(stars):
        (x, y, z) = star.get_pos()
        #print(x, y, z) # DEBUG PRINT
        z -= 1
        star.set_pos(x, y, z)
        if (z <= max_z):
            bad_stars.append(i)
            star.e.enabled = False

    stars = [star for i, star in enumerate(stars) if i not in bad_stars]

    if frame_counter > 200:
        frame_counter = 0
        print('num stars:', len(stars)) # DEBUG PRINT
        generate_stars(random.randrange(30, 100), 1200, 2000)

    frame_counter += 1

def main():
    app = st.Ursina(borderless=False, size=(1200, 700))
    print('Main')
    st.window.color = st.color.black
    generate_stars(300, 50, 800)
    #camera=Entity()
    #camera.add_script(FirstPersonController())
    app.run()

if __name__ == '__main__':
    main()
