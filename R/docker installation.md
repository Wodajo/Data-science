`docker run --name rstudio --restart=always -v ~/github/projects/:/home/rstudio/projects/ -e PASSWORD=yourpassword123 -dp 8899:8787 rocker/ml`
	Rstudio with CUDA
	rstudio/yourpassword - initial creds

`docker commit -a "Ultrabob Master " -m "added pak&renv" 88ffebedcbc2 ml:pak_renv`
`docker run --name rstudio --restart=always -v /:/twardovsky -e PASSWORD=password -dp 8899:8787 ml:pak_renv`