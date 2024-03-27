"""
WIP code to write a recipe for turning the seal tag csv data into a gpkg w/
apache beam + pangeo forge.

Still need to figure out how to write the transform/write steps. Pangeo-forges'
pre-defined transformations focus on e.g., reading a variable from many nc files
and then aggregating them into zarr stores.
"""
import apache_beam as beam
from pangeo_forge_recipes.patterns import FilePattern, FileType, Index
from pangeo_forge_recipes.transforms import OpenURLWithFSSpec


INPUT_URL = "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f"
OUTPUT_PATH = "foo.txt"

class WriteCSV(beam.DoFn):
    def process(self, pcoll):
        import pandas as pd
        breakpoint()
        local_fs = pcoll[1]
        # data = pd.read_csv(local_fs.f)
        # data.write_csv(OUTPUT_PATH)
        ...

pattern = FilePattern(lambda: INPUT_URL, file_type=FileType.unknown)

recipe = (
    beam.Create(pattern.items())
    | OpenURLWithFSSpec()
    | beam.ParDo(WriteCSV())
)
