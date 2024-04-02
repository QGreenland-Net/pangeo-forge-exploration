#!/usr/bin/env bash

pangeo-forge-runner bake --repo . -f local_runner_config.py --Bake.job_name=test --prune
