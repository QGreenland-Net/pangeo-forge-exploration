"""
WIP code to write a recipe for turning the seal tag csv data into a gpkg w/
apache beam + pangeo forge.

Still need to figure out how to write the transform/write steps. Pangeo-forges'
pre-defined transformations focus on e.g., reading a variable from many nc files
and then aggregating them into zarr stores.
"""
import apache_beam as beam
from pangeo_forge_recipes.patterns import FilePattern, FileType
from pangeo_forge_recipes.transforms import OpenURLWithFSSpec


INPUT_URL = "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f"
OUTPUT_PATH = "foo.txt"

# from .open_pandas import OpenCsvWithPandas

# Type as pcoll containing empty dict and fsspec.localfileopener
def write_csv(pcoll):
    pcoll[1].write(OUTPUT_PATH)
    return OUTPUT_PATH


# @beam.ptransform_fn
# def WriteCsv(pcoll: beam.PCollection):
#     return beam.ParDo(lambda: 
#     ...
pattern = FilePattern(
    lambda: INPUT_URL,
    file_type=FileType.unknown,
)

recipe = (
    beam.Create(pattern.items())
    | OpenURLWithFSSpec()
    # | OpenCsvWithPandas()
    # | SomeCustomProcessing()
    # | beam.io.WriteToText("foo.txt")
    | beam.ParDo(write_csv)
)
