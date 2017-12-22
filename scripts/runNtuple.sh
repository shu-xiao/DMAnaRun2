#!/bin/sh

echo $1
cd $1
export SCRAM_ARCH=slc6_amd64_gcc530; eval `scramv1 runtime -sh`
export X509_USER_PROXY=$HOME/private/grid.proxy

cmsRun runMiniAOD_treeMaker_genOnly.py txt=$2 outputFile=$3
