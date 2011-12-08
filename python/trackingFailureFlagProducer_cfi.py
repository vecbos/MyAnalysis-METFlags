
import FWCore.ParameterSet.Config as cms

trackingFailureFlagProducer = cms.EDProducer(
  "TrackingFailureFlagProducer",
  JetSource = cms.InputTag('ak5PFJets'),
  TrackSource = cms.InputTag('generalTracks'),
  VertexSource = cms.InputTag('offlinePrimaryVertices'),
  DzTrVtxMax = cms.double(1),
  DxyTrVtxMax = cms.double(0.2),
  MinSumPtOverHT = cms.double(0.10)
)
