---
layout: default
title: "UML: animlib"
parent: Schemas
nav_exclude: true
---

# UML: animlib

Class relationships (inheritance and composition) for the `animlib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CNmBlendTaskBase <|-- CNmAdditiveBlendTask
    CNmBlendTaskBase <|-- CNmBlendTask
    CNmPoseTask <|-- CNmBlendTaskBase
    CNmEvent <|-- CNmBodyGroupEvent
    CNmPoseTask <|-- CNmCachedPoseReadTask
    CNmPoseTask <|-- CNmCachedPoseWriteTask
    CNmPoseTask <|-- CNmChainLookatTask
    CNmPoseTask <|-- CNmChainSolverTask
    CNmEvent <|-- CNmEntityAttributeEventBase
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeFloatEvent
    CNmEntityAttributeEventBase <|-- CNmEntityAttributeIntEvent
    CNmEvent <|-- CNmFloatCurveEvent
    CNmPoseTask <|-- CNmFollowBoneTask
    CNmEvent <|-- CNmFootEvent
    CNmEvent <|-- CNmFrameSnapEvent
    CNmEvent <|-- CNmIDEvent
    CNmEvent <|-- CNmLegacyEvent
    CNmEvent <|-- CNmMaterialAttributeEvent
    CNmBlendTaskBase <|-- CNmModelSpaceBlendTask
    CNmEvent <|-- CNmOrientationWarpEvent
    CNmBlendTaskBase <|-- CNmOverlayBlendTask
    CNmEvent <|-- CNmParticleEvent
    CNmPoseTask <|-- CNmReferencePoseTask
    CNmEvent <|-- CNmRootMotionEvent
    CNmPoseTask <|-- CNmSampleTask
    CNmPoseTask <|-- CNmScaleTask
    CNmEvent <|-- CNmSoundEvent
    CNmEvent <|-- CNmTargetWarpEvent
    CNmEvent <|-- CNmTransitionEvent
    CNmPoseTask <|-- CNmTwoBoneIKTask
    CNmPoseTask <|-- CNmZeroPoseTask
    CNmChainSolverTask *-- CNmTarget
    CNmChainSolverTask *-- NmIKBlendMode_t
    CNmEvent *-- NmPercent_t
    CNmTwoBoneIKTask *-- CNmTarget
    CNmTwoBoneIKTask *-- NmIKBlendMode_t
```
