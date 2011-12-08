
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/JetReco/interface/Jet.h"


class TrackingFailureFlagProducer : public edm::EDProducer {

  public:

    explicit TrackingFailureFlagProducer(const edm::ParameterSet & iConfig);
    ~TrackingFailureFlagProducer() {}

  private:

    virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);
    
    edm::InputTag jetSrc_, trackSrc_, vertexSrc_;
    double dzTrVtxMax_, dxyTrVtxMax_;
    double minSumPtOverHT_;

};


TrackingFailureFlagProducer::TrackingFailureFlagProducer(const edm::ParameterSet & iConfig) {
  jetSrc_         = iConfig.getParameter<edm::InputTag>("JetSource");
  trackSrc_       = iConfig.getParameter<edm::InputTag>("TrackSource");
  vertexSrc_      = iConfig.getParameter<edm::InputTag>("VertexSource");
  dzTrVtxMax_     = iConfig.getParameter<double>("DzTrVtxMax");
  dxyTrVtxMax_    = iConfig.getParameter<double>("DxyTrVtxMax");
  minSumPtOverHT_ = iConfig.getParameter<double>("MinSumPtOverHT");
  produces<bool>();
}


void TrackingFailureFlagProducer::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {

  bool pass = false;

  edm::Handle<edm::View<reco::Jet> > jets;
  iEvent.getByLabel(jetSrc_, jets);
  edm::Handle<std::vector<reco::Track> > tracks;
  iEvent.getByLabel(trackSrc_, tracks);
  edm::Handle<std::vector<reco::Vertex> > vtxs;
  iEvent.getByLabel(vertexSrc_, vtxs);

  double ht = 0;
  for (edm::View<reco::Jet>::const_iterator j = jets->begin(); j != jets->end(); ++j) {
    ht += j->pt();
  }
  double sumpt = 0;
  if (vtxs->size() > 0) {
    const reco::Vertex * vtx = &((*vtxs)[0]);
    for (std::vector<reco::Track>::const_iterator tr = tracks->begin(); tr != tracks->end(); ++tr) {
      if (fabs(tr->dz(vtx->position())) > dzTrVtxMax_) continue;
      if (fabs(tr->dxy(vtx->position())) > dxyTrVtxMax_) continue;
      sumpt += tr->pt();
    }
  }
  if ((sumpt/ht) < minSumPtOverHT_)
    std::cout << "TRACKING FAILURE: "
              << iEvent.id().run() << " : " << iEvent.id().luminosityBlock() << " : " << iEvent.id().event()
              << " HT=" << ht
              << " SumPt=" << sumpt
              << std::endl;

  pass = ((sumpt/ht) > minSumPtOverHT_);

  std::auto_ptr<bool> pOut( new bool(pass) );
  iEvent.put( pOut );

}


#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(TrackingFailureFlagProducer);
