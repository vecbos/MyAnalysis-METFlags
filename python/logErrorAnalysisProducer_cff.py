import FWCore.ParameterSet.Config as cms

tooManySeeds = cms.EDProducer("LogErrorAnalysis",
                              src = cms.InputTag("logErrorHarvester"),
                              maxErrorFractionInLumi = cms.double(1),
                              # if more than 20% of the events in this lumi have errors, the lumi will be excluded from the run summary (not relevant for skimming)
                              maxErrorFractionInRun  = cms.double(1),
                              # if more than 20% of the events in this run (excluding bad lumis) have errors, the run will be excluded (not relevant for skimming)
                              maxSavedEventsPerLumiAndError = cms.uint32(999999999),
                              # save events with errors but each error can get no no more than 10 events per lumi
                              ##################################
                              #categoriesToIgnore = cms.vstring("HLTConfigProvider","FastCloningDisabled"), # not concerned with some errors
                              categoriesToWatch = cms.vstring("TooManySeeds"), # not concerned with some errors
                              #you can find the error_name list at https://twiki.cern.ch/twiki/bin/view/CMS/RecoErrorsAndWarningsMeaning
                              ##################################
                              verbose = cms.untracked.bool(False), # dump summary information to stdout
                              veryVerbose  = cms.untracked.bool(False) # dump even more info to stdout
                              )

tooManyClusters = cms.EDProducer("LogErrorAnalysis",
                                 src = cms.InputTag("logErrorHarvester"),
                                 maxErrorFractionInLumi = cms.double(1),
                                 # if more than 20% of the events in this lumi have errors, the lumi will be excluded from the run summary (not relevant for skimming)
                                 maxErrorFractionInRun  = cms.double(1),
                                 # if more than 20% of the events in this run (excluding bad lumis) have errors, the run will be excluded (not relevant for skimming)
                                 maxSavedEventsPerLumiAndError = cms.uint32(999999999),
                                 # save events with errors but each error can get no no more than 10 events per lumi
                                 ##################################
                                 #categoriesToIgnore = cms.vstring("HLTConfigProvider","FastCloningDisabled"), # not concerned with some errors
                                 categoriesToWatch = cms.vstring("TooManyClusters"), # not concerned with some errors
                                 #you can find the error_name list at https://twiki.cern.ch/twiki/bin/view/CMS/RecoErrorsAndWarningsMeaning
                                 ##################################
                                 verbose = cms.untracked.bool(False), # dump summary information to stdout
                                 veryVerbose  = cms.untracked.bool(False) # dump even more info to stdout
                                 )

logErrorAnalysis = cms.Sequence(tooManySeeds * tooManyClusters)
