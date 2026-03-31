---
layout: default
title: texturelib
parent: Schemas
nav_exclude: true
---

# Module: texturelib

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [AlphaCropAxis_t](#alphacropaxis_t) | enum |  | 3 |
| [CTextureSheetDoc](#ctexturesheetdoc) | class |  | 0 |
| [CTextureSheetDoc_Frame](#ctexturesheetdoc_frame) | class |  | 0 |
| [CTextureSheetDoc_Sequence](#ctexturesheetdoc_sequence) | class |  | 0 |
| [CTextureSheetDoc_SequenceDecalParams](#ctexturesheetdoc_sequencedecalparams) | class |  | 0 |
| [PackingMode_t](#packingmode_t) | enum |  | 3 |
| [SeqMode_t](#seqmode_t) | enum |  | 4 |
| [SequenceAlphaCropMode_t](#sequencealphacropmode_t) | enum |  | 4 |
| [SequenceChannelMode_t](#sequencechannelmode_t) | enum |  | 3 |
| [SequenceLoopMode_t](#sequenceloopmode_t) | enum |  | 3 |

---

### AlphaCropAxis_t

**Values:**

| Name | Value |
|------|-------|
| `ALPHACROP_UV` | 0 |
| `ALPHACROP_U` | 1 |
| `ALPHACROP_V` | 2 |

### CTextureSheetDoc

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_ePackingMode": "PCKM_FLAT",`, `"m_NumMips": 2,`, `"m_bHasDecalParams": false,`, `"m_sLayoutOwnerSheet": "",`, `"m_Sequences":`, `{`, `},`, `"generic_data_type": "CTextureSheetDoc"`, `}`, `MVDataRoot`, `MVDataSingleton`, `MVDataPreviewWidget = "sheet_file_preview"`, `MVDataFileExtension = "mks"`

### CTextureSheetDoc_Frame

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_sImageName": "",`, `"m_fDisplayTime": 1.000000,`, `"m_bCropEnabled": false,`, `"m_srcCropXStart": -1,`, `"m_srcCropYStart": -1,`, `"m_srcCropXEnd": -1,`, `"m_srcCropYEnd": -1`, `}`, `MPropertyAutoExpandSelf`, `MPropertyCustomEditor = "SheetSequenceFrame"`

### CTextureSheetDoc_Sequence

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_ChannelMode": "RGBA",`, `"m_LoopMode": "CLAMP",`, `"m_AlphaCropMode": "NONE",`, `"m_DecalParams":`, `{`, `"m_flScale": 1.000000,`, `"m_flDepth": 4.000000,`, `"m_flScaleVariation": 0.250000,`, `"m_flStartFadeTime": 10.000000,`, `"m_flFadeDuration": 3.000000,`, `"m_flAnimationScale": 1.000000,`, `"m_flAnimationStartTime": 0.000000,`, `"m_flAlignWithGravityFactor": 0.000000,`, `"m_nDecalRtEncoding": "kDecalInvalid"`, `},`, `"m_Frames":`, `[`, `]`, `}`

### CTextureSheetDoc_SequenceDecalParams

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_flScale": 1.000000,`, `"m_flDepth": 4.000000,`, `"m_flScaleVariation": 0.250000,`, `"m_flStartFadeTime": 10.000000,`, `"m_flFadeDuration": 3.000000,`, `"m_flAnimationScale": 1.000000,`, `"m_flAnimationStartTime": 0.000000,`, `"m_flAlignWithGravityFactor": 0.000000,`, `"m_nDecalRtEncoding": "kDecalInvalid"`, `}`, `MPropertyAutoExpandSelf`

### PackingMode_t

**Values:**

| Name | Value |
|------|-------|
| `PCKM_INVALID` | 0 |
| `PCKM_FLAT` | 1 |
| `PCKM_RGB_A` | 2 |

### SeqMode_t

**Values:**

| Name | Value |
|------|-------|
| `SQM_RGBA` | 0 |
| `SQM_RGB` | 1 |
| `SQM_ALPHA` | 2 |
| `SQM_ALPHA_INVALID` | 3 |

### SequenceAlphaCropMode_t

**Values:**

| Name | Value |
|------|-------|
| `NONE` | 0 |
| `UV` | 1 |
| `U` | 2 |
| `V` | 3 |

### SequenceChannelMode_t

**Values:**

| Name | Value |
|------|-------|
| `RGBA` | 0 |
| `RGB` | 1 |
| `ALPHA` | 2 |

### SequenceLoopMode_t

**Values:**

| Name | Value |
|------|-------|
| `CLAMP` | 0 |
| `LOOP` | 1 |
| `CLAMP_EXTEND` | 2 |
