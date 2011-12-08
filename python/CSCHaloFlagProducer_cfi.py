import FWCore.ParameterSet.Config as cms

from TrackingTools.TrackAssociator.default_cfi import *


CSCBasedHaloFlagProducer = cms.EDProducer("CSCHaloFlagProducer",

                                        BeamHaloSummaryLabel = cms.InputTag("BeamHaloSummary"),
                                        ### Do you want to filter based on BeamHaloSummary::CSCLooseHaloId() ( ~90% eff, 1E-3 mistag rate) 
                                        FilterCSCLoose = cms.bool(False),
                                        ### Do you want to filter based on BeamHaloSummary::CSCTightHaloId() ( ~65% eff, <1E-5 mistag rate)
                                        FilterCSCTight = cms.bool(False),


                                        #############  For Use Only if FilterCSCLoose and FilterCSCTight are false
                                        #
                                        #
                                        #
                                        #
                                        
                                        ### Do you want to use L1 CSC BeamHalo Trigger to identify halo? (For < 36X, this requires the RAW-DIGI )
                                        FilterTriggerLevel = cms.bool(True),
                                        ### Do you want to use early ALCT Digis to identify halo? (requires DIGI data tier)
                                        FilterDigiLevel = cms.bool(True),
                                        ### Do you want to use halo-like CSC cosmic reconstructed tracks to identify halo?   
                                        FilterRecoLevel = cms.bool(True),
                                        
                                        # L1
                                        L1MuGMTReadoutLabel = cms.InputTag("gtDigis"),
                                        # Chamber Level Trigger Primitive
                                        ALCTDigiLabel = cms.InputTag("muonCSCDigis","MuonCSCALCTDigi"),
                                        # RecHit Level
                                        CSCRecHitLabel = cms.InputTag("csc2DRecHits"),
                                        # Higher Level Reco
                                        CSCSegmentLabel= cms.InputTag("cscSegments"),
                                        SACosmicMuonLabel= cms.InputTag("cosmicMuons"),
                                        CollisionMuonLabel = cms.InputTag("muons"),
                                        CSCHaloDataLabel = cms.InputTag("CSCHaloData"),
                                        
                                        ###### Cut Parameters
                                        ### minimum delta-eta between innermost-outermost CSC track rechit 
                                        Deta = cms.double(0.1),
                                        ### maximum delta-phi between innermost-outermost CSC track rechit 
                                        Dphi = cms.double(1.00),
                                        ### maximum Chi-Square of CSC cosmic track
                                        NormChi2  = cms.double(8.),
                                        #InnerRMin = cms.double(140.),
                                        #OuterRMin = cms.double(140.),
                                        #InnerRMax = cms.double(310.),
                                        #OuterRMax = cms.double(310.),
                                        ### minimum radius of innermost CSC cosmic track rechit
                                        InnerRMin = cms.double(0.),
                                        ### minimum radius of outermost CSC cosmic track rechit
                                        OuterRMin = cms.double(0.),
                                        ### maximum radius of innermost CSC cosmic track rechit
                                        InnerRMax = cms.double(99999.),
                                        ### maximum radius of outermost CSC cosmic track rechit
                                        OuterRMax = cms.double(99999.),
                                        ### lower edge of theta exclusion window of CSC cosmic track
                                        MinOuterMomentumTheta = cms.double(.10),
                                        ### higher edge of theta exclusion window of CSC cosmic track
                                        MaxOuterMomentumTheta = cms.double(3.0),
                                        ### maximum dr/dz calculated from innermost and outermost rechit of CSC cosmic track
                                        MaxDROverDz = cms.double(0.13),
                                        
                                        ### Phi window for matching collision muon rechits to L1 Halo Triggers
                                        MatchingDPhiThreshold = cms.double(0.18),
                                        ### Eta window for matching collision muon rechits to L1 Halo Triggers
                                        MatchingDEtaThreshold = cms.double(0.4),
                                        ### Wire window for matching collision muon rechits to earl ALCT Digis  
                                        MatchingDWireThreshold= cms.int32(5),
                                        
                                        ### Min number of L1 Halo Triggers required to call event "halo" (requires FilterTriggerLevel=True) 
                                        MinNumberOfHaloTriggers = cms.untracked.int32(1),
                                        ### Min number of early ALCT Digis required to call event "halo" (requires FilterDigiLevel =True)
                                        MinNumberOfOutOfTimeDigis = cms.untracked.int32(1),
                                        ### Min number of halo-like CSC cosmic tracks to call event "halo" (requires FilterRecoLevel =True)
                                        MinNumberOfHaloTracks = cms.untracked.int32(1),
                                        
                                        # If this is MC, the expected collision bx for ALCT Digis will be 6 instead of 3
                                        ExpectedBX = cms.int32(3),
                                        TrackAssociatorParameters = TrackAssociatorParameterBlock.TrackAssociatorParameters
                                        )


###CSC Loose Only
CSCLooseHaloFlagProducer = CSCBasedHaloFlagProducer.clone()
CSCLooseHaloFlagProducer.FilterCSCLoose = True
CSCLooseHaloFlagProducer.FilterCSCTight = False

###CSC Tight Only
CSCTightHaloFlagProducer = CSCBasedHaloFlagProducer.clone()
CSCTightHaloFlagProducer.FilterCSCLoose = False
CSCTightHaloFlagProducer.FilterCSCTight = True

###Trigger Level Only###
CSCHaloFlagProducerTriggerLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerTriggerLevel.FilterRecoLevel = False
CSCHaloFlagProducerTriggerLevel.FilterDigiLevel = False

###Reco Level Only ####
CSCHaloFlagProducerRecoLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerRecoLevel.FilterTriggerLevel = False
CSCHaloFlagProducerRecoLevel.FilterDigiLevel = False

### Digi Level Only ###
CSCHaloFlagProducerDigiLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerDigiLevel.FilterTriggerLevel = False
CSCHaloFlagProducerDigiLevel.FilterRecoLevel = False

### Reco AND Trigger Level ###
CSCHaloFlagProducerRecoAndTriggerLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerRecoAndTriggerLevel.FilterDigiLevel = False
### Digi AND Trigger Level ###
CSCHaloFlagProducerDigiAndTriggerLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerDigiAndTriggerLevel.FilterRecoLevel = False
### Digi AND Reco Level ###
CSCHaloFlagProducerDigiAndRecoLevel = CSCBasedHaloFlagProducer.clone()
CSCHaloFlagProducerDigiAndRecoLevel.FilterTriggerLevel = False

### Reco AND Digi AND Trigger Level ###  (Most Restrictive) 
CSCHaloFlagProducerRecoAndDigiAndTriggerLevel = CSCBasedHaloFlagProducer.clone()

### Sequences ####

### Reco OR Trigger Level ###
CSCHaloFlagProducerRecoOrTriggerLevel = cms.Sequence( CSCHaloFlagProducerTriggerLevel * CSCHaloFlagProducerRecoLevel )

### Digi OR Trigger Level ###
CSCHaloFlagProducerDigiOrTriggerLevel = cms.Sequence( CSCHaloFlagProducerDigiLevel * CSCHaloFlagProducerTriggerLevel )

### Digi OR Reco Level ###
CSCHaloFlagProducerDigiOrRecoLevel = cms.Sequence( CSCHaloFlagProducerDigiLevel * CSCHaloFlagProducerRecoLevel )

### Digi OR Reco OR Trigger Level ###  (Loose Selection)
CSCHaloFlagProducerDigiOrRecoOrTriggerLevel = cms.Sequence( CSCHaloFlagProducerDigiLevel * CSCHaloFlagProducerRecoLevel * CSCHaloFlagProducerTriggerLevel )
#CSCHaloFlagProducerLoose = cms.Sequence(CSCHaloFlagProducerDigiOrRecoOrTriggerLevel)

### (Digi AND Reco) OR (Digi AND Trigger) OR (Reco AND Trigger)###  (Tight Selection)
CSCHaloFlagProducer_DigiAndReco_Or_DigiAndTrigger_Or_RecoAndTrigger = cms.Sequence( CSCHaloFlagProducerRecoAndTriggerLevel *
                                                                              CSCHaloFlagProducerDigiAndTriggerLevel *
                                                                              CSCHaloFlagProducerDigiAndRecoLevel )

#CSCHaloFlagProducerTight = cms.Sequence(CSCHaloFlagProducer_DigiAndReco_Or_DigiAndTrigger_Or_RecoAndTrigger)

