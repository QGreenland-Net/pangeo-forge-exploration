"""
WIP code to write a recipe for turning the seal tag csv data into a gpkg w/
apache beam + pangeo forge.

Still need to figure out how to write the transform/write steps. Pangeo-forges'
pre-defined transformations focus on e.g., reading a variable from many nc files
and then aggregating them into zarr stores.
"""
from dataclasses import dataclass

import apache_beam as beam
from pangeo_forge_recipes.patterns import FilePattern
import pandas as pd


# In pangeo-forge, this function would normally take arguments corresponding to
# the variables specified by a `MergeDim` instance. We're just fetching a single
# csv file.
def make_full_path():
    return "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A31162eb9-7e3b-4b88-948f-f4c99f13a83f"


# Note: stolen/adapted from `pangeo_forge_recipes.openers`
def open_with_pandas(
    url_or_file_obj,
):
    """Open item with Pandas. Accepts either fsspec open-file-like objects
    or string URLs that can be passed directly to Xarray.

    :param url_or_file_obj: The url or file object to be opened.
    :param file_type: Provide this if you know what type of file it is.
    :param load: Whether to eagerly load the data into memory ofter opening.
    :param copy_to_local: Whether to copy the file-like-object to a local path
       and pass the path to Xarray. Required for some file types (e.g. Grib).
       Can only be used with file-like-objects, not URLs.
    :xarray_open_kwargs: Extra arguments to pass to Xarray's open function.
    """
    # TODO: fetch the data from the remote source? Or use
    # https://filesystem-spec.readthedocs.io/en/latest/?badge=latest?
    filepath = ...
    ds = pd.read_csv(filepath, **kw)

    return ds


# Note: stolen/adapted from `pangeo_forge_recipes.transforms`
@dataclass
class OpenCsvWithPandas(beam.PTransform):
    """Open indexed items with Pandas. Accepts either fsspec open-file-like objects
    or string URLs that can be passed directly to Xarray.
    """

    def expand(self, pcoll):
        return pcoll | "Open with Pandas" >> beam.MapTuple(
            lambda k, v: (
                k,
                open_with_pandas(
                    v,
                    file_type=self.file_type,
                    load=self.load,
                    copy_to_local=self.copy_to_local,
                    xarray_open_kwargs=self.xarray_open_kwargs,
                ),
            )
        )


pattern = FilePattern(make_full_path)
for index, fname in pattern.items():
    print(index, fname)

recipe = beam.Create(pattern.items())
