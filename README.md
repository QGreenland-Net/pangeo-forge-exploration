# pangeo-forge-exploration

This repository contains notes and code to explore the use of
[pangeo-forge](https://pangeo-forge.readthedocs.io/en/latest/).


## Custom writers

Custom writers are currently a challenge being worked on in Pangeo Forge. While it looks
straightforward to create a custom writer, there is special logic that injects the
output directory (`target_root`) to writers based on a hard-coded data structure of
classes to receive injection. We reached out for support and were recommended to pursue
the following workaround (thank you, Greg!):

1. Fork `pangeo-forge-recipes`, add custom writer `PTransform` to e.g. `transforms.py`.
2. Ensure the new transform has a special argument based on this
   [example custom writer class](https://github.com/pangeo-forge/pangeo-forge-recipes/blob/gc/ndpyramid_final/pangeo_forge_recipes/transforms.py#L757-L759).
3. In the fork, update `injections.py` to add our new `PTransform` to the static data
   structure.
4. In recipe repository, update `requirements.txt` to point to the forked
   `pangeo-forge-runner` instead of the official following `git+https://github.com/...`
   notation.


Some examples:

* Example w/o pangeo-forge-runner:
  https://github.com/pangeo-forge/staged-recipes/blob/gpm_pyramid/recipes/gpm/feedstock/recipe.py#L174-L212
* Similar example in pangeo-forge-recipe tests:
  https://github.com/pangeo-forge/pangeo-forge-recipes/blob/main/tests/test_end_to_end.py#L218-L231


### What about a monkeypatch approach so my custom transform can live with my recipe?

This approach is ruled out because the injection happens prior to runtime.

The dependency injection approach is currently being revisited. _TODO: Link to GitHub
issues/discussions where this is happening!*
