import FWCore.ParameterSet.Config as cms

tooManySeeds = cms.EDFilter("LogErrorEventFilter",
                              src = cms.InputTag("logErrorHarvester"),
                              maxErrorFractionInLumi = cms.double(1),
                              maxErrorFractionInRun  = cms.double(1),
                              maxSavedEventsPerLumiAndError = cms.uint32(100000),
                              categoriesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                               "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg"),
                              categoriesToWatch = cms.vstring("TooManySeeds"),
                              verbose = cms.untracked.bool(False),
                              veryVerbose  = cms.untracked.bool(False),
                              taggedMode = cms.untracked.bool(True)
                              )

tooManyClusters = cms.EDFilter("LogErrorEventFilter",
                                 src = cms.InputTag("logErrorHarvester"),
                                 maxErrorFractionInLumi = cms.double(1),
                                 maxErrorFractionInRun  = cms.double(1),
                                 maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                 categoriesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                  "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg"),
                                 categoriesToWatch = cms.vstring("TooManyClusters"),
                                 verbose = cms.untracked.bool(False),
                                 veryVerbose  = cms.untracked.bool(False),
                                 taggedMode = cms.untracked.bool(True)
                                 )

tooManyTripletsPairs = cms.EDFilter("LogErrorEventFilter",
                                    src = cms.InputTag("logErrorHarvester"),
                                    maxErrorFractionInLumi = cms.double(1.0),
                                    maxErrorFractionInRun  = cms.double(1.0),
                                    maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                    categoriesToWatch = cms.vstring("TooManyTriplets","TooManyPairs","PixelTripletHLTGenerator"),
                                    modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                  "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg"),
                                    verbose = cms.untracked.bool(False),
                                    veryVerbose  = cms.untracked.bool(False),
                                    taggedMode = cms.untracked.bool(True)
                                    )

tooManyTripletsPairsMainIterations = cms.EDFilter("LogErrorEventFilter",
                                                  src = cms.InputTag("logErrorHarvester"),
                                                  maxErrorFractionInLumi = cms.double(1.0),
                                                  maxErrorFractionInRun  = cms.double(1.0),
                                                  maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                                  categoriesToWatch = cms.vstring("TooManyTriplets","TooManyPairs","PixelTripletHLTGenerator"),
                                                  modulesToWatch = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:initialStepSeeds",
                                                                               "SeedGeneratorFromRegionHitsEDProducer:pixelPairStepSeeds"
                                                                               ),
                                                  verbose = cms.untracked.bool(False),
                                                  veryVerbose  = cms.untracked.bool(False),
                                                  taggedMode = cms.untracked.bool(True)
                                                  )

tooManySeedsMainIterations = cms.EDFilter("LogErrorEventFilter",
                                          src = cms.InputTag("logErrorHarvester"),
                                          maxErrorFractionInLumi = cms.double(1.0),
                                          maxErrorFractionInRun  = cms.double(1.0),
                                          maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                          categoriesToWatch = cms.vstring("TooManySeeds"),
                                          modulesToWatch = cms.vstring("CkfTrackCandidateMaker:initialStepTrackCandidate",
                                                                       "CkfTrackCandidateMaker:pixelPairTrackCandidate"
                                                                       ),
                                          verbose = cms.untracked.bool(False),
                                          veryVerbose  = cms.untracked.bool(False),
                                          taggedMode = cms.untracked.bool(True)
                                          )


logErrorAnalysis = cms.Sequence(tooManySeeds
                                * tooManyClusters
                                * tooManyTripletsPairs
                                * tooManyTripletsPairsMainIterations
                                * tooManySeedsMainIterations)
