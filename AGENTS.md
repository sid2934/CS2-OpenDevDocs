# CS2 Developer Reference — AI Agent Context

This file is designed to be loaded as context into any AI coding assistant
(GitHub Copilot, Claude Code, Cursor, ChatGPT, Gemini, etc.) by external
developers working on **Counter-Strike 2 tooling, plugins, demo parsers,
game servers, or any other CS2-related project**.

You do **not** need to clone this repository. Paste this file's raw URL into
your AI tool's context, or copy-paste the content directly into a system
prompt / custom instructions field:

```
https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/AGENTS.md
```

---

## What this documentation covers

This repository contains auto-generated, structured documentation for
Counter-Strike 2, extracted from the
[SteamDatabase/GameTracking-CS2](https://github.com/SteamDatabase/GameTracking-CS2)
game-file dump. It is updated automatically every 4 hours. The documentation
covers:

| Section | Contents | Browse URL |
|---------|----------|------------|
| **Schema entities** | All C++ entity classes, structs, and enums from CS2's DumpSource2 schemas (~3 000 types across 30 engine modules) | https://sid2934.github.io/GameTracking-CS2/schemas |
| **Protobufs** | All `.proto` message definitions — game events, network messages, GC messages, demo format (42 files, ~777 messages) | https://sid2934.github.io/GameTracking-CS2/protobufs |
| **ConVars** | Every console variable with default value, flags, and description (~3 800 entries) | https://sid2934.github.io/GameTracking-CS2/convars |
| **Commands** | Every console command with flags and description (~1 130 entries) | https://sid2934.github.io/GameTracking-CS2/commands |
| **UML diagrams** | Mermaid class-hierarchy diagrams for every schema module | https://sid2934.github.io/GameTracking-CS2/diagrams/server_hierarchy |

---

## CS2 Architecture overview

CS2 is built on Source 2. Its entity system uses a
**controller / pawn split**:

- A **controller** (`CBasePlayerController` → `CCSPlayerController`) is a
  lightweight, persistent entity that represents a connected client for the
  lifetime of the connection. It survives round resets.
- A **pawn** (`CBasePlayerPawn` → `CCSPlayerPawn`) is the physical, in-world
  representation of the player. It is recreated each round. The controller
  points to the current pawn via `m_hPlayerPawn`.

All server-side entities ultimately derive from `CEntityInstance` →
`CBaseEntity`. Client-side mirrors are `C_BaseEntity`-rooted (prefix `C_`).

---

## Key server-side entities

### `CBaseEntity`
*Root entity. Every server entity derives from this.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#cbaseentity

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_iHealth` | `int32` | Current health points |
| `m_iTeamNum` | `uint8` | 0 = unassigned, 1 = spectator, 2 = T, 3 = CT |
| `m_vecAbsOrigin` | `Vector` | World-space position |
| `m_angAbsRotation` | `QAngle` | World-space rotation |
| `m_iName` | `CUtlSymbolLarge` | Targetname / entity name |
| `m_bTakesDamage` | `bool` | Whether entity can receive damage |
| `m_nNextThinkTick` | `GameTick_t` | Next simulation tick |

---

### `CCSPlayerController`
*One per connected client, persists across rounds.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#ccsplayercontroller

Inheritance: `CEntityInstance` → `CBaseEntity` → `CBasePlayerController` → `CCSPlayerController`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_hPlayerPawn` | `CHandle<CCSPlayerPawn>` | Handle to the active pawn (may change each round) |
| `m_iTeamNum` | `uint8` | Team: 2 = T, 3 = CT |
| `m_iszPlayerName` | `CUtlSymbolLarge` | Display name |
| `m_steamID` | `uint64` | Steam account ID |
| `m_iScore` | `int32` | Match score |
| `m_iPing` | `uint32` | Network RTT in milliseconds |
| `m_szClan` | `CUtlSymbolLarge` | Clan/team tag shown in scoreboard |
| `m_szCrosshairCodes` | `CUtlSymbolLarge` | Encoded crosshair share-code |
| `m_iPendingTeamNum` | `uint8` | Pending team change |
| `m_iCoachingTeam` | `int32` | Non-zero if player is coaching |
| `m_nPlayerDominated` | `uint64` | Bitmask of players this controller is dominating |
| `m_pInGameMoneyServices` | `CCSPlayerController_InGameMoneyServices*` | Money/economy component |
| `m_pInventoryServices` | `CCSPlayerController_InventoryServices*` | Item/skin component |
| `m_pActionTrackingServices` | `CCSPlayerController_ActionTrackingServices*` | Stat-tracking component |
| `m_pDamageServices` | `CCSPlayerController_DamageServices*` | Damage-log component |

---

### `CCSPlayerPawn`
*The in-world player body; recreated each round.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#ccsplayerpawn

Inheritance: `CBaseEntity` → `CBaseModelEntity` → `CBaseFlex` → `CBaseAnimGraph` → `CBaseCombatCharacter` → `CBasePlayerPawn` → `CCSPlayerPawnBase` → `CCSPlayerPawn`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_vecVelocity` | `Vector` | Current velocity |
| `m_flFallVelocity` | `float32` | Vertical fall speed |
| `m_flStamina` | `float32` | Stamina (affects accuracy) |
| `m_flVelocityModifier` | `float32` | Speed multiplier |
| `m_iShotsFired` | `int32` | Shots fired this burst (recoil tracking) |
| `m_flFlashDuration` | `float32` | Remaining flashbang blind time (seconds) |
| `m_flFlashMaxAlpha` | `float32` | Peak flash intensity (0–255) |
| `m_bIsScoped` | `bool` | Currently scoped in |
| `m_bIsWalking` | `bool` | Currently walking (shifted) |
| `m_bResumeZoom` | `bool` | Will re-scope after shooting |
| `m_iPlayerState` | `int32` | Death-state flags |
| `m_hActiveWeapon` | `CHandle<CBasePlayerWeapon>` | Currently held weapon |
| `m_hObserverTarget` | `CHandle<CBaseEntity>` | Entity being spectated |

---

### `CCSGameRules`
*Singleton holding all match-level state.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#ccsgamerules

Accessed via the `CCSGameRulesProxy` entity on the client. Inheritance:
`CGameRules` → `CMultiplayRules` → `CTeamplayRules` → `CCSGameRules`

Key fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_bFreezePeriod` | `bool` | Buy phase (players frozen) |
| `m_bWarmupPeriod` | `bool` | Pre-match warmup active |
| `m_gamePhase` | `int32` | 1=First Half, 2=Second Half, 3=Pre-OT, 4=OT, 5=Game Over |
| `m_totalRoundsPlayed` | `int32` | Total rounds completed |
| `m_nRoundsPlayedThisPhase` | `int32` | Rounds in current half/OT period |
| `m_nOvertimePlaying` | `int32` | Overtime period count (0 = regulation) |
| `m_fRoundStartTime` | `GameTime_t` | When freeze time ended |
| `m_iRoundTime` | `int32` | Round time limit (seconds) |
| `m_iFreezeTime` | `int32` | Freeze-time duration (seconds) |
| `m_bMapHasBombTarget` | `bool` | Map has bomb sites |
| `m_bMapHasRescueZone` | `bool` | Map has hostage rescue zones |
| `m_iNumCT` | `int32` | Players on CT side |
| `m_iNumTerrorist` | `int32` | Players on T side |
| `m_bBombDropped` | `bool` | Bomb currently dropped on ground |
| `m_bBombPlanted` | `bool` | Bomb currently planted |
| `m_nEndMatchMapGroupVoteTypes` | `int32[10]` | Map vote options |
| `m_eMatchDevice` | `int32` | Device type (PC, console) |

---

### `CCSWeaponBase` / `CCSWeaponBaseGun`
*Base weapon classes.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#ccsweaponbase

Inheritance: `CBaseEntity` → `CBaseModelEntity` → `CBasePlayerWeapon` → `CCSWeaponBase` → `CCSWeaponBaseGun`

Key `CCSWeaponBase` fields:

| Field | Type | Notes |
|-------|------|-------|
| `m_iClip1` | `int32` | Rounds remaining in magazine |
| `m_iPrimaryAmmoCount` | `int32` | Ammo in reserve |
| `m_fLastShotTime` | `GameTime_t` | GameTime of most recent shot |
| `m_bInReload` | `bool` | Reload animation in progress |
| `m_bBurstMode` | `bool` | Burst-fire mode active (Glock, FAMAS) |
| `m_flNextPrimaryAttack` | `GameTime_t` | Earliest next fire time |
| `m_zoomLevel` | `int32` | Scope zoom level (0 = unscoped) |
| `m_iSilencerOn` | `bool` | Silencer attached (M4A1-S, USP-S) |
| `m_weaponMode` | `CSWeaponMode` | Fire mode enum |

All individual weapons (`CAWP`, `CAK47`, `CDEAGLE`, etc.) inherit from
`CCSWeaponBaseGun` and typically carry 0 additional fields (all data is in
`CCSWeaponBaseVData` and the base classes).

Full weapon list: https://sid2934.github.io/GameTracking-CS2/schemas/server

---

### `CPlantedC4`
*The planted bomb entity.*
Full reference: https://sid2934.github.io/GameTracking-CS2/schemas/server#cplantedc4

| Field | Type | Notes |
|-------|------|-------|
| `m_flC4Blow` | `GameTime_t` | GameTime when bomb detonates |
| `m_bBombTicking` | `bool` | Bomb is counting down |
| `m_bBombDefused` | `bool` | Bomb was successfully defused |
| `m_hBombDefuser` | `CHandle<CCSPlayerPawn>` | Pawn currently defusing |
| `m_flDefuseLength` | `float32` | Total defuse duration (with/without kit) |
| `m_flDefuseCountDown` | `GameTime_t` | Time when defuse completes |
| `m_nBombSite` | `int32` | Bombsite index (0 = A, 1 = B) |

---

## Key Protobuf message groups

### Game events (`cs_gameevents.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/cs_gameevents

CS2-specific game event messages (e.g. bomb plant/defuse, kill, round end).
Sent as `CMsgSource1LegacyGameEvent` on the network.

### CS2 user messages (`cstrike15_usermessages.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/cstrike15_usermessages

73 messages sent from server to individual clients: HUD hints, radar updates,
kill cam data, round end summary, item purchases, etc.

Key messages: `CCSUsrMsg_RoundEnd`, `CCSUsrMsg_SendAudio`,
`CCSUsrMsg_RadioText`, `CCSUsrMsg_HudMsg`, `CCSUsrMsg_KillCam`,
`CCSUsrMsg_MatchEndData`

### CS2 GC messages (`cstrike15_gcmessages.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/cstrike15_gcmessages

156 messages between the game client/server and Valve's Game Coordinator:
matchmaking, lobbies, item inventory, competitive ranks, GOTV relay, etc.

Key messages: `CMsgGCCStrike15_v2_MatchmakingClient2GCHello`,
`CMsgGCCStrike15_v2_ClientRequestPlayersProfile`,
`CMsgGCCStrike15_v2_MatchList`

### Core net messages (`netmessages.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/netmessages

63 engine-level network messages: snapshot packets, string tables, data
tables (SendTables), sound events, entity creation/deletion.

Key messages: `CNETMsg_Tick`, `CSVCMsg_PacketEntities`,
`CSVCMsg_CreateStringTable`, `CSVCMsg_GameEvent`, `CSVCMsg_UserMessage`

### Demo file format (`demo.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/demo

Messages defining the `.dem` file format: `CDemoHeader`, `CDemoFileHeader`,
`CDemoPacket`, `CDemoFullPacket`, `CDemoStringTables`, `CDemoClassInfo`.
CS2 demos are written in the Source 2 "PBDEMS2" binary format.

### User commands (`cs_usercmd.proto`)
Reference: https://sid2934.github.io/GameTracking-CS2/proto/cs_usercmd

`CCSUsrCmd` — the per-tick command sent from client to server: move direction,
view angles, attack buttons, subtick data.

---

## Important enums

### Team numbers
| Value | Meaning |
|-------|---------|
| `0` | Unassigned |
| `1` | Spectator |
| `2` | Terrorist (T) |
| `3` | Counter-Terrorist (CT) |

### `m_gamePhase` values (`CCSGameRules`)
| Value | Meaning |
|-------|---------|
| `1` | First Half |
| `2` | Second Half |
| `3` | Pre-overtime (halftime of OT) |
| `4` | Overtime |
| `5` | Game Over |

### `CSWeaponState_t` (weapon state)
| Value | Meaning |
|-------|---------|
| `WEAPON_NOT_CARRIED` | On the ground |
| `WEAPON_IS_CARRIED_BY_PLAYER` | In a player's inventory |
| `WEAPON_IS_ACTIVE` | Currently held / active |

---

## Schema modules quick-reference

| Module | Entities | Description | URL |
|--------|----------|-------------|-----|
| `server` | ~574 | Server-side entity classes (weapons, players, game rules, …) | https://sid2934.github.io/GameTracking-CS2/schemas/server |
| `client` | ~714 | Client-side entity mirrors and UI components | https://sid2934.github.io/GameTracking-CS2/schemas/client |
| `particles` | ~502 | Particle system types | https://sid2934.github.io/GameTracking-CS2/schemas/particles |
| `animgraphlib` | ~265 | Animation graph nodes and types | https://sid2934.github.io/GameTracking-CS2/schemas/animgraphlib |
| `animlib` | ~210 | Core animation types | https://sid2934.github.io/GameTracking-CS2/schemas/animlib |
| `animationsystem` | ~55 | Top-level animation system | https://sid2934.github.io/GameTracking-CS2/schemas/animationsystem |
| `physicslib` | ~98 | Physics types | https://sid2934.github.io/GameTracking-CS2/schemas/physicslib |
| `vphysics2` | ~5 | Havok physics integration | https://sid2934.github.io/GameTracking-CS2/schemas/vphysics2 |
| `modellib` | ~140 | Model/mesh types | https://sid2934.github.io/GameTracking-CS2/schemas/modellib |
| `soundsystem` | ~23 | Sound system types | https://sid2934.github.io/GameTracking-CS2/schemas/soundsystem |
| `materialsystem2` | ~19 | Material types | https://sid2934.github.io/GameTracking-CS2/schemas/materialsystem2 |
| `entity2` | ~17 | Base entity framework types (`CEntityInstance`, `GameTime_t`, …) | https://sid2934.github.io/GameTracking-CS2/schemas/entity2 |
| `navlib` | ~11 | Navigation mesh types | https://sid2934.github.io/GameTracking-CS2/schemas/navlib |
| `resourcesystem` | ~48 | Resource/asset system types | https://sid2934.github.io/GameTracking-CS2/schemas/resourcesystem |
| `scenesystem` | ~12 | Scene graph types | https://sid2934.github.io/GameTracking-CS2/schemas/scenesystem |
| `pulse_system` | ~30 | Pulse scripting system | https://sid2934.github.io/GameTracking-CS2/schemas/pulse_system |

---

## Raw GitHub URLs for deep fetching

If your AI tool supports fetching raw documents, use these URLs to load full
content for a specific section:

| Content | Raw URL |
|---------|---------|
| Server schema (full, ~large) | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/schemas/server.md` |
| Client schema (full, ~large) | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/schemas/client.md` |
| ConVars | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/convars.md` |
| Commands | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/commands.md` |
| cs_gameevents proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/cs_gameevents.md` |
| cstrike15_usermessages proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/cstrike15_usermessages.md` |
| cstrike15_gcmessages proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/cstrike15_gcmessages.md` |
| netmessages proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/netmessages.md` |
| demo proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/demo.md` |
| cs_usercmd proto | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/proto/cs_usercmd.md` |
| Entity hierarchy diagram | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/docs/diagrams/server_hierarchy.md` |
| This file (AGENTS.md) | `https://raw.githubusercontent.com/sid2934/GameTracking-CS2/main/AGENTS.md` |

---

## Common tasks and where to look

| Task | Where to look |
|------|--------------|
| Parse a CS2 demo file | `demo.proto`, `netmessages.proto`, `CCSGameRules` fields |
| Track player positions / health | `CCSPlayerPawn` fields in `server` schema |
| Track player money / economy | `CCSPlayerController_InGameMoneyServices` in `server` schema |
| Identify round state (freeze, live, over) | `CCSGameRules.m_bFreezePeriod`, `m_gamePhase`, `m_bWarmupPeriod` |
| Decode kill/damage events | `cs_gameevents.proto` → `CMsgSource1LegacyGameEvent` |
| Understand weapon properties | `CCSWeaponBase`, `CCSWeaponBaseGun`, `CCSWeaponBaseVData` in `server` schema |
| Work with bomb events | `CPlantedC4` in `server` schema, `cs_gameevents.proto` |
| Decode player commands | `cs_usercmd.proto` → `CCSUsrCmd` |
| Find all convars for a system | ConVars reference, filter by flag or prefix |
| Build a server plugin (Metamod/CS2) | `server` schema for entity offsets, `netmessages.proto` for hooking |
| Work with item/skin data | `cstrike15_gcmessages.proto`, `CCSPlayerController_InventoryServices` |
| Understand rank/matchmaking | `cstrike15_gcmessages.proto` GC message types |
