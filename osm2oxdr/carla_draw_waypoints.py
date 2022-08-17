import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('134.206.154.73', 2000)
world = client.get_world()
map = world.get_map()

# Draw waypoints in Carla and print them in the terminal
waypoints = map.generate_waypoints(2)
for w in waypoints:
    print(w)
    world.debug.draw_string(w.transform.location, 'O', draw_shadow=False,
                                       color=carla.Color(r=255, g=0, b=0), life_time=1200, 
                                       persistent_lines=True)


