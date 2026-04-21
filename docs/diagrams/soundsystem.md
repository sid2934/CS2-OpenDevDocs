---
layout: default
title: "UML: soundsystem"
parent: Schemas
nav_exclude: true
---

# UML: soundsystem

Class relationships (inheritance and composition) for the `soundsystem` module.

**Arrow legend:** `<|--` inheritance &nbsp; `*--` composition &nbsp; `-->` association/pointer

```mermaid
classDiagram
    CSndSeqInstBaseSchema <|-- CSndSeqInstMidiSampler
    CSndSeqInstBaseSchema <|-- CSndSeqInstSndEvtSchema
    ISndSeqInstruments <|-- CSndSeqInstruments
    CSosGroupActionSchema <|-- CSosGroupActionLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionMemberCountEnvelopeSchema
    CSosGroupActionSchema <|-- CSosGroupActionOcclusionSchema
    CSosGroupActionSchema <|-- CSosGroupActionSetSoundeventParameterSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventClusterSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventCountSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventMinMaxValuesSchema
    CSosGroupActionSchema <|-- CSosGroupActionSoundeventPrioritySchema
    CSosGroupActionSchema <|-- CSosGroupActionTimeBlockLimitSchema
    CSosGroupActionSchema <|-- CSosGroupActionTimeLimitSchema
    CSndSeqInstBaseSchema *-- SndSeqInstrumentType_t
    CSndSeqInstBaseSchema *-- SndSeqPlayerType_t
    KeyGroup_t --> VelocityZone_t
```
