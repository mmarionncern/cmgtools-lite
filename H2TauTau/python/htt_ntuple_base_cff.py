import PhysicsTools.HeppyCore.framework.config as cfg

# import all analysers:
# Heppy analyzers
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.core.EventSelector import EventSelector
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer import PileUpAnalyzer
from PhysicsTools.Heppy.analyzers.gen.GeneratorAnalyzer import GeneratorAnalyzer

# Tau-tau analyzers
from CMGTools.H2TauTau.proto.analyzers.MCWeighter import MCWeighter
from CMGTools.H2TauTau.proto.analyzers.TriggerAnalyzer import TriggerAnalyzer
from CMGTools.H2TauTau.proto.analyzers.JetAnalyzer import JetAnalyzer
from CMGTools.H2TauTau.proto.analyzers.EmbedWeighter import EmbedWeighter
from CMGTools.H2TauTau.proto.analyzers.DYJetsFakeAnalyzer import DYJetsFakeAnalyzer
from CMGTools.H2TauTau.proto.analyzers.NJetsAnalyzer import NJetsAnalyzer
from CMGTools.H2TauTau.proto.analyzers.HiggsPtWeighter import HiggsPtWeighter
from CMGTools.H2TauTau.proto.analyzers.VBFAnalyzer import VBFAnalyzer
from CMGTools.H2TauTau.proto.analyzers.RecoilCorrector import RecoilCorrector

puFileMC = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/MC_Fall15_PU25_V1.root'
puFileData = '$CMSSW_BASE/src/CMGTools/H2TauTau/data/Data_Pileup_2015D_Feb02.root'

reapplyJEC = True

eventSelector = cfg.Analyzer(
    EventSelector,
    name='EventSelector',
    toSelect=[]
)

jsonAna = cfg.Analyzer(
    JSONAnalyzer,
    name='JSONAnalyzer',
)

skimAna = cfg.Analyzer(
    SkimAnalyzerCount,
    name='SkimAnalyzerCount'
)

mcWeighter = cfg.Analyzer(
    MCWeighter,
    name='MCWeighter'
)

triggerAna = cfg.Analyzer(
    TriggerAnalyzer,
    name='TriggerAnalyzer',
    addTriggerObjects=True,
    requireTrigger=True,
    usePrescaled=False
)

vertexAna = cfg.Analyzer(
    VertexAnalyzer,
    name='VertexAnalyzer',
    fixedWeight=1,
    verbose=False
)

pileUpAna = cfg.Analyzer(
    PileUpAnalyzer,
    name='PileUpAnalyzer',
    true=True
)

genAna = GeneratorAnalyzer.defaultConfig

genAna.savePreFSRParticleIds = [1, 2, 3, 4, 5, 21]

dyJetsFakeAna = cfg.Analyzer(
    DYJetsFakeAnalyzer,
    name='DYJetsFakeAnalyzer',
    jetCol='patJetsReapplyJEC' if reapplyJEC else 'slimmedJets',
    channel='',
    genPtCut=8.
)

jetAna = cfg.Analyzer(
    JetAnalyzer,
    name='JetAnalyzer',
    jetCol='patJetsReapplyJEC' if reapplyJEC else 'slimmedJets',
    jetPt=20.,
    jetEta=4.7,
    relaxJetId=False,
    relaxPuJetId=True,
    jerCorr=False,
    #jesCorr = 1.,
    puJetIDDisc='pileupJetId:fullDiscriminant',
)

vbfAna = cfg.Analyzer(
    VBFAnalyzer,
    name='VBFAnalyzer',
    cjvPtCut=20.,
    Mjj=500.,
    deltaEta=3.5
)

recoilCorr = cfg.Analyzer(
    RecoilCorrector,
    name='RecoilCorrector'
)

embedWeighter = cfg.Analyzer(
    EmbedWeighter,
    name='EmbedWeighter',
    isRecHit=False,
    verbose=False
)

NJetsAna = cfg.Analyzer(
    NJetsAnalyzer,
    name='NJetsAnalyzer',
    fillTree=True,
    verbose=False
)

higgsWeighter = cfg.Analyzer(
    HiggsPtWeighter,
    name='HiggsPtWeighter',
)


###################################################
###                  SEQUENCE                   ###
###################################################
commonSequence = cfg.Sequence([
    jsonAna,
    skimAna,
    mcWeighter,
    triggerAna,
    vertexAna,
    genAna,
    dyJetsFakeAna,
    jetAna,
    vbfAna,
    recoilCorr,
    pileUpAna,
    embedWeighter,
    NJetsAna,
    higgsWeighter
])
