---
layout: default
title: steamaudio
parent: Schemas
nav_exclude: true
---

# Module: steamaudio

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CSteamAudioAmbisonicsField](#csteamaudioambisonicsfield) | class |  | 0 |
| [CSteamAudioBakedDimensionsData](#csteamaudiobakeddimensionsdata) | class |  | 0 |
| [CSteamAudioBakedMaterialsData](#csteamaudiobakedmaterialsdata) | class |  | 0 |
| [CSteamAudioBakedOcclusionData](#csteamaudiobakedocclusiondata) | class |  | 0 |
| [CSteamAudioBakedPathingData](#csteamaudiobakedpathingdata) | class |  | 0 |
| [CSteamAudioBakedReverbData](#csteamaudiobakedreverbdata) | class |  | 0 |
| [CSteamAudioCompressedReverb](#csteamaudiocompressedreverb) | class |  | 0 |
| [CSteamAudioProbeData](#csteamaudioprobedata) | class |  | 0 |
| [CSteamAudioProbeGrid](#csteamaudioprobegrid) | class |  | 0 |
| [CSteamAudioProbeLineSegment](#csteamaudioprobelinesegment) | class |  | 0 |
| [SteamAudioCustomDataDimensionsSettings_t](#steamaudiocustomdatadimensionssettings_t) | class |  | 0 |
| [SteamAudioCustomDataOcclusionSettings_t](#steamaudiocustomdataocclusionsettings_t) | class |  | 0 |
| [SteamAudioPathSettings_t](#steamaudiopathsettings_t) | class |  | 0 |
| [SteamAudioReverbClusteringSettings_t](#steamaudioreverbclusteringsettings_t) | class |  | 0 |
| [SteamAudioReverbCompressionSettings_t](#steamaudioreverbcompressionsettings_t) | class |  | 0 |
| [SteamAudioReverbSettings_t](#steamaudioreverbsettings_t) | class |  | 0 |

---

### CSteamAudioAmbisonicsField

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_field":`, `[`, `]`, `}`

### CSteamAudioBakedDimensionsData

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_settings":`, `{`, `"m_nAmbisonicsOrderOutsideField": 0,`, `"m_nAmbisonicsOrderInsideSizeField": 0,`, `"m_flOutsideThreshold": 0.000000,`, `"m_flSizeThreshold": 0.000000,`, `"m_flInsideThreshold": 0.000000`, `},`, `"m_probes":`, `{`, `},`, `"m_vecInOut":`, `[`, `],`, `"m_vecSize":`, `[`, `],`, `"m_vecOutsideField":`, `[`, `],`, `"m_vecInsideSmallSizeField":`, `[`, `],`, `"m_movables":`, `{`, `"m_vecData":`, `[`, `],`, `"m_vecInitialTransforms":`, `[`, `],`, `"m_vecAABBs":`, `[`, `],`, `"m_vecKeys":`, `[`, `]`, `}`, `}`

### CSteamAudioBakedMaterialsData

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_probes":`, `{`, `},`, `"m_vecMaterialTokens":`, `[`, `],`, `"m_vecMaterialWeights":`, `[`, `]`, `}`

### CSteamAudioBakedOcclusionData

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_settings":`, `{`, `"m_bEnablePathing": false,`, `"m_bEnableReflections": false,`, `"m_nReflectionRays": 0,`, `"m_nReflectionBounces": 0`, `},`, `"m_probes":`, `{`, `},`, `"m_vecPathingRatio":`, `[`, `],`, `"m_vecPathingDeviation":`, `[`, `],`, `"m_vecReflectionRatio":`, `[`, `]`, `}`

### CSteamAudioBakedPathingData

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nBands": 3,`, `"m_probes":`, `{`, `},`, `"m_movables":`, `{`, `"m_vecData":`, `[`, `],`, `"m_vecInitialTransforms":`, `[`, `],`, `"m_vecAABBs":`, `[`, `],`, `"m_vecKeys":`, `[`, `]`, `}`, `}`

### CSteamAudioBakedReverbData

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nBands": 3,`, `"m_grid":`, `{`, `"m_aabb":`, `{`, `"m_vMinBounds":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `],`, `"m_vMaxBounds":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `]`, `},`, `"m_flSpacing": 0.000000,`, `"m_nx": 0,`, `"m_ny": 0,`, `"m_nz": 0,`, `"m_vecLineSegments":`, `[`, `],`, `"m_vecProbes":`, `[`, `]`, `},`, `"m_reverbSettings":`, `{`, `"m_nNumRays": 0,`, `"m_nNumBounces": 0,`, `"m_flIRDuration": 0.000000,`, `"m_nAmbisonicsOrder": 0`, `},`, `"m_reverbClusteringSettings":`, `{`, `"m_bEnableClustering": false,`, `"m_nCubeMapResolution": 0,`, `"m_flDepthThreshold": 0.000000`, `},`, `"m_reverbCompressionSettings":`, `{`, `"m_bEnableCompression": false,`, `"m_flQuality": 0.950000`, `},`, `"m_vecClusterForProbe":`, `[`, `],`, `"m_compressedData":`, `{`, `"m_nChannels": 0,`, `"m_nBands": 0,`, `"m_nBins": 0,`, `"m_nProbes": 0,`, `"m_vecNumSingularValues":`, `[`, `],`, `"m_vecDictionary":`, `[`, `],`, `"m_vecCompressedData":`, `[`, `]`, `},`, `"m_compressedClusteredData":`, `{`, `"m_nChannels": 0,`, `"m_nBands": 0,`, `"m_nBins": 0,`, `"m_nProbes": 0,`, `"m_vecNumSingularValues":`, `[`, `],`, `"m_vecDictionary":`, `[`, `],`, `"m_vecCompressedData":`, `[`, `]`, `},`, `"m_movables":`, `{`, `"m_vecData":`, `[`, `],`, `"m_vecInitialTransforms":`, `[`, `],`, `"m_vecAABBs":`, `[`, `],`, `"m_vecKeys":`, `[`, `]`, `}`, `}`

### CSteamAudioCompressedReverb

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nChannels": 0,`, `"m_nBands": 0,`, `"m_nBins": 0,`, `"m_nProbes": 0,`, `"m_vecNumSingularValues":`, `[`, `],`, `"m_vecDictionary":`, `[`, `],`, `"m_vecCompressedData":`, `[`, `]`, `}`

### CSteamAudioProbeData

**Metadata:** `MGetKV3ClassDefaults = {`, `}`

### CSteamAudioProbeGrid

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_aabb":`, `{`, `"m_vMinBounds":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `],`, `"m_vMaxBounds":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `]`, `},`, `"m_flSpacing": 0.000000,`, `"m_nx": 0,`, `"m_ny": 0,`, `"m_nz": 0,`, `"m_vecLineSegments":`, `[`, `],`, `"m_vecProbes":`, `[`, `]`, `}`

### CSteamAudioProbeLineSegment

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_vStart":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `],`, `"m_vEnd":`, `[`, `0.000000,`, `0.000000,`, `0.000000`, `],`, `"m_vecIntervals":`, `[`, `],`, `"m_vecProbeIndices":`, `[`, `]`, `}`

### SteamAudioCustomDataDimensionsSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nAmbisonicsOrderOutsideField": 0,`, `"m_nAmbisonicsOrderInsideSizeField": 0,`, `"m_flOutsideThreshold": 0.000000,`, `"m_flSizeThreshold": 0.000000,`, `"m_flInsideThreshold": 0.000000`, `}`

### SteamAudioCustomDataOcclusionSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_bEnablePathing": false,`, `"m_bEnableReflections": false,`, `"m_nReflectionRays": 0,`, `"m_nReflectionBounces": 0`, `}`

### SteamAudioPathSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nNumVisSamples": 0,`, `"m_flProbeVisRadius": 0.000000,`, `"m_flProbeVisThreshold": 0.000000,`, `"m_flProbePathRange": 0.000000`, `}`

### SteamAudioReverbClusteringSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_bEnableClustering": false,`, `"m_nCubeMapResolution": 0,`, `"m_flDepthThreshold": 0.000000`, `}`

### SteamAudioReverbCompressionSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_bEnableCompression": false,`, `"m_flQuality": 0.950000`, `}`

### SteamAudioReverbSettings_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nNumRays": 0,`, `"m_nNumBounces": 0,`, `"m_flIRDuration": 0.000000,`, `"m_nAmbisonicsOrder": 0`, `}`
