`.libPaths()` - list libraries (dirs with packages)

## renv
package for R programming language that provides a project-specific environment management system

`renv::init()` - create 3 new files&dirs
	`renv/library` - contains all packages currently used by your project (soft links to cache)
	`renv.lock` - records enough metadata about every package that it can be re-installed on a new machine. 
	`.Rprofile` - run automatically every time you start R (in that project), and renv uses it to configure your R session to use the project library

`pak::pkg_install(...)`
`renv::snapshot()` - update `renv.lock`
`renv::restore()` - use `renv.lock` to restore (install) packages in exact same version
`renv::history` & `renv::revert` navigate prior versions of lock files

Cache powinien miec osobną, montowalą do contenerów lokalizację.
`renv::paths$cache()` - shows current cache
Można podać ścieżkę podczas odpalania kontenera
```
1# the location of the renv cache on the host machine
RENV_PATHS_CACHE_HOST=/opt/local/renv/cache

# where the cache should be mounted in the container
RENV_PATHS_CACHE_CONTAINER=/renv/cache

# run the container with the host cache mounted in the container
docker run --rm \
    -e "RENV_PATHS_CACHE=${RENV_PATHS_CACHE_CONTAINER}" \
    -v "${RENV_PATHS_CACHE_HOST}:${RENV_PATHS_CACHE_CONTAINER}" \
    -p 14618:14618 \
    R -s -e 'renv::restore(); shiny::runApp(host = "0.0.0.0", port = 14618)'
```
or export `RENV_PATHS_CACHE` via `Renviron.site` (R installation's site-wide) during docker image building
## pak
[`pak`](https://github.com/r-lib/pak) - `install.packages()` alternative. Use CRAN, Bioconductor, git, URLs, local files

`install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))` - installation (or `install.packages("pak")` from CRAN)

`pak::pkg_install('ggplot2')`