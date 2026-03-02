---
layout: default
title: mathlib_extended
parent: Schemas
nav_exclude: true
---

# Module: mathlib_extended

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [AABB_t](#aabb_t) | class |  | 2 |
| [CFuseProgram](#cfuseprogram) | class |  | 0 |
| [CFuseSymbolTable](#cfusesymboltable) | class |  | 0 |
| [ConstantInfo_t](#constantinfo_t) | class |  | 0 |
| [FourQuaternions](#fourquaternions) | class |  | 4 |
| [FunctionInfo_t](#functioninfo_t) | class |  | 0 |
| [FuseFunctionIndex_t](#fusefunctionindex_t) | class |  | 1 |
| [FuseVariableAccess_t](#fusevariableaccess_t) | enum |  | 2 |
| [FuseVariableIndex_t](#fusevariableindex_t) | class |  | 1 |
| [FuseVariableType_t](#fusevariabletype_t) | enum |  | 9 |
| [PackedAABB_t](#packedaabb_t) | class |  | 2 |
| [VariableInfo_t](#variableinfo_t) | class |  | 0 |

---

### AABB_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_vMinBounds` | Vector | `MNetworkEnable` |
| `m_vMaxBounds` | Vector | `MNetworkEnable` |

### CFuseProgram

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_programBuffer":`, `[`, `],`, `"m_variablesRead":`, `[`, `],`, `"m_variablesWritten":`, `[`, `],`, `"m_nMaxTempVarsUsed": 0`, `}`

### CFuseSymbolTable

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_constants":`, `[`, `],`, `"m_variables":`, `[`, `],`, `"m_functions":`, `[`, `],`, `"m_constantMap":`, `{`, `},`, `"m_variableMap":`, `{`, `},`, `"m_functionMap":`, `{`, `}`, `}`

### ConstantInfo_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_name": "",`, `"m_nameToken": "",`, `"m_flValue": 0.000000`, `}`

### FourQuaternions

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `x` | fltx4 |  |
| `y` | fltx4 |  |
| `z` | fltx4 |  |
| `w` | fltx4 |  |

### FunctionInfo_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_name": "",`, `"m_nameToken": "",`, `"m_nParamCount": 0,`, `"m_nIndex": 65535,`, `"m_bIsPure": false`, `}`

### FuseFunctionIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint16 |  |

### FuseVariableAccess_t

**Values:**

| Name | Value |
|------|-------|
| `WRITABLE` | 0 |
| `READ_ONLY` | 1 |

### FuseVariableIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint16 |  |

### FuseVariableType_t

**Values:**

| Name | Value |
|------|-------|
| `INVALID` | 0 |
| `BOOL` | 1 |
| `INT8` | 2 |
| `INT16` | 3 |
| `INT32` | 4 |
| `UINT8` | 5 |
| `UINT16` | 6 |
| `UINT32` | 7 |
| `FLOAT32` | 8 |

### PackedAABB_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_nPackedMin` | uint32 |  |
| `m_nPackedMax` | uint32 |  |

### VariableInfo_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_name": "",`, `"m_nameToken": "",`, `"m_nIndex": 65535,`, `"m_nNumComponents": 1,`, `"m_eVarType": "INVALID",`, `"m_eAccess": "WRITABLE"`, `}`
