"""
WIP code to write a recipe for turning the seal tag csv data into a gpkg w/
apache beam + pangeo forge.

Still need to figure out how to write the transform/write steps. Pangeo-forges'
pre-defined transformations focus on e.g., reading a variable from many nc files
and then aggregating them into zarr stores.
"""
import apache_beam as beam
from pangeo_forge_recipes.patterns import FilePattern


# In pangeo-forge, this function would normally take arguments corresponding to
# the variables specified by a `MergeDim` instance. We're just fetching a single
# csv file.
def make_full_path():
    return "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f"


pattern = FilePattern(make_full_path)
for index, fname in pattern.items():
    print(index, fname)

recipe = beam.Create(pattern.items())
