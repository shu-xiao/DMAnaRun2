import os

## check if file exist then ask if you want to delete old one and create new one. 
## if answer is yes then deelte the old and create this one new. 
fout = open("datasetdetails_Summer16.txt","w")
## each line will contain four parameters. 
## taskname   cfg.py  datasetname  numberofdiles
## cfg.py is configurable because data and MC will have different configurations.
## And number of files canbe used as number of lumis in that case. 

## Moriond MC

fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")

fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM 1 \n")

fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-950_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-550_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-50_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p5_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p5_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-500_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2500_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-5_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-200_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-2000_MChi2-1_MChi1-0p1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-1_MChi1-0p1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-5_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-5_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1500_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-10_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-1_MChi1-0p1_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-8_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-5_ctau-1000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-100_MChi2-10_MChi1-1_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p8_ctau-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p8_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p5_ctau-1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")
fout.write("MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph treeMaker_Summer16_cfg.py /MonoHbb_ZpBaryonic_MZp-1000_MChi2-1_MChi1-0p5_ctau-100000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 1 \n")


fout.close()


def submit():
    print "submitting"
    f = open('datasetdetails_Summer16.txt','r')
    for line in f:
        print line
        a=[]
        b=[]
        c=[]
        d=[]
        a,b,c,d = line.split()
        datasetdetail=[a,b,c,d]
        print datasetdetail
        os.system('crab submit General.requestName='+datasetdetail[0]+' JobType.psetName='+datasetdetail[1]+' Data.inputDataset='+datasetdetail[2]+' Data.unitsPerJob='+datasetdetail[3])
    #name =  'crab submit General.requestName='+datasetdetail[0]+' JobType.psetName='+datasetdetail[1]+' Data.inputDataset='+datasetdetail[2]+' Data.unitsPerJob='+datasetdetail[3]
    #print name 
        
        



def status(crabdirname):
    import os
    os.system ("./Statusall.sh "+crabdirname)
    

## Add a help or usage function here 
def help() :
    print "this is under progress"

    


####################################################################################################################################################
####################################################################################################################################################
## this will control the functions   ##
## convert this to python main.      ##
####################################################################################################################################################
####################################################################################################################################################
import os
import sys
print sys.argv


## safety check
## improve this
if len(sys.argv) < 2 :
    print "insufficient options provided see help function "
    help()
    exit (1)


## submit jobs 
if len(sys.argv) == 2 :
    if sys.argv[1] == "submit" :
        submit()


## check status of jobs 
## send the crab directory 
if len(sys.argv) == 3 : 
    if sys.argv[1] == "status" :
        crabdir = sys.argv[2]
        status(crabdir)




