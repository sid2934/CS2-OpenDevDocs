---
layout: default
title: "UML: sounddoc_lib"
parent: Schemas
nav_exclude: true
---

# UML: sounddoc_lib

Class relationships (inheritance and composition) for the `sounddoc_lib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CMixPropertyBase <|-- CMixAmp
    CMixPropertyBase <|-- CMixAudioMeter
    CMixPropertyBase <|-- CMixAutoFilter
    CMixPropertyBase <|-- CMixBlendAudio
    CMixPropertyBase <|-- CMixBlendVsndsToImpulseResponse
    CMixPropertyBase <|-- CMixBoxverb
    CMixPropertyBase <|-- CMixBoxverb2
    CMixPropertyBase <|-- CMixControlAutomatic
    CMixPropertyBase <|-- CMixControlCrossfade
    CMixPropertyBase <|-- CMixControlCurve
    CMixPropertyBase <|-- CMixControlInput
    CMixPropertyBase <|-- CMixControlInputArray
    CMixPropertyBase <|-- CMixControlListener
    CMixPropertyBase <|-- CMixControlMax
    CMixPropertyBase <|-- CMixControlMeter
    CMixPropertyBase <|-- CMixControlOutput
    CMixPropertyBase <|-- CMixControlRemap
    CMixPropertyBase <|-- CMixControlStackInput
    CMixPropertyBase <|-- CMixControlTransientInput
    CMixPropertyBase <|-- CMixConvolution
    CMixPropertyBase <|-- CMixDelay
    CMixPropertyBase <|-- CMixDelayImpulseResponse
    CMixPropertyBase <|-- CMixDiffusor
    CMixPropertyBase <|-- CMixDualCompressor
    CMixPropertyBase <|-- CMixDynamics
    CMixPropertyBase <|-- CMixDynamics3Band
    CMixPropertyBase <|-- CMixDynamicsCompressor
    CMixPropertyBase <|-- CMixEQ8
    CMixPropertyBase <|-- CMixEffectChain
    CMixPropertyBase <|-- CMixEffectName
    CMixPropertyBase <|-- CMixEnvelope
    CMixPropertyBase <|-- CMixEnvelopeTrigger
    CMixPropertyBase <|-- CMixFilter
    CMixPropertyBase <|-- CMixFlanger
    CMixPropertyBase <|-- CMixFreeverb
    CMixPropertyBase <|-- CMixGroupBox
    CMixPropertyBase <|-- CMixImpulseResponseInput
    CMixPropertyBase <|-- CMixModDelay
    CMixPropertyBase <|-- CMixOsc
    CMixPropertyBase <|-- CMixOutput
    CMixPropertyBase <|-- CMixPanner
    CMixPropertyBase <|-- CMixPitchShift
    CMixPropertyBase <|-- CMixPlateverb
    CMixPropertyBase <|-- CMixPresetDSP
    CMixPropertyBase <|-- CMixRemapVsndToImpulseResponse
    CMixPropertyBase <|-- CMixShaper
    CMixPropertyBase <|-- CMixSplitter
    CMixPropertyBase <|-- CMixSplitterBlend
    CMixPropertyBase <|-- CMixSteamAudioDirect
    CMixPropertyBase <|-- CMixSteamAudioHybridReverb
    CMixPropertyBase <|-- CMixSteamAudioPathing
    CMixPropertyBase <|-- CMixSteamAudioSource
    CMixPropertyBase <|-- CMixStereoDelay
    CMixPropertyBase <|-- CMixSubgraph
    CMixPropertyBase <|-- CMixSubgraphSwitch
    CMixPropertyBase <|-- CMixSum
    CMixPropertyBase <|-- CMixTrack
    CMixPropertyBase <|-- CMixUtility
    CMixPropertyBase <|-- CMixVocoder
    CMixPropertyBase <|-- CMixVsndName
```
