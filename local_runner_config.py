"""Config for running pangeo forge jobs locally."""

from pathlib import Path

THIS_DIR = Path(__file__).parent

c.TargetStorage.root_path = f"file://{THIS_DIR}/storage/output/{{job_name}}"
c.TargetStorage.fsspec_class = "fsspec.implementations.local.LocalFileSystem"


c.InputCacheStorage.root_path = f"file://{THIS_DIR}/storage/cache"
c.InputCacheStorage.fsspec_class = c.TargetStorage.fsspec_class

c.Bake.bakery_class = "pangeo_forge_runner.bakery.local.LocalDirectBakery"
c.LocalDirectBakery.num_workers = 4
