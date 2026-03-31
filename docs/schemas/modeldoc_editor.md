---
layout: default
title: modeldoc_editor
parent: Schemas
nav_exclude: true
---

# Module: modeldoc_editor

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CMotionAnalysisSettings](#cmotionanalysissettings) | class |  | 0 |
| [CMotionAnalysisSettings_Foot](#cmotionanalysissettings_foot) | class |  | 0 |
| [DuplicateAndMirrorAttachmentOpts_t](#duplicateandmirrorattachmentopts_t) | class |  | 0 |
| [MirrorSpace_t](#mirrorspace_t) | enum |  | 2 |

---

### CMotionAnalysisSettings

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Description": "",`, `"m_flLinearThresholdSlow": 60.000000,`, `"m_flLinearThresholdStopped": 25.000000,`, `"m_flAngularThresholdSlow": 90.000000,`, `"m_flAngularThresholdStopped": 15.000000,`, `"m_Feet":`, `{`, `}`, `}`, `MVDataRoot`

### CMotionAnalysisSettings_Foot

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_AnkleBoneNames":`, `[`, `],`, `"m_AttachmentNames":`, `[`, `],`, `"m_DebugColor":`, `[`, `255,`, `255,`, `255`, `],`, `"m_CreatedEventType": "AE_FOOTSTEP",`, `"m_CreatedEventFootValue": ""`, `}`

### DuplicateAndMirrorAttachmentOpts_t

**Metadata:** `MPropertyElementNameFn (UNKNOWN FOR PARSER)`, `MGetKV3ClassDefaults = {`, `"m_Name": "Duplicate And Mirror Attachment Options",`, `"m_eMirrorSpace": "MIRROR_SPACE_MODEL_RELATIVE",`, `"m_bSwapLeftRightParentBones": false,`, `"m_bMirrorX": false,`, `"m_bMirrorY": true,`, `"m_bMirrorZ": false`, `}`, `MPropertyDescription = "Options for duplicating and mirroring attachments."`

### MirrorSpace_t

**Values:**

| Name | Value |
|------|-------|
| `MIRROR_SPACE_BONE_RELATIVE` | 0 |
| `MIRROR_SPACE_MODEL_RELATIVE` | 1 |
