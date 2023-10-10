`docker run -it --rm -v /media:/media ubuntu:22.04 -v /var/run/docker.sock:/var/run/docker.sock -w /usr/local/bin /bin/bash`
	`/var/run/docker.sock` - default unix socket. If mounted in container you can access host's containers
		`-v /var/run/docker.sock:/var/run/docker.sock`

`apt update && apt upgrade`
`apt install vim wget curl gcc make java-1.8.0-openjdk git bzip2 autoconf libncurses5-dev zlib1g-dev`
install docker engine
```
# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl gnupg -y
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
```
	`apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y`
	`systemctl enable docker`

`wget https://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz`
`tar xf Python-2.7.3.tgz`
`cd Python-2.7.3`
`export PYTHON_VERSION=2.7.3`
`export PYTHON_MAJOR=2`
``` bash
./configure \
    --prefix=/opt/python/${PYTHON_VERSION} \
    --enable-shared \
    --enable-optimizations \
    --enable-ipv6 \
    LDFLAGS=-Wl,-rpath=/opt/python/${PYTHON_VERSION}/lib,--disable-new-dtags
```
`make`
`make install`
`export PATH=/opt/python/Python-2.7.3/bin/:$PATH`

`wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh`
`bash Anaconda3-2023.09-0-Linux-x86_64.sh`
`. ~/.bashrc`

`conda config --add channels defaults`
`conda config --add channels bioconda`
`conda config --add channels conda-forge`
`conda create -n TEST3 python=2.7.3 scipy numpy`
`conda create -n TEST3 python=2.7 scipy numpy`

GATK v3.6
`wget https://github.com/broadgsa/gatk-protected/archive/refs/tags/3.6.tar.gz`
`tar xf 3.6.tar.gz`
NIE ma GenomeAnalysisTK.jar :<
odpal dockera z kontenera-.-
	docker run --rm ba0dfa08ea63 java -jar GenomeAnalysisTK.jar

samtools
	`bzip2 -d samtools-1.3.1.tar.bz2
	`tar xf samtools-1.3.1.tar`
	`cd samtools-1.3.1`
	`autoheader`
	`autoconf -Wno-syntax`
	`./configure `
	`make`
	`make install`






`/var/run/docker.sock` - default unix socket. If mounted in container you can access host's containers
	`-v /var/run/docker.sock:/var/run/docker.sock`

```
python rMATS-DVR.py --sample1 S1_rep_1.bam[,S1_rep_2.bam][,...,S1_rep_n.bam] --sample2 S2_rep_1.bam[,S2_rep_2.bam][,...,S2_rep_n.bam] --label S1,S2 --genome hg19.fa --output /Path/to/output/S1_vs_S2 [--known dbSNP147.vcf] [--editing RADAR2.txt] [--repeat repeats.txt] [--gene RefSeq.txt] [--minQ 20] [--minDP 5] [--thread 1] [--diff 0.0001] [--merge] [--ReadStranded] [--ReadPaired] [--skipBamCalibration] [--KeepTemp]
```