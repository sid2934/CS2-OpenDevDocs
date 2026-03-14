---
layout: default
title: pulsedoc_lib
parent: Schemas
nav_exclude: true
---

# Module: pulsedoc_lib

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CPulseEditorSettings](#cpulseeditorsettings) | class |  | 0 |
| [GetVarTarget_t](#getvartarget_t) | class |  | 0 |
| [PulsePortUserVisibility_t](#pulseportuservisibility_t) | enum |  | 3 |
| [SetVarTarget_t](#setvartarget_t) | class |  | 0 |

---

### CPulseEditorSettings

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_colCanvasBackground":`, `[`, `16,`, `16,`, `16`, `],`, `"m_colCanvasBackgroundWhenDebugging":`, `[`, `45,`, `16,`, `16`, `],`, `"m_flGridSnapV2": 40.000000,`, `"m_bSnapAbsToGrid": true,`, `"m_bSnapSizeToGrid": true,`, `"m_bGridMinorPoints": true,`, `"m_flGridMinorSpacingV2": 40.000000,`, `"m_flSuppressMinorGridFurtherThan": 5000.000000,`, `"m_colGridMinorColor":`, `[`, `48,`, `48,`, `48`, `],`, `"m_flGridMinorWidth": 2.000000,`, `"m_nGridMajorMultiple": 10,`, `"m_colGridMajorColor":`, `[`, `31,`, `31,`, `31`, `],`, `"m_flGridMajorWidth": 1.500000,`, `"m_colGridOriginColor":`, `[`, `0,`, `54,`, `55`, `],`, `"m_flGridOriginWidth": 1.500000,`, `"m_nFlowTooltipBoxMargin": 4.000000,`, `"m_FontSequencePoint": "Segoe UI,8,-1,5,50,0,0,0,0,0,Regular",`, `"m_flSequencePointRadius": 21.000000,`, `"m_flSequencePointLinkWidth": 2.000000,`, `"m_colSequencePointFadeOverlay":`, `[`, `0,`, `0,`, `0,`, `200`, `],`, `"m_colSequencePointSpontaneous":`, `[`, `0,`, `255,`, `0`, `],`, `"m_colSequencePointYield":`, `[`, `255,`, `255,`, `0`, `],`, `"m_colSequencePoint":`, `[`, `128,`, `128,`, `128`, `],`, `"m_colSequencePointLink":`, `[`, `200,`, `200,`, `200`, `],`, `"m_colSequencePointLinkYield":`, `[`, `200,`, `200,`, `0`, `],`, `"m_colSequencePointName":`, `[`, `255,`, `255,`, `255`, `],`, `"m_colFlowTooltipBorder":`, `[`, `0,`, `0,`, `0`, `],`, `"m_colFlowTooltipBackground":`, `[`, `100,`, `100,`, `100`, `],`, `"m_colFlowTooltipForeground":`, `[`, `255,`, `255,`, `255`, `],`, `"m_flPortDragOffCreateThreshold": 32.000000,`, `"m_colBool":`, `[`, `142,`, `47,`, `0`, `],`, `"m_colNumber":`, `[`, `62,`, `187,`, `112`, `],`, `"m_colString":`, `[`, `0,`, `109,`, `187`, `],`, `"m_colOther":`, `[`, `156,`, `115,`, `0`, `],`, `"m_colCursorFlow":`, `[`, `140,`, `140,`, `140`, `],`, `"m_FontFlowTooltip": "Segoe UI,11,-1,5,50,0,0,0,0,0,Regular",`, `"m_FontLiteral": "Barlow,13,-1,5,75,0,0,0,0,0,Bold",`, `"m_FontDomainName": "Lucida Sans,72,-1,5,50,0,0,0,0,0,Regular",`, `"m_vDomainNameOffsetPX":`, `[`, `10.000000,`, `10.000000`, `],`, `"m_colDomainName":`, `[`, `64,`, `64,`, `64`, `],`, `"m_colDomainNameWhenDebugging":`, `[`, `128,`, `64,`, `64`, `],`, `"m_FontParentAssets": "Lucida Sans,20,-1,5,50,0,0,0,0,0,Regular",`, `"m_colParentAssets":`, `[`, `64,`, `64,`, `64`, `],`, `"m_colParentAssetsBroken":`, `[`, `255,`, `144,`, `144`, `],`, `"m_flLiteralLabelSpacing": 8.000000,`, `"m_colDebuggerBrokenBorder":`, `[`, `255,`, `144,`, `144`, `],`, `"m_DebuggerBrokenImg": "tools/images/pulse_editor/debugger_broken.png",`, `"m_DebuggerBrokenOtherImg": "tools/images/pulse_editor/debugger_broken_other.png",`, `"m_flDebuggerBrokenMarkerOffset": 2.000000,`, `"m_flDebuggerBrokenMarkerSize": 18.000000,`, `"m_DebuggerBreakpointImg": "tools/images/pulse_editor/debugger_breakpoint.png",`, `"m_DebuggerBreakpointDisabledImg": "tools/images/pulse_editor/debugger_breakpoint_disabled.png",`, `"m_flDebuggerBreakpointOffset": 2.000000,`, `"m_flDebuggerBreakpointSize": 18.000000,`, `"m_flYieldedCursorStackOffset": 8.000000,`, `"m_GraphInstanceImg": "tools/images/pulse_editor/graph_instance.png",`, `"m_flRecentExecTimeoutSec": 10.000000,`, `"m_flRecentExecStartOffset": 20.000000,`, `"m_flRecentExecEndOffset": 150.000000,`, `"m_flRecentExecLineWidth": 4.000000,`, `"m_colRecentExecStartColor":`, `[`, `150,`, `255,`, `150`, `],`, `"m_colRecentExecEndColor":`, `[`, `150,`, `255,`, `150,`, `0`, `],`, `"m_colRecentExecRequirementFailStartColor":`, `[`, `200,`, `150,`, `150`, `],`, `"m_colRecentExecRequirementFailEndColor":`, `[`, `200,`, `150,`, `150,`, `0`, `],`, `"m_flRecentExecConnectionIndicatorSize": 8.000000,`, `"m_RecentExecConnectionIndicatorImg": "tools/images/pulse_editor/connection_execution_history.png",`, `"m_bBreakOnExceptions": false,`, `"m_bShowExecutionHistory": false,`, `"m_bBoxSelectRequiresFullyContained": false,`, `"m_flFlowMinWidth": 200.000000,`, `"m_colSelectedBorder":`, `[`, `255,`, `255,`, `0`, `],`, `"m_flAppendButtonSize": 20.000000,`, `"m_colAppendHover":`, `[`, `146,`, `152,`, `153`, `],`, `"m_AppendImg": "tools/images/pulse_editor/add_to_block.png",`, `"m_flMoveChildArrowOffset": 5.000000,`, `"m_flMoveChildArrowSize": 25.000000,`, `"m_MoveChildArrowImg": "tools/images/pulse_editor/move_child.png",`, `"m_colMoveChildArrow":`, `[`, `255,`, `255,`, `255`, `],`, `"m_flConnectionTangentStrength": 100.000000,`, `"m_flConnectionCurveSpacing": 5.000000,`, `"m_flConnectionDeltaLimitScale": 0.300000,`, `"m_flBrokenConnectionOffset": 80.000000,`, `"m_flConnectionInflowOffset": 0.000000,`, `"m_flConnectionInparamOffset": 0.000000,`, `"m_flConnectionInparamOffsetArray": 4.000000,`, `"m_flConnectionCapBrokenSize": 8.000000,`, `"m_ConnectionCapBrokenImg": "tools/images/pulse_editor/connection_cap_broken.png",`, `"m_flConnectionColorLerpPercentageStart": 0.500000,`, `"m_vecBlockCommentDefaultSize":`, `[`, `200.000000,`, `200.000000`, `],`, `"m_vecBlockCommentMinSize":`, `[`, `200.000000,`, `20.000000`, `],`, `"m_colBlockCommentDefault":`, `[`, `47,`, `79,`, `79`, `],`, `"m_colBlockCommentTextLight":`, `[`, `211,`, `211,`, `211`, `],`, `"m_colBlockCommentTextDark":`, `[`, `46,`, `46,`, `46`, `],`, `"m_flBlockCommentRegionAlpha": 0.160000,`, `"m_flTimelineSeekBarHeight": 20.000000,`, `"m_flTimelinePauseIconSize": 10.000000,`, `"m_flTimelineCallModeIconSize": 18.000000,`, `"m_FontTimelineTime": "Segoe UI,11,-1,5,50,0,0,0,0,0,Regular",`, `"m_colTimelineLabel":`, `[`, `196,`, `196,`, `196`, `],`, `"m_vecTimelineIconFromPort":`, `[`, `-4.000000,`, `-19.000000`, `],`, `"m_vecTimelinePauseIconOffset":`, `[`, `-8.000000,`, `3.000000`, `],`, `"m_flTimelineCursorHeight": 12.000000,`, `"m_flTimelineCursorTextHeight": 20.000000`, `}`

### GetVarTarget_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"nVarDefID": -1,`, `"strValueEncoded": ""`, `}`

### PulsePortUserVisibility_t

**Values:**

| Name | Value |
|------|-------|
| `UNSPECIFIED` | 0 |
| `SHOW` | 1 |
| `HIDE` | 2 |

### SetVarTarget_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"nVarDefID": -1,`, `"strValueEncoded": ""`, `}`
