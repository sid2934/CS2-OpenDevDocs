---
layout: default
title: pulse_runtime_lib
parent: Schemas
nav_exclude: true
---

# Module: pulse_runtime_lib

[📊 View UML Diagram](../diagrams/pulse_runtime_lib.md)

| Name | Kind | Bases | Fields |
|------|------|-------|--------|
| [CBasePulseGraphInstance](#cbasepulsegraphinstance) | class |  | 0 |
| [CPulseArraylib](#cpulsearraylib) | class |  | 0 |
| [CPulseCell_Base](#cpulsecell_base) | class |  | 0 |
| [CPulseCell_BaseFlow](#cpulsecell_baseflow) | class | CPulseCell_Base | 0 |
| [CPulseCell_BaseLerp](#cpulsecell_baselerp) | class | CPulseCell_BaseYieldingInflow | 1 |
| [CPulseCell_BaseLerp](#cpulsecell_baselerp) | class |  | 0 |
| [CPulseCell_BaseRequirement](#cpulsecell_baserequirement) | class | CPulseCell_Base | 0 |
| [CPulseCell_BaseState](#cpulsecell_basestate) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_BaseValue](#cpulsecell_basevalue) | class | CPulseCell_Base | 0 |
| [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_BooleanSwitchState](#cpulsecell_booleanswitchstate) | class | CPulseCell_BaseState | 0 |
| [CPulseCell_CursorQueue](#cpulsecell_cursorqueue) | class | CPulseCell_WaitForCursorsWithTagBase | 0 |
| [CPulseCell_FireCursors](#cpulsecell_firecursors) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Inflow_EntOutputHandler](#cpulsecell_inflow_entoutputhandler) | class | CPulseCell_Inflow_BaseEntrypoint | 0 |
| [CPulseCell_Inflow_EventHandler](#cpulsecell_inflow_eventhandler) | class | CPulseCell_Inflow_BaseEntrypoint | 0 |
| [CPulseCell_Inflow_GraphHook](#cpulsecell_inflow_graphhook) | class | CPulseCell_Inflow_BaseEntrypoint | 0 |
| [CPulseCell_Inflow_Method](#cpulsecell_inflow_method) | class | CPulseCell_Inflow_BaseEntrypoint | 0 |
| [CPulseCell_Inflow_ObservableVariableListener](#cpulsecell_inflow_observablevariablelistener) | class | CPulseCell_Inflow_BaseEntrypoint | 0 |
| [CPulseCell_Inflow_Wait](#cpulsecell_inflow_wait) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_Inflow_Yield](#cpulsecell_inflow_yield) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_InlineNodeSkipSelector](#cpulsecell_inlinenodeskipselector) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_IntervalTimer](#cpulsecell_intervaltimer) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_IntervalTimer](#cpulsecell_intervaltimer) | class |  | 0 |
| [CPulseCell_IsRequirementValid](#cpulsecell_isrequirementvalid) | class | CPulseCell_BaseRequirement | 0 |
| [CPulseCell_IsRequirementValid](#cpulsecell_isrequirementvalid) | class |  | 1 |
| [CPulseCell_LimitCount](#cpulsecell_limitcount) | class | CPulseCell_BaseRequirement | 0 |
| [CPulseCell_LimitCount](#cpulsecell_limitcount) | class |  | 1 |
| [CPulseCell_LimitCount](#cpulsecell_limitcount) | class |  | 0 |
| [CPulseCell_Outflow_CycleOrdered](#cpulsecell_outflow_cycleordered) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Outflow_CycleOrdered](#cpulsecell_outflow_cycleordered) | class |  | 0 |
| [CPulseCell_Outflow_CycleRandom](#cpulsecell_outflow_cyclerandom) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Outflow_CycleShuffled](#cpulsecell_outflow_cycleshuffled) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Outflow_CycleShuffled](#cpulsecell_outflow_cycleshuffled) | class |  | 0 |
| [CPulseCell_PickBestOutflowSelector](#cpulsecell_pickbestoutflowselector) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Step_CallExternalMethod](#cpulsecell_step_callexternalmethod) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_Step_DebugLog](#cpulsecell_step_debuglog) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Step_PublicOutput](#cpulsecell_step_publicoutput) | class | CPulseCell_BaseFlow | 0 |
| [CPulseCell_Timeline](#cpulsecell_timeline) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_Timeline](#cpulsecell_timeline) | class |  | 0 |
| [CPulseCell_Unknown](#cpulsecell_unknown) | class | CPulseCell_Base | 1 |
| [CPulseCell_Value_Curve](#cpulsecell_value_curve) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_Value_Gradient](#cpulsecell_value_gradient) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_Value_RandomFloat](#cpulsecell_value_randomfloat) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_Value_RandomInt](#cpulsecell_value_randomint) | class | CPulseCell_BaseValue | 0 |
| [CPulseCell_WaitForCursorsWithTag](#cpulsecell_waitforcursorswithtag) | class | CPulseCell_WaitForCursorsWithTagBase | 0 |
| [CPulseCell_WaitForCursorsWithTagBase](#cpulsecell_waitforcursorswithtagbase) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCell_WaitForCursorsWithTagBase](#cpulsecell_waitforcursorswithtagbase) | class |  | 1 |
| [CPulseCell_WaitForObservable](#cpulsecell_waitforobservable) | class | CPulseCell_BaseYieldingInflow | 0 |
| [CPulseCursorFuncs](#cpulsecursorfuncs) | class |  | 0 |
| [CPulseExecCursor](#cpulseexeccursor) | class |  | 0 |
| [CPulseGraphDef](#cpulsegraphdef) | class |  | 0 |
| [CPulseGraphExecutionHistory](#cpulsegraphexecutionhistory) | class |  | 0 |
| [CPulseMathlib](#cpulsemathlib) | class |  | 0 |
| [CPulseRuntimeMethodArg](#cpulseruntimemethodarg) | class |  | 0 |
| [CPulseTestScriptLib](#cpulsetestscriptlib) | class |  | 0 |
| [CPulse_BlackboardReference](#cpulse_blackboardreference) | class |  | 0 |
| [CPulse_CallInfo](#cpulse_callinfo) | class |  | 0 |
| [CPulse_Chunk](#cpulse_chunk) | class |  | 0 |
| [CPulse_Constant](#cpulse_constant) | class |  | 0 |
| [CPulse_DomainValue](#cpulse_domainvalue) | class |  | 0 |
| [CPulse_InstructionDebug](#cpulse_instructiondebug) | class |  | 0 |
| [CPulse_InvokeBinding](#cpulse_invokebinding) | class |  | 0 |
| [CPulse_OutflowConnection](#cpulse_outflowconnection) | class |  | 4 |
| [CPulse_OutputConnection](#cpulse_outputconnection) | class |  | 0 |
| [CPulse_PublicOutput](#cpulse_publicoutput) | class |  | 0 |
| [CPulse_RegisterInfo](#cpulse_registerinfo) | class |  | 0 |
| [CPulse_ResumePoint](#cpulse_resumepoint) | class | CPulse_OutflowConnection | 0 |
| [CPulse_Variable](#cpulse_variable) | class |  | 0 |
| [EPulseGraphExecutionHistoryFlag](#epulsegraphexecutionhistoryflag) | enum |  | 6 |
| [OutflowWithRequirements_t](#outflowwithrequirements_t) | class |  | 0 |
| [PGDInstruction_t](#pgdinstruction_t) | class |  | 0 |
| [PulseApiFeature_t](#pulseapifeature_t) | enum |  | 6 |
| [PulseBestOutflowRules_t](#pulsebestoutflowrules_t) | enum |  | 2 |
| [PulseCursorCancelPriority_t](#pulsecursorcancelpriority_t) | enum |  | 4 |
| [PulseCursorExecResult_t](#pulsecursorexecresult_t) | enum |  | 4 |
| [PulseCursorID_t](#pulsecursorid_t) | class |  | 1 |
| [PulseCursorYieldToken_t](#pulsecursoryieldtoken_t) | class |  | 1 |
| [PulseDocNodeID_t](#pulsedocnodeid_t) | class |  | 1 |
| [PulseDomainValueType_t](#pulsedomainvaluetype_t) | enum |  | 4 |
| [PulseGraphExecutionHistoryCursorDesc_t](#pulsegraphexecutionhistorycursordesc_t) | class |  | 0 |
| [PulseGraphExecutionHistoryEntry_t](#pulsegraphexecutionhistoryentry_t) | class |  | 0 |
| [PulseGraphExecutionHistoryNodeDesc_t](#pulsegraphexecutionhistorynodedesc_t) | class |  | 0 |
| [PulseGraphInstanceID_t](#pulsegraphinstanceid_t) | class |  | 1 |
| [PulseInstructionCode_t](#pulseinstructioncode_t) | enum |  | 125 |
| [PulseMethodCallMode_t](#pulsemethodcallmode_t) | enum |  | 2 |
| [PulseNodeDynamicOutflows_t](#pulsenodedynamicoutflows_t) | class |  | 0 |
| [PulseNodeDynamicOutflows_t](#pulsenodedynamicoutflows_t) | class |  | 0 |
| [PulseObservableBoolExpression_t](#pulseobservableboolexpression_t) | class |  | 0 |
| [PulseRegisterMap_t](#pulseregistermap_t) | class |  | 3 |
| [PulseRuntimeBlackboardReferenceIndex_t](#pulseruntimeblackboardreferenceindex_t) | class |  | 1 |
| [PulseRuntimeCallInfoIndex_t](#pulseruntimecallinfoindex_t) | class |  | 1 |
| [PulseRuntimeCellIndex_t](#pulseruntimecellindex_t) | class |  | 1 |
| [PulseRuntimeChunkIndex_t](#pulseruntimechunkindex_t) | class |  | 1 |
| [PulseRuntimeConstantIndex_t](#pulseruntimeconstantindex_t) | class |  | 1 |
| [PulseRuntimeDomainValueIndex_t](#pulseruntimedomainvalueindex_t) | class |  | 1 |
| [PulseRuntimeEntrypointIndex_t](#pulseruntimeentrypointindex_t) | class |  | 1 |
| [PulseRuntimeInvokeIndex_t](#pulseruntimeinvokeindex_t) | class |  | 1 |
| [PulseRuntimeOutputIndex_t](#pulseruntimeoutputindex_t) | class |  | 1 |
| [PulseRuntimeRegisterIndex_t](#pulseruntimeregisterindex_t) | class |  | 1 |
| [PulseRuntimeStateOffset_t](#pulseruntimestateoffset_t) | class |  | 1 |
| [PulseRuntimeVarIndex_t](#pulseruntimevarindex_t) | class |  | 1 |
| [PulseSelectorOutflowList_t](#pulseselectoroutflowlist_t) | class |  | 0 |
| [PulseValueType_t](#pulsevaluetype_t) | enum |  | 33 |
| [PulseVariableKeysSource_t](#pulsevariablekeyssource_t) | enum |  | 6 |
| [SignatureOutflow_Continue](#signatureoutflow_continue) | class | CPulse_OutflowConnection | 0 |
| [SignatureOutflow_Resume](#signatureoutflow_resume) | class | CPulse_ResumePoint | 0 |

---

### CBasePulseGraphInstance

**Derived by:** [CParticleCollectionBindingInstance](particleslib.md#cparticlecollectionbindinginstance), [CPulseGraphInstance_ServerEntity](server.md#cpulsegraphinstance_serverentity), [CPulseGraphInstance_SmartPropEval](smartprops.md#cpulsegraphinstance_smartpropeval), [CPulseGraphInstance_TestDomain](pulse_system.md#cpulsegraphinstance_testdomain), [CPulseGraphInstance_TestDomain_FakeEntityOwner](pulse_system.md#cpulsegraphinstance_testdomain_fakeentityowner), [CPulseGraphInstance_TurtleGraphics](pulse_system.md#cpulsegraphinstance_turtlegraphics)

**Relationships:**

```mermaid
classDiagram
    CBasePulseGraphInstance <|-- CParticleCollectionBindingInstance
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TestDomain_FakeEntityOwner
    CBasePulseGraphInstance <|-- CPulseGraphInstance_TurtleGraphics
    CBasePulseGraphInstance <|-- CPulseGraphInstance_ServerEntity
    CBasePulseGraphInstance <|-- CPulseGraphInstance_SmartPropEval
```

### CPulseArraylib

**Metadata:** `MPropertyDescription = "Array support."`

### CPulseCell_Base

**Derived by:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow), [CPulseCell_BaseRequirement](pulse_runtime_lib.md#cpulsecell_baserequirement), [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue), [CPulseCell_Unknown](pulse_runtime_lib.md#cpulsecell_unknown)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Base",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_Base <|-- CPulseCell_Unknown
```

### CPulseCell_BaseFlow

**Inherits from:** [CPulseCell_Base](pulse_runtime_lib.md#cpulsecell_base)

**Derived by:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow), [CPulseCell_ExampleSelector](pulse_system.md#cpulsecell_exampleselector), [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint), [CPulseCell_InlineNodeSkipSelector](pulse_runtime_lib.md#cpulsecell_inlinenodeskipselector), [CPulseCell_Outflow_CycleOrdered](pulse_runtime_lib.md#cpulsecell_outflow_cycleordered), [CPulseCell_Outflow_CycleRandom](pulse_runtime_lib.md#cpulsecell_outflow_cyclerandom), [CPulseCell_Outflow_CycleShuffled](pulse_runtime_lib.md#cpulsecell_outflow_cycleshuffled), [CPulseCell_Outflow_TestExplicitYesNo](pulse_system.md#cpulsecell_outflow_testexplicityesno), [CPulseCell_Outflow_TestRandomYesNo](pulse_system.md#cpulsecell_outflow_testrandomyesno), [CPulseCell_PickBestOutflowSelector](pulse_runtime_lib.md#cpulsecell_pickbestoutflowselector), [CPulseCell_SoundEventStart](server.md#cpulsecell_soundeventstart), [CPulseCell_Step_DebugLog](pulse_runtime_lib.md#cpulsecell_step_debuglog), [CPulseCell_Step_EntFire](client.md#cpulsecell_step_entfire), [CPulseCell_Step_FollowEntity](server.md#cpulsecell_step_followentity), [CPulseCell_Step_PublicOutput](pulse_runtime_lib.md#cpulsecell_step_publicoutput), [CPulseCell_Step_SetAnimGraphParam](server.md#cpulsecell_step_setanimgraphparam), [CPulseCell_Step_TestDomainCreateFakeEntity](pulse_system.md#cpulsecell_step_testdomaincreatefakeentity), [CPulseCell_Step_TestDomainDestroyFakeEntity](pulse_system.md#cpulsecell_step_testdomaindestroyfakeentity), [CPulseCell_Step_TestDomainEntFire](pulse_system.md#cpulsecell_step_testdomainentfire), [CPulseCell_Step_TestDomainTracepoint](pulse_system.md#cpulsecell_step_testdomaintracepoint), [CPulseCell_Test_MultiInflow_NoDefault](pulse_system.md#cpulsecell_test_multiinflow_nodefault), [CPulseCell_Test_MultiInflow_WithDefault](pulse_system.md#cpulsecell_test_multiinflow_withdefault), [CPulseCell_Test_MultiOutflow_WithParams](pulse_system.md#cpulsecell_test_multioutflow_withparams), [CPulseCell_Test_NoInflow](pulse_system.md#cpulsecell_test_noinflow), [CSmartPropPulse_BaseQueryableFlow](smartprops.md#csmartproppulse_basequeryableflow), [CSmartPropPulse_CreateRotator](smartprops.md#csmartproppulse_createrotator), [CSmartPropPulse_CreateSizer](smartprops.md#csmartproppulse_createsizer), [CSmartPropPulse_FitOnLine](smartprops.md#csmartproppulse_fitonline), [CSmartPropPulse_Group](smartprops.md#csmartproppulse_group), [CSmartPropPulse_PickOneSelector](smartprops.md#csmartproppulse_pickoneselector), [CSmartPropPulse_PlaceInSphere](smartprops.md#csmartproppulse_placeinsphere), [CSmartPropPulse_SmartProp](smartprops.md#csmartproppulse_smartprop)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_BaseFlow",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseFlow <|-- CPulseCell_Step_EntFire
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_BaseFlow <|-- CPulseCell_InlineNodeSkipSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleOrdered
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleRandom
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleShuffled
    CPulseCell_BaseFlow <|-- CPulseCell_PickBestOutflowSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Step_DebugLog
    CPulseCell_BaseFlow <|-- CPulseCell_Step_PublicOutput
    CPulseCell_BaseFlow <|-- CPulseCell_ExampleSelector
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestExplicitYesNo
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_TestRandomYesNo
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainCreateFakeEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainDestroyFakeEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainEntFire
    CPulseCell_BaseFlow <|-- CPulseCell_Step_TestDomainTracepoint
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_NoDefault
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiInflow_WithDefault
    CPulseCell_BaseFlow <|-- CPulseCell_Test_MultiOutflow_WithParams
    CPulseCell_BaseFlow <|-- CPulseCell_Test_NoInflow
    CPulseCell_BaseFlow <|-- CPulseCell_SoundEventStart
    CPulseCell_BaseFlow <|-- CPulseCell_Step_FollowEntity
    CPulseCell_BaseFlow <|-- CPulseCell_Step_SetAnimGraphParam
    CPulseCell_BaseFlow <|-- CSmartPropPulse_BaseQueryableFlow
    CPulseCell_BaseFlow <|-- CSmartPropPulse_CreateRotator
    CPulseCell_BaseFlow <|-- CSmartPropPulse_CreateSizer
    CPulseCell_BaseFlow <|-- CSmartPropPulse_FitOnLine
    CPulseCell_BaseFlow <|-- CSmartPropPulse_Group
    CPulseCell_BaseFlow <|-- CSmartPropPulse_PickOneSelector
    CPulseCell_BaseFlow <|-- CSmartPropPulse_PlaceInSphere
    CPulseCell_BaseFlow <|-- CSmartPropPulse_SmartProp
```

### CPulseCell_BaseLerp

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Derived by:** [CPulseCell_LerpCameraSettings](client.md#cpulsecell_lerpcamerasettings)

**Metadata:** `MGetKV3ClassDefaults = Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseLerp
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseLerp <|-- CPulseCell_LerpCameraSettings
    CPulseCell_BaseLerp *-- CPulse_ResumePoint
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_WakeResume` | [CPulse_ResumePoint](../schemas/pulse_runtime_lib.md#cpulse_resumepoint) |  |

### CPulseCell_BaseLerp

**Derived by:** [CPulseCell_LerpCameraSettings](client.md#cpulsecell_lerpcamerasettings)

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_StartTime": null,`, `"m_EndTime": null`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseLerp <|-- CPulseCell_LerpCameraSettings
```

### CPulseCell_BaseRequirement

**Inherits from:** [CPulseCell_Base](pulse_runtime_lib.md#cpulsecell_base)

**Derived by:** [CPulseCell_ExampleCriteria](pulse_system.md#cpulsecell_examplecriteria), [CPulseCell_IsRequirementValid](pulse_runtime_lib.md#cpulsecell_isrequirementvalid), [CPulseCell_LimitCount](pulse_runtime_lib.md#cpulsecell_limitcount), [CSmartPropPulse_CriteriaPathPosition](smartprops.md#csmartproppulse_criteriapathposition), [CSmartPropPulse_SelectionChoiceWeight](smartprops.md#csmartproppulse_selectionchoiceweight), [CSmartPropPulse_SelectionEndCap](smartprops.md#csmartproppulse_selectionendcap), [CSmartPropPulse_SelectionLinearLength](smartprops.md#csmartproppulse_selectionlinearlength)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_BaseRequirement",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
    CPulseCell_BaseRequirement <|-- CPulseCell_IsRequirementValid
    CPulseCell_BaseRequirement <|-- CPulseCell_LimitCount
    CPulseCell_BaseRequirement <|-- CPulseCell_ExampleCriteria
    CPulseCell_BaseRequirement <|-- CSmartPropPulse_CriteriaPathPosition
    CPulseCell_BaseRequirement <|-- CSmartPropPulse_SelectionChoiceWeight
    CPulseCell_BaseRequirement <|-- CSmartPropPulse_SelectionEndCap
    CPulseCell_BaseRequirement <|-- CSmartPropPulse_SelectionLinearLength
```

### CPulseCell_BaseState

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Derived by:** [CPulseCell_BooleanSwitchState](pulse_runtime_lib.md#cpulsecell_booleanswitchstate)

**Metadata:** `MGetKV3ClassDefaults = Could not parse KV3 Defaults`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/inflow_statecell.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseState
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseState <|-- CPulseCell_BooleanSwitchState
```

### CPulseCell_BaseValue

**Inherits from:** [CPulseCell_Base](pulse_runtime_lib.md#cpulsecell_base)

**Derived by:** [CPulseCell_Val_TestDomainFindEntityByName](pulse_system.md#cpulsecell_val_testdomainfindentitybyname), [CPulseCell_Val_TestDomainGetEntityName](pulse_system.md#cpulsecell_val_testdomaingetentityname), [CPulseCell_Value_Curve](pulse_runtime_lib.md#cpulsecell_value_curve), [CPulseCell_Value_Gradient](pulse_runtime_lib.md#cpulsecell_value_gradient), [CPulseCell_Value_RandomFloat](pulse_runtime_lib.md#cpulsecell_value_randomfloat), [CPulseCell_Value_RandomInt](pulse_runtime_lib.md#cpulsecell_value_randomint), [CPulseCell_Value_TestValue50](pulse_system.md#cpulsecell_value_testvalue50)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_BaseValue",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_BaseValue
    CPulseCell_BaseValue <|-- CPulseCell_Value_Curve
    CPulseCell_BaseValue <|-- CPulseCell_Value_Gradient
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomFloat
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomInt
    CPulseCell_BaseValue <|-- CPulseCell_Val_TestDomainFindEntityByName
    CPulseCell_BaseValue <|-- CPulseCell_Val_TestDomainGetEntityName
    CPulseCell_BaseValue <|-- CPulseCell_Value_TestValue50
```

### CPulseCell_BaseYieldingInflow

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Derived by:** [CPulseCell_BaseLerp](pulse_runtime_lib.md#cpulsecell_baselerp), [CPulseCell_BaseState](pulse_runtime_lib.md#cpulsecell_basestate), [CPulseCell_FireCursors](pulse_runtime_lib.md#cpulsecell_firecursors), [CPulseCell_Inflow_Wait](pulse_runtime_lib.md#cpulsecell_inflow_wait), [CPulseCell_Inflow_Yield](pulse_runtime_lib.md#cpulsecell_inflow_yield), [CPulseCell_IntervalTimer](pulse_runtime_lib.md#cpulsecell_intervaltimer), [CPulseCell_Outflow_ListenForAnimgraphTag](server.md#cpulsecell_outflow_listenforanimgraphtag), [CPulseCell_Outflow_ListenForEntityOutput](server.md#cpulsecell_outflow_listenforentityoutput), [CPulseCell_Outflow_PlaySceneBase](server.md#cpulsecell_outflow_playscenebase), [CPulseCell_Outflow_ScriptedSequence](server.md#cpulsecell_outflow_scriptedsequence), [CPulseCell_PlaySequence](client.md#cpulsecell_playsequence), [CPulseCell_Step_CallExternalMethod](pulse_runtime_lib.md#cpulsecell_step_callexternalmethod), [CPulseCell_TestWaitWithCursorState](pulse_system.md#cpulsecell_testwaitwithcursorstate), [CPulseCell_Test_MultiOutflow_WithParams_Yielding](pulse_system.md#cpulsecell_test_multioutflow_withparams_yielding), [CPulseCell_Timeline](pulse_runtime_lib.md#cpulsecell_timeline), [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib.md#cpulsecell_waitforcursorswithtagbase), [CPulseCell_WaitForObservable](pulse_runtime_lib.md#cpulsecell_waitforobservable)

**Metadata:** `MGetKV3ClassDefaults = Could not parse KV3 Defaults`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_PlaySequence
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseLerp
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseState
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_FireCursors
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Wait
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Yield
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_IntervalTimer
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Step_CallExternalMethod
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Timeline
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForObservable
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_TestWaitWithCursorState
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Test_MultiOutflow_WithParams_Yielding
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Outflow_ListenForAnimgraphTag
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Outflow_ListenForEntityOutput
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Outflow_PlaySceneBase
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Outflow_ScriptedSequence
```

### CPulseCell_BooleanSwitchState

**Inherits from:** [CPulseCell_BaseState](pulse_runtime_lib.md#cpulsecell_basestate)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_BooleanSwitchState",`, `"m_nEditorNodeID": -1,`, `"m_Condition":`, `{`, `"m_EvaluateConnection":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_DependentObservableVars":`, `[`, `],`, `"m_DependentObservableBlackboardReferences":`, `[`, `]`, `},`, `"m_SubGraph":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_WhenTrue":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_WhenFalse":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPropertyFriendlyName = "Boolean Switch State"`, `MPropertyDescription = "While active, activate a child state based on the results of a boolean condition. Any referenced variables must be marked as observable."`, `MPulseEditorCanvasItemSpecKV3 = "{ className = 'IsStateNode' item_factory = 'BooleanSwitchState' }"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseState <|-- CPulseCell_BooleanSwitchState
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_BaseState
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_CursorQueue

**Inherits from:** [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib.md#cpulsecell_waitforcursorswithtagbase)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_CursorQueue",`, `"m_nEditorNodeID": -1,`, `"m_nCursorsAllowedToWait": -1,`, `"m_WaitComplete":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_nCursorsAllowedToRunParallel": 1`, `}`, `MPropertyFriendlyName = "Cursor Queue"`, `MPropertyDescription = "Causes each execution cursor to wait for the completion of all prior cursors that have visited this node. Use this to safely support multiple triggers to areas of the graph that take time to complete."`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/cursor_wait_zone.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_CursorQueue
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_FireCursors

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_FireCursors",`, `"m_nEditorNodeID": -1,`, `"m_Outflows":`, `[`, `],`, `"m_bWaitForChildOutflows": true,`, `"m_OnFinished":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_OnCanceled":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_FireCursors
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_BaseEntrypoint

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Derived by:** [CPulseCell_Inflow_EntOutputHandler](pulse_runtime_lib.md#cpulsecell_inflow_entoutputhandler), [CPulseCell_Inflow_EventHandler](pulse_runtime_lib.md#cpulsecell_inflow_eventhandler), [CPulseCell_Inflow_GraphHook](pulse_runtime_lib.md#cpulsecell_inflow_graphhook), [CPulseCell_Inflow_Method](pulse_runtime_lib.md#cpulsecell_inflow_method), [CPulseCell_Inflow_ObservableVariableListener](pulse_runtime_lib.md#cpulsecell_inflow_observablevariablelistener)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_BaseEntrypoint",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `}`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EntOutputHandler
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EventHandler
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_GraphHook
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_Method
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_ObservableVariableListener
```

### CPulseCell_Inflow_EntOutputHandler

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_EntOutputHandler",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_SourceEntity": "",`, `"m_SourceOutput": "",`, `"m_ExpectedParamType": "PVAL_VOID"`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EntOutputHandler
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_EventHandler

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_EventHandler",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_EventName": ""`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_EventHandler
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_GraphHook

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_GraphHook",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_HookName": ""`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_GraphHook
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_Method

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_Method",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_MethodName": "",`, `"m_Description": "",`, `"m_bIsPublic": false,`, `"m_ReturnType": "PVAL_VOID",`, `"m_Args":`, `[`, `]`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_Method
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_ObservableVariableListener

**Inherits from:** [CPulseCell_Inflow_BaseEntrypoint](pulse_runtime_lib.md#cpulsecell_inflow_baseentrypoint)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_ObservableVariableListener",`, `"m_nEditorNodeID": -1,`, `"m_EntryChunk": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_nBlackboardReference": -1,`, `"m_bSelfReference": false`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Inflow_BaseEntrypoint <|-- CPulseCell_Inflow_ObservableVariableListener
    CPulseCell_BaseFlow <|-- CPulseCell_Inflow_BaseEntrypoint
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_Wait

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_Wait",`, `"m_nEditorNodeID": -1,`, `"m_WakeResume":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPropertyFriendlyName = "Wait"`, `MPropertyDescription = "Causes each execution cursor to pause at this node for a fixed period of time. Each cursor will wake up and resume execution when the time expires, unless aborted or early-woken."`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/inflow_wait.png"`, `MPulseEditorCanvasItemSpecKV3 = "{ className = 'IsWaitNode IsControlFlowNode' }"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Wait
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Inflow_Yield

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Inflow_Yield",`, `"m_nEditorNodeID": -1,`, `"m_UnyieldResume":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Inflow_Yield
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_InlineNodeSkipSelector

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_InlineNodeSkipSelector",`, `"m_nEditorNodeID": -1,`, `"m_nFlowNodeID": -1,`, `"m_bAnd": false,`, `"m_PassOutflow":`, `{`, `"m_Outflows":`, `[`, `]`, `},`, `"m_FailOutflow":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPulseFunctionHiddenInTool`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_InlineNodeSkipSelector
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_IntervalTimer

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_IntervalTimer",`, `"m_nEditorNodeID": -1,`, `"m_Completed":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_OnInterval":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPropertyFriendlyName = "Interval Timer"`, `MPropertyDescription = "Wait for a duration, firing a child cursor at regular (or randomized) intervals"`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/node_timer.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_IntervalTimer
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_IntervalTimer

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_StartTime": null,`, `"m_EndTime": null,`, `"m_flWaitInterval": 0.000000,`, `"m_flWaitIntervalHigh": 0.000000,`, `"m_bCompleteOnNextWake": false`, `}`

### CPulseCell_IsRequirementValid

**Inherits from:** [CPulseCell_BaseRequirement](pulse_runtime_lib.md#cpulsecell_baserequirement)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_IsRequirementValid",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseRequirement <|-- CPulseCell_IsRequirementValid
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
```

### CPulseCell_IsRequirementValid

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bIsValid` | bool |  |

### CPulseCell_LimitCount

**Inherits from:** [CPulseCell_BaseRequirement](pulse_runtime_lib.md#cpulsecell_baserequirement)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_LimitCount",`, `"m_nEditorNodeID": -1,`, `"m_nLimitCount": 1`, `}`, `MPropertyFriendlyName = "Limit Count"`, `MPropertyDescription = "Skip this node after the limit. Check Type does not apply, the limit will always be checked."`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseRequirement <|-- CPulseCell_LimitCount
    CPulseCell_Base <|-- CPulseCell_BaseRequirement
```

### CPulseCell_LimitCount

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_bLimitCountPasses` | bool |  |

### CPulseCell_LimitCount

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nCurrentCount": 0`, `}`

### CPulseCell_Outflow_CycleOrdered

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Outflow_CycleOrdered",`, `"m_nEditorNodeID": -1,`, `"m_Outputs":`, `[`, `]`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleOrdered
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Outflow_CycleOrdered

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nNextIndex": 0`, `}`

### CPulseCell_Outflow_CycleRandom

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Outflow_CycleRandom",`, `"m_nEditorNodeID": -1,`, `"m_Outputs":`, `[`, `]`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleRandom
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Outflow_CycleShuffled

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Outflow_CycleShuffled",`, `"m_nEditorNodeID": -1,`, `"m_Outputs":`, `[`, `]`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Outflow_CycleShuffled
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Outflow_CycleShuffled

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Shuffle":`, `[`, `],`, `"m_nNextShuffle": 0`, `}`

### CPulseCell_PickBestOutflowSelector

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_PickBestOutflowSelector",`, `"m_nEditorNodeID": -1,`, `"m_nCheckType": "SORT_BY_NUMBER_OF_VALID_CRITERIA",`, `"m_OutflowList":`, `{`, `"m_Outflows":`, `[`, `]`, `}`, `}`, `MPropertyFriendlyName = "Select Best Exit"`, `MPropertyDescription = "Evaluate the requirements of each connected node"`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/requirements.png"`, `MPulseEditorCanvasItemSpecKV3 = "{ className='IsControlFlowNode AllOutflowsInSpecialSection IsSelectorNode' create_special_outflows_section=true }"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_PickBestOutflowSelector
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Step_CallExternalMethod

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Step_CallExternalMethod",`, `"m_nEditorNodeID": -1,`, `"m_MethodName": "",`, `"m_GameBlackboard": "",`, `"m_ExpectedArgs":`, `[`, `],`, `"m_nAsyncCallMode": "ASYNC_FIRE_AND_FORGET",`, `"m_OnFinished":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Step_CallExternalMethod
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Step_DebugLog

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Step_DebugLog",`, `"m_nEditorNodeID": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_DebugLog
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Step_PublicOutput

**Inherits from:** [CPulseCell_BaseFlow](pulse_runtime_lib.md#cpulsecell_baseflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Step_PublicOutput",`, `"m_nEditorNodeID": -1,`, `"m_OutputIndex": -1`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseFlow <|-- CPulseCell_Step_PublicOutput
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Timeline

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Timeline",`, `"m_nEditorNodeID": -1,`, `"m_TimelineEvents":`, `[`, `],`, `"m_bWaitForChildOutflows": true,`, `"m_OnFinished":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_OnCanceled":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_Timeline
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_Timeline

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_flTimeFromPrevious": 0.000000,`, `"m_EventOutflow":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

### CPulseCell_Unknown

**Inherits from:** [CPulseCell_Base](pulse_runtime_lib.md#cpulsecell_base)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_Base <|-- CPulseCell_Unknown
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_UnknownKeys` | KeyValues3 |  |

### CPulseCell_Value_Curve

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Value_Curve",`, `"m_nEditorNodeID": -1,`, `"m_Curve":`, `{`, `"m_spline":`, `[`, `],`, `"m_tangents":`, `[`, `],`, `"m_vDomainMins":`, `[`, `0.000000,`, `0.000000`, `],`, `"m_vDomainMaxs":`, `[`, `0.000000,`, `0.000000`, `]`, `}`, `}`, `MPropertyFriendlyName = "Curve"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Value_Curve
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_Value_Gradient

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Value_Gradient",`, `"m_nEditorNodeID": -1,`, `"m_Gradient":`, `{`, `"m_Stops":`, `[`, `]`, `}`, `}`, `MPropertyFriendlyName = "Gradient"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Value_Gradient
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_Value_RandomFloat

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Value_RandomFloat",`, `"m_nEditorNodeID": -1`, `}`, `MPropertyFriendlyName = "Random Float"`, `MPropertyDescription = "Generate a random float between min and max (inclusive)"`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/exit_cycle_random.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomFloat
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_Value_RandomInt

**Inherits from:** [CPulseCell_BaseValue](pulse_runtime_lib.md#cpulsecell_basevalue)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_Value_RandomInt",`, `"m_nEditorNodeID": -1`, `}`, `MPropertyFriendlyName = "Random Integer"`, `MPropertyDescription = "Generate a random integer between min and max (inclusive)"`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/exit_cycle_random.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseValue <|-- CPulseCell_Value_RandomInt
    CPulseCell_Base <|-- CPulseCell_BaseValue
```

### CPulseCell_WaitForCursorsWithTag

**Inherits from:** [CPulseCell_WaitForCursorsWithTagBase](pulse_runtime_lib.md#cpulsecell_waitforcursorswithtagbase)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_WaitForCursorsWithTag",`, `"m_nEditorNodeID": -1,`, `"m_nCursorsAllowedToWait": -1,`, `"m_WaitComplete":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_bTagSelfWhenComplete": false,`, `"m_nDesiredKillPriority": "None"`, `}`, `MPropertyFriendlyName = "Wait For Cursors With Tag"`, `MPropertyDescription = "Causes this execution cursor to wait for the completion of other cursors with the given tag. Can optionally kill the tag while waiting."`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/cursor_tag.png"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_WaitForCursorsWithTag
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCell_WaitForCursorsWithTagBase

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Derived by:** [CPulseCell_CursorQueue](pulse_runtime_lib.md#cpulsecell_cursorqueue), [CPulseCell_WaitForCursorsWithTag](pulse_runtime_lib.md#cpulsecell_waitforcursorswithtag)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_WaitForCursorsWithTagBase",`, `"m_nEditorNodeID": -1,`, `"m_nCursorsAllowedToWait": -1,`, `"m_WaitComplete":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPulseEditorCanvasItemSpecKV3 = "{ className = 'IsControlFlowNode' }"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForCursorsWithTagBase
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_CursorQueue
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_WaitForCursorsWithTag
```

### CPulseCell_WaitForCursorsWithTagBase

**Derived by:** [CPulseCell_CursorQueue](pulse_runtime_lib.md#cpulsecell_cursorqueue), [CPulseCell_WaitForCursorsWithTag](pulse_runtime_lib.md#cpulsecell_waitforcursorswithtag)

**Relationships:**

```mermaid
classDiagram
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_CursorQueue
    CPulseCell_WaitForCursorsWithTagBase <|-- CPulseCell_WaitForCursorsWithTag
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_TagName` | PulseSymbol_t |  |

### CPulseCell_WaitForObservable

**Inherits from:** [CPulseCell_BaseYieldingInflow](pulse_runtime_lib.md#cpulsecell_baseyieldinginflow)

**Metadata:** `MGetKV3ClassDefaults = {`, `"_class": "CPulseCell_WaitForObservable",`, `"m_nEditorNodeID": -1,`, `"m_Condition":`, `{`, `"m_EvaluateConnection":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_DependentObservableVars":`, `[`, `],`, `"m_DependentObservableBlackboardReferences":`, `[`, `]`, `},`, `"m_OnTrue":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`, `MPulseEditorHeaderIcon = "tools/images/pulse_editor/observable_variable_listener.png"`, `MPropertyFriendlyName = "Wait For Observable Condition"`

**Relationships:**

```mermaid
classDiagram
    CPulseCell_BaseYieldingInflow <|-- CPulseCell_WaitForObservable
    CPulseCell_BaseFlow <|-- CPulseCell_BaseYieldingInflow
    CPulseCell_Base <|-- CPulseCell_BaseFlow
```

### CPulseCursorFuncs

**Metadata:** `MPropertyDescription = "Library for interacting with pulse cursors."`

### CPulseExecCursor

**Derived by:** [CPulseServerCursor](server.md#cpulseservercursor), [CPulseTurtleGraphicsCursor](pulse_system.md#cpulseturtlegraphicscursor), [CTestDomainDerived_Cursor](pulse_system.md#ctestdomainderived_cursor)

**Relationships:**

```mermaid
classDiagram
    CPulseExecCursor <|-- CPulseTurtleGraphicsCursor
    CPulseExecCursor <|-- CTestDomainDerived_Cursor
    CPulseExecCursor <|-- CPulseServerCursor
```

### CPulseGraphDef

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_DomainIdentifier": "",`, `"m_DomainSubType": "PVAL_VOID",`, `"m_ParentMapName": "",`, `"m_ParentXmlName": "",`, `"m_Chunks":`, `[`, `],`, `"m_Cells":`, `[`, `],`, `"m_Vars":`, `[`, `],`, `"m_PublicOutputs":`, `[`, `],`, `"m_InvokeBindings":`, `[`, `],`, `"m_CallInfos":`, `[`, `],`, `"m_Constants":`, `[`, `],`, `"m_DomainValues":`, `[`, `],`, `"m_BlackboardReferences":`, `[`, `],`, `"m_OutputConnections":`, `[`, `]`, `}`

### CPulseGraphExecutionHistory

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nInstanceID": 0,`, `"m_strFileName": "",`, `"m_vecHistory":`, `[`, `],`, `"m_mapCellDesc":`, `{`, `},`, `"m_mapCursorDesc":`, `{`, `}`, `}`

### CPulseMathlib

**Metadata:** `MPropertyDescription = "Basic math support."`

### CPulseRuntimeMethodArg

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Name": "",`, `"m_Description": "",`, `"m_Type": "PVAL_VOID"`, `}`

### CPulseTestScriptLib

**Metadata:** `MPropertyDescription = "Testing script helpers."`

### CPulse_BlackboardReference

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_hBlackboardResource": "",`, `"m_BlackboardResource": "",`, `"m_nNodeID": -1,`, `"m_NodeName": ""`, `}`

### CPulse_CallInfo

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_PortName": "",`, `"m_nEditorNodeID": -1,`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_CallMethodID": -1,`, `"m_nSrcChunk": -1,`, `"m_nSrcInstruction": -1`, `}`

### CPulse_Chunk

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Instructions":`, `[`, `],`, `"m_Registers":`, `[`, `],`, `"m_InstructionDebugInfos":`, `[`, `]`, `}`

### CPulse_Constant

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Type": "PVAL_VOID",`, `"m_Value": null`, `}`

### CPulse_DomainValue

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nType": "INVALID",`, `"m_Value": "",`, `"m_RequiredRuntimeType": "PVAL_VOID"`, `}`

### CPulse_InstructionDebug

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nFlowNodeID": -1,`, `"m_nValueNodeID": -1,`, `"m_SequencePointName": ""`, `}`

### CPulse_InvokeBinding

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_RegisterMap":`, `{`, `"m_Inparams": null,`, `"m_Outparams": null`, `},`, `"m_FuncName": "",`, `"m_nCellIndex": -1,`, `"m_nSrcChunk": -1,`, `"m_nSrcInstruction": -1`, `}`

### CPulse_OutflowConnection

**Derived by:** [CPulse_ResumePoint](pulse_runtime_lib.md#cpulse_resumepoint), [SignatureOutflow_Continue](pulse_runtime_lib.md#signatureoutflow_continue)

**Relationships:**

```mermaid
classDiagram
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
    CPulse_OutflowConnection <|-- SignatureOutflow_Continue
    CPulse_OutflowConnection *-- PulseRuntimeChunkIndex_t
    CPulse_OutflowConnection *-- PulseRegisterMap_t
```

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_SourceOutflowName` | PulseSymbol_t |  |
| `m_nDestChunk` | [PulseRuntimeChunkIndex_t](../schemas/pulse_runtime_lib.md#pulseruntimechunkindex_t) |  |
| `m_nInstruction` | int32 |  |
| `m_OutflowRegisterMap` | [PulseRegisterMap_t](../schemas/pulse_runtime_lib.md#pulseregistermap_t) |  |

### CPulse_OutputConnection

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_SourceOutput": "",`, `"m_TargetEntity": "",`, `"m_TargetInput": "",`, `"m_Param": ""`, `}`

### CPulse_PublicOutput

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Name": "",`, `"m_Description": "",`, `"m_Args":`, `[`, `]`, `}`

### CPulse_RegisterInfo

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nReg": -1,`, `"m_Type": "PVAL_VOID",`, `"m_OriginName": "",`, `"m_nWrittenByInstruction": -1,`, `"m_nLastReadByInstruction": -1`, `}`

### CPulse_ResumePoint

**Inherits from:** [CPulse_OutflowConnection](pulse_runtime_lib.md#cpulse_outflowconnection)

**Derived by:** [SignatureOutflow_Resume](pulse_runtime_lib.md#signatureoutflow_resume)

**Relationships:**

```mermaid
classDiagram
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
    CPulse_ResumePoint <|-- SignatureOutflow_Resume
```

### CPulse_Variable

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Name": "",`, `"m_Description": "",`, `"m_Type": "PVAL_VOID",`, `"m_DefaultValue": null,`, `"m_nKeysSource": "PRIVATE",`, `"m_bIsPublicBlackboardVariable": false,`, `"m_bIsObservable": false,`, `"m_nEditorNodeID": -1`, `}`

### EPulseGraphExecutionHistoryFlag

**Values:**

| Name | Value |
|------|-------|
| `NO_FLAGS` | 0 |
| `CURSOR_ADD_TAG` | 1 |
| `CURSOR_REMOVE_TAG` | 2 |
| `CURSOR_RETIRED` | 4 |
| `REQUIREMENT_PASS` | 8 |
| `REQUIREMENT_FAIL` | 16 |

### OutflowWithRequirements_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Connection":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_DestinationFlowNodeID": -1,`, `"m_RequirementNodeIDs":`, `[`, `],`, `"m_nCursorStateBlockIndex":`, `[`, `]`, `}`

### PGDInstruction_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_nCode": "INVALID",`, `"m_nVar": -1,`, `"m_nReg0": -1,`, `"m_nReg1": -1,`, `"m_nReg2": -1,`, `"m_nInvokeBindingIndex": -1,`, `"m_nChunk": -1,`, `"m_nDestInstruction": 0,`, `"m_nCallInfoIndex": -1,`, `"m_nConstIdx": -1,`, `"m_nDomainValueIdx": -1,`, `"m_nBlackboardReferenceIdx": -1`, `}`

### PulseApiFeature_t

**Values:**

| Name | Value |
|------|-------|
| `AF_NONE` | 0 |
| `AF_ENTITIES` | 1 |
| `AF_PANORAMA` | 2 |
| `AF_PARTICLES` | 8 |
| `AF_FAKE_ENTITIES` | 16 |
| `AF_SELECTORS_WITHOUT_REQUIREMENTS` | 32 |

### PulseBestOutflowRules_t

**Values:**

| Name | Value |
|------|-------|
| `SORT_BY_NUMBER_OF_VALID_CRITERIA` | 0 |
| `SORT_BY_OUTFLOW_INDEX` | 1 |

### PulseCursorCancelPriority_t

**Values:**

| Name | Value |
|------|-------|
| `None` | 0 |
| `CancelOnSucceeded` | 1 |
| `SoftCancel` | 2 |
| `HardCancel` | 3 |

### PulseCursorExecResult_t

**Values:**

| Name | Value |
|------|-------|
| `Succeeded` | 0 |
| `Canceled` | 1 |
| `Failed` | 2 |
| `OngoingNotify` | 3 |

### PulseCursorID_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseCursorYieldToken_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseDocNodeID_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseDomainValueType_t

**Values:**

| Name | Value |
|------|-------|
| `INVALID` | -1 |
| `ENTITY_NAME` | 0 |
| `PANEL_ID` | 1 |
| `COUNT` | 2 |

### PulseGraphExecutionHistoryCursorDesc_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"vecAncestorCursorIDs":`, `[`, `],`, `"nSpawnNodeID": -1,`, `"nRetiredAtNodeID": -1,`, `"flLastReferenced": 0.000000,`, `"nLastValidEntryIdx": 0`, `}`

### PulseGraphExecutionHistoryEntry_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"nCursorID": -1,`, `"nEditorID": -1,`, `"flExecTime": 0.000000,`, `"unFlags": 0,`, `"tagName": ""`, `}`

### PulseGraphExecutionHistoryNodeDesc_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"strCellDesc": "",`, `"strBindingName": ""`, `}`

### PulseGraphInstanceID_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint32 |  |

### PulseInstructionCode_t

**Values:**

| Name | Value |
|------|-------|
| `INVALID` | 0 |
| `IMMEDIATE_HALT` | 1 |
| `RETURN_VOID` | 2 |
| `RETURN_VALUE` | 3 |
| `NOP` | 4 |
| `JUMP` | 5 |
| `JUMP_COND` | 6 |
| `CHUNK_LEAP` | 7 |
| `CHUNK_LEAP_COND` | 8 |
| `PULSE_CALL_SYNC` | 9 |
| `PULSE_CALL_ASYNC_FIRE` | 10 |
| `CELL_INVOKE` | 11 |
| `LIBRARY_INVOKE` | 12 |
| `SET_VAR` | 13 |
| `GET_VAR` | 14 |
| `GET_VAR_DETACH` | 15 |
| `DETACH_REGISTER` | 16 |
| `SET_VAR_ARRAY_ELEMENT_1D` | 17 |
| `SET_VAR_OBSERVABLE` | 18 |
| `GET_CONST` | 19 |
| `GET_ARRAY_ELEMENT` | 20 |
| `GET_DOMAIN_VALUE` | 21 |
| `COPY` | 22 |
| `NOT` | 23 |
| `NEGATE` | 24 |
| `ADD` | 25 |
| `SUB` | 26 |
| `MUL` | 27 |
| `DIV` | 28 |
| `MOD` | 29 |
| `LT` | 30 |
| `LTE` | 31 |
| `EQ` | 32 |
| `NE` | 33 |
| `AND` | 34 |
| `OR` | 35 |
| `SCALE` | 36 |
| `SCALE_INV` | 37 |
| `ELEMENT_ACCESS` | 38 |
| `CONVERT_VALUE` | 39 |
| `REINTERPRET_INSTANCE` | 40 |
| `GET_BLACKBOARD_REFERENCE` | 41 |
| `SET_BLACKBOARD_REFERENCE` | 42 |
| `LAST_SERIALIZED_CODE` | 43 |
| `NEGATE_INT` | 44 |
| `NEGATE_FLOAT` | 45 |
| `NEGATE_VEC2` | 46 |
| `NEGATE_VEC3` | 47 |
| `NEGATE_VEC4` | 48 |
| `ADD_INT` | 49 |
| `ADD_FLOAT` | 50 |
| `ADD_STRING` | 51 |
| `ADD_VEC2` | 52 |
| `ADD_VEC3` | 53 |
| `ADD_VEC3WS_VEC3` | 54 |
| `ADD_VEC3_VEC3WS` | 55 |
| `ADD_VEC4` | 56 |
| `ADD_GAMETIME_FLOAT` | 57 |
| `ADD_FLOAT_GAMETIME` | 58 |
| `SUB_INT` | 59 |
| `SUB_FLOAT` | 60 |
| `SUB_VEC2` | 61 |
| `SUB_VEC3` | 62 |
| `SUB_VEC3WS_VEC3` | 63 |
| `SUB_VEC3WS_VEC3WS` | 64 |
| `SUB_VEC4` | 65 |
| `SUB_GAMETIME_FLOAT` | 66 |
| `SUB_GAMETIME` | 67 |
| `MUL_INT` | 68 |
| `MUL_FLOAT` | 69 |
| `DIV_FLOAT` | 70 |
| `MOD_INT` | 71 |
| `MOD_FLOAT` | 72 |
| `LT_INT` | 73 |
| `LT_FLOAT` | 74 |
| `LT_GAMETIME` | 75 |
| `LTE_INT` | 76 |
| `LTE_FLOAT` | 77 |
| `LTE_GAMETIME` | 78 |
| `EQ_BOOL` | 79 |
| `EQ_INT` | 80 |
| `EQ_FLOAT` | 81 |
| `EQ_VEC2` | 82 |
| `EQ_VEC3` | 83 |
| `EQ_VEC3WS` | 84 |
| `EQ_VEC4` | 85 |
| `EQ_STRING` | 86 |
| `EQ_ENTITY_NAME` | 87 |
| `EQ_SCHEMA_ENUM` | 88 |
| `EQ_EHANDLE` | 89 |
| `EQ_PANEL_HANDLE` | 90 |
| `EQ_OPAQUE_HANDLE` | 91 |
| `EQ_TEST_HANDLE` | 92 |
| `EQ_COLOR_RGB` | 93 |
| `EQ_ARRAY` | 94 |
| `EQ_GAMETIME` | 95 |
| `NE_BOOL` | 96 |
| `NE_INT` | 97 |
| `NE_FLOAT` | 98 |
| `NE_VEC2` | 99 |
| `NE_VEC3` | 100 |
| `NE_VEC3WS` | 101 |
| `NE_VEC4` | 102 |
| `NE_STRING` | 103 |
| `NE_ENTITY_NAME` | 104 |
| `NE_SCHEMA_ENUM` | 105 |
| `NE_EHANDLE` | 106 |
| `NE_PANEL_HANDLE` | 107 |
| `NE_OPAQUE_HANDLE` | 108 |
| `NE_TEST_HANDLE` | 109 |
| `NE_COLOR_RGB` | 110 |
| `NE_ARRAY` | 111 |
| `NE_GAMETIME` | 112 |
| `SCALE_VEC3` | 113 |
| `SCALE_VEC2` | 114 |
| `SCALE_VEC4` | 115 |
| `SCALE_INV_VEC3` | 116 |
| `SCALE_INV_VEC2` | 117 |
| `SCALE_INV_VEC4` | 118 |
| `ELEMENT_ACCESS_VEC2` | 119 |
| `ELEMENT_ACCESS_VEC3` | 120 |
| `ELEMENT_ACCESS_VEC3WS` | 121 |
| `ELEMENT_ACCESS_VEC4` | 122 |
| `ELEMENT_ACCESS_COLOR_RGB` | 123 |
| `GET_CONST_INLINE_STORAGE` | 124 |

### PulseMethodCallMode_t

**Values:**

| Name | Value |
|------|-------|
| `SYNC_WAIT_FOR_COMPLETION` | 0 |
| `ASYNC_FIRE_AND_FORGET` | 1 |

### PulseNodeDynamicOutflows_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Outflows":`, `[`, `]`, `}`

### PulseNodeDynamicOutflows_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_OutflowID": "",`, `"m_Connection":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `}`, `}`

### PulseObservableBoolExpression_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_EvaluateConnection":`, `{`, `"m_SourceOutflowName": "",`, `"m_nDestChunk": -1,`, `"m_nInstruction": -1`, `},`, `"m_DependentObservableVars":`, `[`, `],`, `"m_DependentObservableBlackboardReferences":`, `[`, `]`, `}`

### PulseRegisterMap_t

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Inparams` | KeyValues3 |  |
| `m_InparamsWhichCanBeMoved` | CKV3MemberNameSet |  |
| `m_Outparams` | KeyValues3 |  |

### PulseRuntimeBlackboardReferenceIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int16 |  |

### PulseRuntimeCallInfoIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeCellIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeChunkIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeConstantIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int16 |  |

### PulseRuntimeDomainValueIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int16 |  |

### PulseRuntimeEntrypointIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeInvokeIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeOutputIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseRuntimeRegisterIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int16 |  |

### PulseRuntimeStateOffset_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | uint16 |  |

### PulseRuntimeVarIndex_t

**Metadata:** `MIsBoxedIntegerType`

**Fields:**

| Name | Type | Annotations |
|------|------|-------------|
| `m_Value` | int32 |  |

### PulseSelectorOutflowList_t

**Metadata:** `MGetKV3ClassDefaults = {`, `"m_Outflows":`, `[`, `]`, `}`

### PulseValueType_t

**Values:**

| Name | Value |
|------|-------|
| `PVAL_VOID` | -1 |
| `PVAL_BOOL` | 0 |
| `PVAL_INT` | 1 |
| `PVAL_FLOAT` | 2 |
| `PVAL_STRING` | 3 |
| `PVAL_VEC2` | 4 |
| `PVAL_VEC3` | 5 |
| `PVAL_QANGLE` | 6 |
| `PVAL_VEC3_WORLDSPACE` | 7 |
| `PVAL_VEC4` | 8 |
| `PVAL_TRANSFORM` | 9 |
| `PVAL_TRANSFORM_WORLDSPACE` | 10 |
| `PVAL_COLOR_RGB` | 11 |
| `PVAL_GAMETIME` | 12 |
| `PVAL_EHANDLE` | 13 |
| `PVAL_RESOURCE` | 14 |
| `PVAL_RESOURCE_NAME` | 15 |
| `PVAL_SNDEVT_GUID` | 16 |
| `PVAL_SNDEVT_NAME` | 17 |
| `PVAL_ENTITY_NAME` | 18 |
| `PVAL_OPAQUE_HANDLE` | 19 |
| `PVAL_TYPESAFE_INT` | 20 |
| `PVAL_MODEL_MATERIAL_GROUP` | 21 |
| `PVAL_CURSOR_FLOW` | 22 |
| `PVAL_VARIANT` | 23 |
| `PVAL_UNKNOWN` | 24 |
| `PVAL_SCHEMA_ENUM` | 25 |
| `PVAL_PANORAMA_PANEL_HANDLE` | 26 |
| `PVAL_TEST_HANDLE` | 27 |
| `PVAL_ARRAY` | 28 |
| `PVAL_TYPESAFE_INT64` | 29 |
| `PVAL_PARTICLE_EHANDLE` | 30 |
| `PVAL_COUNT` | 31 |

### PulseVariableKeysSource_t

**Values:**

| Name | Value |
|------|-------|
| `PRIVATE` | 0 |
| `CPP` | 1 |
| `VMAP` | 2 |
| `VMDL` | 3 |
| `XML` | 4 |
| `COUNT` | 5 |

### SignatureOutflow_Continue

**Inherits from:** [CPulse_OutflowConnection](pulse_runtime_lib.md#cpulse_outflowconnection)

**Relationships:**

```mermaid
classDiagram
    CPulse_OutflowConnection <|-- SignatureOutflow_Continue
```

### SignatureOutflow_Resume

**Inherits from:** [CPulse_ResumePoint](pulse_runtime_lib.md#cpulse_resumepoint)

**Relationships:**

```mermaid
classDiagram
    CPulse_ResumePoint <|-- SignatureOutflow_Resume
    CPulse_OutflowConnection <|-- CPulse_ResumePoint
```
