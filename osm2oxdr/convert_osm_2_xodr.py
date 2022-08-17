import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('134.206.154.73', 2000)
world = client.get_world()
# Read the .osm data
f = open("map_1.osm", 'r')
osm_data = f.read()
f.close()

# Define the desired settings. In this case, default values.
settings = carla.Osm2OdrSettings()
# enable traffic light generation from OSM data
settings.generate_traffic_lights = True
# Set OSM road types to export to OpenDRIVE
settings.set_osm_way_types(["pedestrian", "service", "road", "pedestrian", "motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link", "secondary", "secondary_link", "tertiary", "tertiary_link", "unclassified", "residential"])
# Convert to .xodr
xodr_data = carla.Osm2Odr.convert(osm_data, settings)

# save opendrive file
f = open("map_2.xodr", 'w')
f.write(xodr_data)
f.close()

# display the xodr map in Carla
vertex_distance = 2.0  # in meters
max_road_length = 500.0 # in meters
wall_height = 0.5      # in meters
extra_width = 0.6      # in meters
world = client.generate_opendrive_world(
    xodr_data, carla.OpendriveGenerationParameters(
        vertex_distance=vertex_distance,
        max_road_length=max_road_length,
        wall_height=wall_height,
        additional_width=extra_width,
        smooth_junctions=True,
        enable_mesh_visibility=True))

# This will show a warning and destroy vehicles when necessary
traffic_manager = client.get_trafficmanager()
traffic_manager.set_osm_mode(True)


