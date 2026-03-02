---
layout: default
title: "UML: particleslib"
parent: Schemas
nav_exclude: true
---

# UML: particleslib

Class relationships (inheritance and composition) for the `particleslib` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    IParticleEffect <|-- CNewParticleEffect
    CParticleCollectionBindingInstance <|-- CParticleBindingRealPulse
    CBasePulseGraphInstance <|-- CParticleCollectionBindingInstance
    CParticleFloatInput <|-- CParticleCollectionFloatInput
    CParticleCollectionFloatInput <|-- CParticleCollectionRendererFloatInput
    CParticleCollectionVecInput <|-- CParticleCollectionRendererVecInput
    CParticleVecInput <|-- CParticleCollectionVecInput
    CParticleInput <|-- CParticleFloatInput
    CParticleInput <|-- CParticleModelInput
    CParticleFloatInput <|-- CParticleRemapFloatInput
    CParticleInput <|-- CParticleTransformInput
    CParticleInput <|-- CParticleVecInput
    CParticleFloatInput <|-- CPerParticleFloatInput
    CParticleVecInput <|-- CPerParticleVecInput
    CNewParticleEffect --> PARTICLE_EHANDLE__
    CNewParticleEffect --> CParticleProperty
```
