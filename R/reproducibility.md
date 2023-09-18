`.libPaths()` - list libraries (dirs with packages)


## renv
package for R programming language that provides a project-specific environment management system

create reproducible projects and to manage dependencies of projects

`renv` - lockfile dla metadanych pakietów projektu
`renv::init()` - create new library for new project
	1. `renv::create()`
	2. `pak::pkg_install(...)`
	3. `renv::snapshot()` - create `renv.lock`
		`renv::history` & `renv::revert` navigate prior versions of lock files
	4. `renv::restore()`


## pak
[`pak`](https://github.com/r-lib/pak) - `install.packages()` alternative. Use CRAN, Bioconductor, git, URLs, local files

`install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))` - installation (or `install.packages("pak")` from CRAN)

`pak::pkg_install('ggplot2')`