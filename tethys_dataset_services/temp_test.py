import os
from engines import GeoServerSpatialDatasetEngine

# Create Engine
engine = GeoServerSpatialDatasetEngine(endpoint='http://192.168.59.103:8181/geoserver/rest',
                                       username='admin',
                                       password='geoserver')

# UPDATE
# updated_resource = engine.update_resource(resource_id='roads',
#                                           enabled=True,
#                                           title='Even more spearfish roads',
#                                           debug=True)

# updated_layer = engine.update_layer(layer_id='roads',
#                                     default_style='simple_roads',
#                                     styles=['line'],
#                                     debug=True)

# updated_layer_group = engine.update_layer_group(layer_group_id='tasmania',
#                                                 layers=['tasmania_state_boundaries', 'tasmania_water_bodies',
#                                                         'tasmania_roads', 'tasmania_cities', 'roads'],
#                                                 styles=['green', 'cite_lakes', 'simple_roads', 'capitals',
#                                                         'simple_roads'],
#                                                 debug=True)



# DELETE
# engine.delete_layer_group(layer_group_id='my_layer_group', debug=True)
# engine.delete_layer(layer_id='my_layer', recurse=True, debug=True) # Check recurse (deletes layer group as well).
# engine.delete_layer(layer_id='my_layer', debug=True)
# engine.delete_resource(resource_id='Pk50095', recurse=True, debug=True)  # Belongs to layer
# engine.delete_resource(resource_id='bob', debug=True)  # Does not exist

# CREATE
# engine.get_layer_group('my_layer_group', debug=True)

# Layer Group
# layers = ('poi', 'tiger_roads')
# styles = ('line', 'line')
# bounds = ('-74.02722', '-73.907005', '40.684221', '40.878178', 'EPSG:4326')
# engine.create_layer_group('my_layer_group', layers=layers, styles=styles, bounds=bounds, debug=True)

# Shapefile Layer
shapefile_base = "/Users/swainn/projects/tethysdev/tethys_dataset_services/tethys_dataset_services/tests/files/shapefile/bugsites"  # Test both base and zip archive methods
# engine.create_shapefile_resource('cite:foo', shapefile_dir=shapefile_base, overwrite=True, debug=True)  # Handle overwrite in tests
# shapefile_base = "/Users/swainn/projects/tethysdev/tethys_dataset_services/tethys_dataset_services/tests/files/shapefile/bar.zip"
# engine.create_shapefile_resource('cite:bar', shapefile_base=shapefile_base, overwrite=True, debug=True)
engine.create_shapefile_resource('bar', shapefile_base=shapefile_base, overwrite=True, debug=True)



# SERVICES



