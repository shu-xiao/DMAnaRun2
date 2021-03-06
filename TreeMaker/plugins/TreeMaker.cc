// -*- C++ -*-
//
// Package:    TreeMaker
// Class:      TreeMaker
// Original Author:  Anil Singh, Ashok Kumar, Shin-Shan Yu, Raman Khurana, Yun-Ju Lu
//                   Panjab University, Delhi University
//                   National Central University
//         Created:  Tue Jul  6 21:04:59 CEST 2010
//


// system include files
#include <memory>
#include <string>

#include "DelPanj/TreeMaker/interface/TreeMaker.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
TreeMaker::TreeMaker(const edm::ParameterSet& iConfig)

{
  fillPUweightInfo_=false;
  fillEventInfo_   =false;
  fillMetInfo_     =false;
  fillTrigInfo_    =false;
  fillFilterInfo_  =false;

  fillGenInfo_     =false;
  fillElecInfo_    =false;
  fillMuonInfo_    =false;
  fillTauInfo_     =false;
  fillPhotInfo_    =false; 
  fillJetInfo_     =false;
  fillFATJetInfo_  =false;
  fillAddJetInfo_  =false;


  fillPUweightInfo_ = iConfig.getParameter<bool>("fillPUweightInfo");
  fillEventInfo_    = iConfig.getParameter<bool>("fillEventInfo");
  fillMetInfo_      = iConfig.getParameter<bool>("fillMetInfo");
  fillTrigInfo_     = iConfig.getParameter<bool>("fillTrigInfo");
  fillFilterInfo_   = iConfig.getParameter<bool>("fillFilterInfo");
  fillGenInfo_      = iConfig.getParameter<bool>("fillGenInfo");
  fillElecInfo_     = iConfig.getParameter<bool>("fillElecInfo");
  fillMuonInfo_     = iConfig.getParameter<bool>("fillMuonInfo");
  fillTauInfo_      = iConfig.getParameter<bool>("fillTauInfo");
  fillPhotInfo_     = iConfig.getParameter<bool>("fillPhotInfo");
  fillJetInfo_      = iConfig.getParameter<bool>("fillJetInfo");
  fillFATJetInfo_   = iConfig.getParameter<bool>("fillFATJetInfo"); 
  fillAddJetInfo_   = iConfig.getParameter<bool>("fillAddJetInfo");
   
  
  edm::Service<TFileService> fs;


  tree_ = fs->make<TTree>("treeMaker","tree");
  if( fillPUweightInfo_) 
    {
      puweight_                   = new puweight("pu_",tree_);
      puweight_->puInfoToken      = consumes<std::vector<PileupSummaryInfo>>(edm::InputTag("slimmedAddPileupInfo"));
    }

  if( fillEventInfo_ ) 
    {
      eventInfo_                  = new eventInfo("",tree_); 
      eventInfo_->vertexToken     = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
    }


  if( fillMetInfo_ )
    {
      patMetTree_                 = new patMetTree("pf",tree_);
      patMetTree_->pfMETRawToken  = consumes<reco::PFMETCollection>(iConfig.getParameter<edm::InputTag>("pfMetRaw"));
      patMetTree_->pfMETToken     = consumes<pat::METCollection>(iConfig.getParameter<edm::InputTag>("pfType1Met"));
      // patMetTree_->pfMVAMETToken  = consumes<reco::PFMETCollection>(iConfig.getParameter<edm::InputTag>("pfMVAMET"));                                                        
    }


  if( fillTrigInfo_ )
    {
      patHltTree_                             = new patHltTree("hlt_",tree_); 
      patHltTree_->trigResultsToken           = consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerLabel"));
      patHltTree_->triggerPrescalesToken      = consumes<pat::PackedTriggerPrescales>(edm::InputTag("patTrigger"));
	
    }
  if( fillFilterInfo_ ) 
    {
      patFilterTree_                          = new patFilters("hlt_",tree_); 
      patFilterTree_->HBHETToken              = consumes<bool>(edm::InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight","MVAMET"));
      patFilterTree_->HBHELToken              = consumes<bool>(edm::InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose","MVAMET"));
      patFilterTree_->HBHEIsoToken            = consumes<bool>(edm::InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult","MVAMET"));
      patFilterTree_->filterTrigResultsToken  = consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("filterLabel"));
    }

  if( fillGenInfo_ ) 
    {
      genInfoTree_                           = new genInfoTree("",tree_,iConfig);
      genInfoTree_->genParticleToken         = consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("genPartLabel"));
      genInfoTree_->genEventToken            = consumes<GenEventInfoProduct>(edm::InputTag("generator"));
      genInfoTree_->lheRunToken              = consumes<LHERunInfoProduct,edm::InRun>(edm::InputTag("externalLHEProducer"));
      genInfoTree_->lheEventToken            = consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"));
    }
  
  if( fillElecInfo_ )
    {
      patElecTree_                              = new patElecTree("",tree_,iConfig);
      patElecTree_->vertexToken                 = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
      patElecTree_->rhoForLepToken              = consumes<double>(edm::InputTag("fixedGridRhoFastjetCentralNeutral"));
      patElecTree_->eleToken                    = consumes<edm::View<pat::Electron>>(iConfig.getParameter<edm::InputTag>("eleLabel"));
      patElecTree_->pfCandToken                 = consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfForMiniIso"));

      patElecTree_->eleVetoIdMapToken           = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleVetoIdMap"));
      patElecTree_->eleLooseIdMapToken          = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleLooseIdMap"));
      patElecTree_->eleMediumIdMapToken         = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleMediumIdMap"));
      patElecTree_->eleTightIdMapToken          = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleTightIdMap"));
      patElecTree_->eleHEEPIdMapToken           = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleHEEPIdMap"));

      patElecTree_->eleVetoIdCFToken            = consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("eleVetoIdMap"));
      patElecTree_->eleLooseIdCFToken           = consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("eleLooseIdMap"));
      patElecTree_->eleMediumIdCFToken          = consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("eleMediumIdMap"));
      patElecTree_->eleTightIdCFToken           = consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("eleTightIdMap"));
      patElecTree_->eleHEEPIdCFToken            = consumes<edm::ValueMap<vid::CutFlowResult>>(iConfig.getParameter<edm::InputTag>("eleHEEPIdMap"));
      
      patElecTree_->eleMVAMediumIdMapToken      = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleMVAMediumIdMap"));
      patElecTree_->eleMVATightIdMapToken       = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("eleMVATightIdMap"));
      patElecTree_->mvaValuesMapToken           = consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("mvaValuesMap"));
      patElecTree_->mvaCategoriesMapToken       = consumes<edm::ValueMap<int>>(iConfig.getParameter<edm::InputTag>("mvaCategoriesMap"));

    }

  if( fillMuonInfo_ ) 
    {
      patMuTree_                             = new patMuonTree("",tree_,iConfig);
      patMuTree_->vertexToken                = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
      patMuTree_->rhoForLepToken             = consumes<double>(edm::InputTag("fixedGridRhoFastjetCentralNeutral"));
      patMuTree_->muToken                    = consumes<pat::MuonCollection>(iConfig.getParameter<edm::InputTag>("muoLabel"));
      patMuTree_->pfCandToken                = consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfForMiniIso"));
    }

  if( fillTauInfo_ ) 
    {
      tauTree_                               = new hpstauInfo("",tree_, false);
      tauTree_->tauToken                     = consumes<pat::TauCollection>(iConfig.getUntrackedParameter<edm::InputTag> ("tauLabel"));
      tauTree_->theBeamSpotToken             = consumes<reco::BeamSpot>(edm::InputTag("offlineBeamSpot"));
    }

  if( fillPhotInfo_)
    {
      photonTree_                                 = new photonTree("", tree_); 
      photonTree_->photonToken                    = consumes<edm::View<pat::Photon>>(iConfig.getParameter<edm::InputTag> ("photonLabel"));
      photonTree_->phoLooseIdMapToken             = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("phoLooseIdMap"));
      photonTree_->phoMediumIdMapToken            = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("phoMediumIdMap"));
      photonTree_->phoTightIdMapToken             = consumes<edm::ValueMap<bool>>(iConfig.getParameter<edm::InputTag>("phoTightIdMap"));
      photonTree_->phoMVAValuesMapToken           = consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("phoMVAValuesMapToken"));
      photonTree_->phoChargedIsolationToken       = consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("phoChargedIsolationToken"));
      photonTree_->phoNeutralHadronIsolationToken = consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("phoNeutralHadronIsolationToken"));
      photonTree_->phoPhotonIsolationToken        = consumes<edm::ValueMap<float>>(iConfig.getParameter<edm::InputTag>("phoPhotonIsolationToken"));
    }

  if( fillJetInfo_ )
    {
      std::string desc             = "THIN";
      THINjetTree_                 = new jetTree(desc,tree_,iConfig);
      THINjetTree_->jetToken       = consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>(Form("%sJets",desc.data())));
      THINjetTree_->vertexToken    = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
      THINjetTree_->rhoForJetToken = consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"));
    }

  if( fillFATJetInfo_ )
    {
      std::string desc            = "FAT";
      FATjetTree_                 = new jetTree(desc,tree_,iConfig);
      FATjetTree_->jetToken       = consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>(Form("%sJets",desc.data())));
      FATjetTree_->vertexToken    = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
      FATjetTree_->rhoForJetToken = consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"));
      FATjetTree_->prunedMToken   = consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>(Form("%sJetsForPrunedMass",desc.data())));
      FATjetTree_->softdropMToken   = consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>(Form("%sJetsForSoftDropMass",desc.data())));
    }

  if( fillAddJetInfo_)
    {
      std::string desc            = "ADD";
      ADDjetTree_                 = new jetTree(desc,tree_,iConfig);
      ADDjetTree_->jetToken       = consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>(Form("%sJets",desc.data())));
      ADDjetTree_->vertexToken    = consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("pvSrc"));
      ADDjetTree_->rhoForJetToken = consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"));

    }

  
  
}


TreeMaker::~TreeMaker()
{
  //delete tree_;
}

void
TreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  using namespace edm;

  if( fillPUweightInfo_ ) puweight_      ->Fill(iEvent);
  if( fillEventInfo_ )    eventInfo_     ->Fill(iEvent);
  if( fillMetInfo_ )      patMetTree_    ->Fill(iEvent);
  if( fillTrigInfo_ )     patHltTree_    ->Fill(iEvent);
  if( fillFilterInfo_ )   patFilterTree_ ->Fill(iEvent);

  if( fillGenInfo_ )      genInfoTree_   ->Fill(iEvent);
  if( fillElecInfo_ )     patElecTree_   ->Fill(iEvent);
  if( fillMuonInfo_ )     patMuTree_     ->Fill(iEvent);
  if( fillTauInfo_ )      tauTree_       ->Fill(iEvent, iSetup);
  if( fillPhotInfo_ )     photonTree_    ->Fill(iEvent);

  if( fillFATJetInfo_ )   FATjetTree_    ->Fill(iEvent, iSetup);
  if( fillJetInfo_ )      THINjetTree_   ->Fill(iEvent, iSetup);
  if( fillAddJetInfo_ )   ADDjetTree_    ->Fill(iEvent, iSetup);  
 
  tree_->Fill();
}


void
TreeMaker::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) {
  
}

void
TreeMaker::endRun(const edm::Run& iRun, const edm::EventSetup& iSetup){

  if( fillGenInfo_ )
    genInfoTree_   ->GetRunInfo(iRun);

}

void
TreeMaker::beginJob(){
}



void
TreeMaker::endJob() {

}

DEFINE_FWK_MODULE(TreeMaker);
