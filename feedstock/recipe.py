"""
WIP code to write a recipe for turning the seal tag csv data into a gpkg w/
apache beam + pangeo forge.

Still need to figure out how to write the transform/write steps. Pangeo-forges'
pre-defined transformations focus on e.g., reading a variable from many nc files
and then aggregating them into zarr stores.
"""
from dataclasses import dataclass, field

import apache_beam as beam
from pangeo_forge_recipes.patterns import FilePattern, FileType
from pangeo_forge_recipes.transforms import OpenURLWithFSSpec


INPUT_URL = "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f"
# We ran into a blocker here:
# This writes out to "./foo.gpkg" in the current directory because only
# zarr-specific writers support the injection of runner config like
# `c.TargetStorage.root_path`. See `pangeo-forge-runner.plugin`.
OUTPUT_PATH = "foo.gpkg"

def write_csv(pcoll):
    import pandas as pd
    import geopandas

    local_fs = pcoll[1]  # <LocalFileOpener>
    df = pd.read_csv(local_fs.f)
    geom = geopandas.points_from_xy(df.Longitude, df.Latitude)
    geo_df = geopandas.GeoDataFrame(df, geometry=geom)
    geo_df.to_file(OUTPUT_PATH, crs="EPSG:4326")

    return OUTPUT_PATH


@dataclass
class WriteCSV(beam.PTransform):
    def expand(self, pcoll):
        return pcoll | beam.Map(write_csv)


pattern = FilePattern(lambda: INPUT_URL, file_type=FileType.unknown)

recipe = (
    beam.Create(pattern.items())
    | OpenURLWithFSSpec()
    | WriteCSV()
)
