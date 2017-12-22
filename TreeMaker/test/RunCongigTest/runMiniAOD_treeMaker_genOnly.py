### NOTE, this python can not run on miniAOD, object names are for GEN-SIM, AODSIM

import FWCore.ParameterSet.Config as cms
## removed cleaning from Exo VV package 
## 

process = cms.Process('GENONLY')
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.register ('txt',
                  '/afs/cern.ch/work/b/bmaier/public/xEiko/2HDMa_gg_sinp_0p1_tanb_1_mXd_10_MH3_1000_MH4_350_MH2_1000_MHC_1000.txt',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "txt")

options.parseArguments()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)



import FWCore.Utilities.FileUtils as FileUtils
mylist = FileUtils.loadListFromFile (options.txt) 
readFiles = cms.untracked.vstring( *mylist)

process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            fileNames = readFiles
                            )



process.load('DelPanj.TreeMaker.TreeMaker_cfi')


process.tree.saveGenJets      = cms.bool(False)
process.tree.saveGenJetSub    = cms.bool(False)
process.tree.ak4GenJetLabel   = cms.InputTag("ak4GenJets")
process.tree.ak8GenJetLabel   = cms.InputTag("ak8GenJets")
process.tree.fillGenInfo      = cms.bool(True)
process.tree.fillPUweightInfo = cms.bool(False)
process.tree.fillEventInfo    = cms.bool(False)
process.tree.fillMetInfo      = cms.bool(False)
process.tree.fillTrigInfo     = cms.bool(False)
process.tree.fillFilterInfo   = cms.bool(False)
process.tree.fillElecInfo     = cms.bool(False)
process.tree.fillMuonInfo     = cms.bool(False)
process.tree.fillTauInfo      = cms.bool(False)
process.tree.fillPhotInfo     = cms.bool(False)
process.tree.fillJetInfo      = cms.bool(False) 
process.tree.fillFATJetInfo   = cms.bool(False) 
process.tree.fillAddJetInfo   = cms.bool(False)
process.tree.fillAK4PuppiJetInfo  = cms.bool(False)
process.tree.fillAK8PuppiJetInfo  = cms.bool(False)
process.tree.fillCA15PuppiJetInfo = cms.bool(False)


process.TFileService = cms.Service("TFileService",
				   fileName = cms.string(options.outputFile)          
				   )

process.analysis = cms.Path(process.tree)
