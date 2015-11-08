
# DMAnaRun2

# For CMSSW_7_4_15
```
setenv SCRAM_ARCH slc6_amd64_gcc491
cmsrel CMSSW_7_4_15
cd CMSSW_7_4_15/src/
cmsenv
```

## For double-b-tagger
```
setenv CMSSW_GIT_REFERENCE /cvmfs/cms.cern.ch/cmssw.git.daily 
git cms-init 
git remote add btv-cmssw https://github.com/cms-btv-pog/cmssw.git 
git fetch --tags btv-cmssw
git cms-merge-topic cms-btv-pog:BoostedDoubleSVTaggerV2-WithWeightFiles-v1_from-CMSSW_7_4_15 
```

## For Egamma to get Spring15 ID
```
git cms-merge-topic ikrav:egm_id_7.4.12_v1
```


## For DelPanj and related dependencies

```
git clone git@github.com:syuvivida/DMAnaRun2.git DelPanj

cd DelPanj

git checkout doublebtagger

cd -

git clone git@github.com:syuvivida/DMAnaRun2_AddModules.git AddModules

mv AddModules/EGamma/ .

rm -rf AddModules
```

## Compile And Run 
```
scramv1 b clean

scramv1 b
```

## Download JEC files

```
mv DelPanj/jec/Summer15_25nsV2_MC_* .
mv DelPanj/jec/Summer15_25nsV5_DATA_* .
cmsRun DelPanj/TreeMaker/test/RunCongigTest/treeMaker_Spring15_Nocleaning_cfg.py
 
```
