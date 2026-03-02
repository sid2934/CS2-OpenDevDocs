---
layout: default
title: resourcefile
parent: Schemas
nav_exclude: true
---

# Module: resourcefile

[📊 View UML Diagram](../diagrams/resourcefile.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CExampleSchemaVData_Monomorphic](#cexampleschemavdata_monomorphic) | class |  | 0 |
| [CExampleSchemaVData_PolymorphicBase](#cexampleschemavdata_polymorphicbase) | class |  | 0 |
| [CExampleSchemaVData_PolymorphicDerivedA](#cexampleschemavdata_polymorphicderiveda) | class | CExampleSchemaVData_PolymorphicBase | 0 |
| [CExampleSchemaVData_PolymorphicDerivedB](#cexampleschemavdata_polymorphicderivedb) | class | CExampleSchemaVData_PolymorphicBase | 0 |
| [InfoForResourceTypeCResourceManifestInternal](#infoforresourcetypecresourcemanifestinternal) | class |  | 0 |
| [ResourceId_t](#resourceid_t) | class |  | 1 |

---

### CExampleSchemaVData_Monomorphic

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nExample1": 5,`, `"m_nExample2": 5`, `}`

### CExampleSchemaVData_PolymorphicBase

**Derived by:** [CExampleSchemaVData_PolymorphicDerivedA](resourcefile.md#cexampleschemavdata_polymorphicderiveda), [CExampleSchemaVData_PolymorphicDerivedB](resourcefile.md#cexampleschemavdata_polymorphicderivedb)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CExampleSchemaVData_PolymorphicBase",`, `"m_nBase": 5`, `}`

**Relationships:**

```mermaid
classDiagram
    CExampleSchemaVData_PolymorphicBase <|-- CExampleSchemaVData_PolymorphicDerivedA
    CExampleSchemaVData_PolymorphicBase <|-- CExampleSchemaVData_PolymorphicDerivedB
```

### CExampleSchemaVData_PolymorphicDerivedA

**Inherits from:** [CExampleSchemaVData_PolymorphicBase](resourcefile.md#cexampleschemavdata_polymorphicbase)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CExampleSchemaVData_PolymorphicDerivedA",`, `"m_nBase": 5,`, `"m_nDerivedA": 5`, `}`

**Relationships:**

```mermaid
classDiagram
    CExampleSchemaVData_PolymorphicBase <|-- CExampleSchemaVData_PolymorphicDerivedA
```

### CExampleSchemaVData_PolymorphicDerivedB

**Inherits from:** [CExampleSchemaVData_PolymorphicBase](resourcefile.md#cexampleschemavdata_polymorphicbase)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CExampleSchemaVData_PolymorphicDerivedB",`, `"m_nBase": 5,`, `"m_nDerivedB": 5`, `}`

**Relationships:**

```mermaid
classDiagram
    CExampleSchemaVData_PolymorphicBase <|-- CExampleSchemaVData_PolymorphicDerivedB
```

### InfoForResourceTypeCResourceManifestInternal

**Metadata:** `MResourceTypeForInfoType = "vrman"`

### ResourceId_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint64 |  |
