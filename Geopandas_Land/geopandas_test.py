import polars as pl
import geopandas
import geodatasets
import json


path_to_data = geodatasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)

gdf
## health, health_indicators
# print(json.dumps(geodatasets.data, indent=4))