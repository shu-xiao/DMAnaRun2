#!/bin/bash

scriptname=`basename $0`
EXPECTED_ARGS=1
if [ $# -ne $EXPECTED_ARGS ]
then
    echo "Usage: $scriptname txtfile"
    echo "Example: ./$scriptname /afs/cern.ch/work/b/bmaier/public/xEiko/2HDMa_gg_sinp_0p35_tanb_1_mXd_10_MH3_600_MH4_200_MH2_600_MHC_600.txt"
    exit 1
fi

export PRODHOME=`pwd`
name=$1

temp=${name##*/}
outputfile=gentuple_${temp%%.txt}.root

echo ""
echo "Producing ntuples for text file "$name
echo "Producing ntuples output name "$outputfile
echo ""

bsub -q1nd $PWD/runNtuple.sh $PWD $name $outputfile




