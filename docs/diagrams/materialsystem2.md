---
layout: default
title: "UML: materialsystem2"
parent: Schemas
nav_exclude: true
---

# UML: materialsystem2

Class relationships (inheritance and composition) for the `materialsystem2` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    MaterialParam_t <|-- MaterialParamBuffer_t
    MaterialParam_t <|-- MaterialParamFloat_t
    MaterialParam_t <|-- MaterialParamInt_t
    MaterialParam_t <|-- MaterialParamString_t
    MaterialParam_t <|-- MaterialParamTexture_t
    MaterialParam_t <|-- MaterialParamVector_t
```
