# generated by datamodel-codegen from https://app.swaggerhub.com/apiproxy/registry/Henrik-3/HenrikDev-API/3.0.0

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class Regions(Enum):
    eu = "eu"
    na = "na"
    ap = "ap"
    kr = "kr"


class Affinities(Enum):
    eu = "eu"
    na = "na"
    latam = "latam"
    br = "br"
    ap = "ap"
    kr = "kr"


class PremierConferences(Enum):
    EU_CENTRAL_EAST = "EU_CENTRAL_EAST"
    EU_WEST = "EU_WEST"
    EU_MIDDLE_EAST = "EU_MIDDLE_EAST"
    EU_TURKEY = "EU_TURKEY"
    NA_US_EAST = "NA_US_EAST"
    NA_US_WEST = "NA_US_WEST"
    LATAM_NORTH = "LATAM_NORTH"
    LATAM_SOUTH = "LATAM_SOUTH"
    BR_BRAZIL = "BR_BRAZIL"
    KR_KOREA = "KR_KOREA"
    AP_ASIA = "AP_ASIA"
    AP_JAPAN = "AP_JAPAN"
    AP_OCEANIA = "AP_OCEANIA"
    AP_SOUTH_ASIA = "AP_SOUTH_ASIA"


class PremierSeasonsEventTypes(Enum):
    LEAGUE = "LEAGUE"
    TOURNAMENT = "TOURNAMENT"


class PremierSeasonsEventMapSelectionTypes(Enum):
    RANDOM = "RANDOM"
    PICKBAN = "PICKBAN"


class Maps(Enum):
    Ascent = "Ascent"
    Split = "Split"
    Fracture = "Fracture"
    Bind = "Bind"
    Breeze = "Breeze"
    District = "District"
    Kasbah = "Kasbah"
    Piazza = "Piazza"
    Lotus = "Lotus"
    Pearl = "Pearl"
    Icebox = "Icebox"
    Haven = "Haven"


class Modes(Enum):
    Competitive = "Competitive"
    Custom_Game = "Custom Game"
    Deathmatch = "Deathmatch"
    Escalation = "Escalation"
    Team_Deathmatch = "Team Deathmatch"
    New_Map = "New Map"
    Replication = "Replication"
    Snowball_Fight = "Snowball Fight"
    Spike_Rush = "Spike Rush"
    Swiftplay = "Swiftplay"
    Unrated = "Unrated"


class ModesApi(Enum):
    competitive = "competitive"
    custom = "custom"
    deathmatch = "deathmatch"
    escalation = "escalation"
    teamdeathmatch = "teamdeathmatch"
    newmap = "newmap"
    replication = "replication"
    snowballfight = "snowballfight"
    spikerush = "spikerush"
    swiftplay = "swiftplay"
    unrated = "unrated"


class ModeIds(Enum):
    competitive = "competitive"
    custom = "custom"
    deathmatch = "deathmatch"
    ggteam = "ggteam"
    hurm = "hurm"
    newmap = "newmap"
    onefa = "onefa"
    snowball = "snowball"
    spikerush = "spikerush"
    swiftplay = "swiftplay"
    unrated = "unrated"


class Tiers(Enum):
    Unrated = "Unrated"
    Unknown_1 = "Unknown 1"
    Unknown_2 = "Unknown 2"
    Iron_1 = "Iron 1"
    Iron_2 = "Iron 2"
    Iron_3 = "Iron 3"
    Bronze_1 = "Bronze 1"
    Bronze_2 = "Bronze 2"
    Bronze_3 = "Bronze 3"
    Silver_1 = "Silver 1"
    Silver_2 = "Silver 2"
    Silver_3 = "Silver 3"
    Gold_1 = "Gold 1"
    Gold_2 = "Gold 2"
    Gold_3 = "Gold 3"
    Platinum_1 = "Platinum 1"
    Platinum_2 = "Platinum 2"
    Platinum_3 = "Platinum 3"
    Diamond_1 = "Diamond 1"
    Diamond_2 = "Diamond 2"
    Diamond_3 = "Diamond 3"
    Ascendant_1 = "Ascendant 1"
    Ascendant_2 = "Ascendant 2"
    Ascendant_3 = "Ascendant 3"
    Immortal_1 = "Immortal 1"
    Immortal_2 = "Immortal 2"
    Immortal_3 = "Immortal 3"
    Radiant = "Radiant"


class TiersOld(Enum):
    Unrated = "Unrated"
    Unknown_1 = "Unknown 1"
    Unknown_2 = "Unknown 2"
    Iron_1 = "Iron 1"
    Iron_2 = "Iron 2"
    Iron_3 = "Iron 3"
    Bronze_1 = "Bronze 1"
    Bronze_2 = "Bronze 2"
    Bronze_3 = "Bronze 3"
    Silver_1 = "Silver 1"
    Silver_2 = "Silver 2"
    Silver_3 = "Silver 3"
    Gold_1 = "Gold 1"
    Gold_2 = "Gold 2"
    Gold_3 = "Gold 3"
    Platinum_1 = "Platinum 1"
    Platinum_2 = "Platinum 2"
    Platinum_3 = "Platinum 3"
    Diamond_1 = "Diamond 1"
    Diamond_2 = "Diamond 2"
    Diamond_3 = "Diamond 3"
    Immortal_1 = "Immortal 1"
    Immortal_2 = "Immortal 2"
    Immortal_3 = "Immortal 3"
    Radiant = "Radiant"


class Platforms(Enum):
    PC = "PC"
    Console = "Console"


class Seasons(Enum):
    e1a1 = "e1a1"
    e1a2 = "e1a2"
    e1a3 = "e1a3"
    e2a1 = "e2a1"
    e2a2 = "e2a2"
    e2a3 = "e2a3"
    e3a1 = "e3a1"
    e3a2 = "e3a2"
    e3a3 = "e3a3"
    e4a1 = "e4a1"
    e4a2 = "e4a2"
    e4a3 = "e4a3"
    e5a1 = "e5a1"
    e5a2 = "e5a2"
    e5a3 = "e5a3"
    e6a1 = "e6a1"
    e6a2 = "e6a2"
    e6a3 = "e6a3"
    e7a1 = "e7a1"
    e7a2 = "e7a2"
    e7a3 = "e7a3"


class ActRankWin(BaseModel):
    patched_tier: str | None = Field(None, examples=["Gold 1"])
    tier: int | None = Field(None, examples=[12])


class BySeason(BaseModel):
    error: str | bool | None = Field(None)
    wins: int | None = Field(None, examples=[12])
    number_of_games: int | None = Field(None, examples=[24])
    final_rank: int | None = Field(None, examples=[12])
    final_rank_patched: str | None = Field(None, examples=["Gold 1"])
    act_rank_wins: list[ActRankWin] | None = None
    old: bool | None = Field(None, examples=[True])


class SessionPlaytime(BaseModel):
    minutes: int | None = Field(None, examples=[26])
    seconds: int | None = Field(None, examples=[1560])
    milliseconds: int | None = Field(None, examples=[1560000])


class Card(BaseModel):
    small: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/playercards/8edf22c5-4489-ab41-769a-07adb4c454d6/smallart.png"
        ],
    )
    large: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/playercards/8edf22c5-4489-ab41-769a-07adb4c454d6/largeart.png"
        ],
    )
    wide: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/playercards/8edf22c5-4489-ab41-769a-07adb4c454d6/wideart.png"
        ],
    )


class Agent(BaseModel):
    small: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/displayicon.png"
        ],
    )
    full: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/fullportrait.png"
        ],
    )
    bust: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/bustportrait.png"
        ],
    )
    killfeed: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/killfeedportrait.png"
        ],
    )


class Assets(BaseModel):
    card: Card | None = None
    agent: Agent | None = None


class FriendlyFire(BaseModel):
    incoming: int | None = Field(None, examples=[0])
    outgoing: int | None = Field(None, examples=[0])


class Behaviour(BaseModel):
    afk_rounds: int | None = Field(None, examples=[0])
    friendly_fire: FriendlyFire | None = None
    rounds_in_spawn: int | None = Field(None, examples=[0])


class Os(BaseModel):
    name: str | None = Field(None, examples=["Windows"])
    version: str | None = Field(None, examples=["10.0.22000.1.768.64bit"])


class Platform(BaseModel):
    type: str | None = Field(None, examples=["PC"])
    os: Os | None = None


class AbilityCasts(BaseModel):
    c_cast: int | None = Field(None, examples=[16])
    q_cast: int | None = Field(None, examples=[5])
    e_cast: int | None = Field(None, examples=[26])
    x_cast: int | None = Field(None, examples=[0])


class Stats(BaseModel):
    score: int | None = Field(None, examples=[4869])
    kills: int | None = Field(None, examples=[18])
    deaths: int | None = Field(None, examples=[18])
    assists: int | None = Field(None, examples=[5])
    bodyshots: int | None = Field(None, examples=[48])
    headshots: int | None = Field(None, examples=[9])
    legshots: int | None = Field(None, examples=[5])


class Spent(BaseModel):
    overall: int | None = Field(None, examples=[59750])
    average: int | None = Field(None, examples=[2598])


class LoadoutValue(BaseModel):
    overall: int | None = Field(None, examples=[71700])
    average: int | None = Field(None, examples=[3117])


class Economy(BaseModel):
    spent: Spent | None = None
    loadout_value: LoadoutValue | None = None


class Player(BaseModel):
    puuid: str | None = Field(None, examples=["54942ced-1967-5f66-8a16-1e0dae875641"])
    name: str | None = Field(None, examples=["Henrik3"])
    tag: str | None = Field(None, examples=["EUW3"])
    team: str | None = Field(None, examples=["Red"])
    level: int | None = Field(None, examples=[104])
    character: str | None = Field(None, examples=["Sova"])
    currenttier: int | None = Field(None, examples=[12])
    currenttier_patched: str | None = Field(None, examples=["Gold 1"])
    player_card: str | None = Field(
        None, examples=["8edf22c5-4489-ab41-769a-07adb4c454d6"]
    )
    player_title: str | None = Field(
        None, examples=["e3ca05a4-4e44-9afe-3791-7d96ca8f71fa"]
    )
    party_id: str | None = Field(
        None, examples=["b7590bd4-e2c9-4dd3-8cbf-05f04158375e"]
    )
    session_playtime: SessionPlaytime | None = None
    assets: Assets | None = None
    behaviour: Behaviour | None = None
    platform: Platform | None = None
    ability_casts: AbilityCasts | None = None
    stats: Stats | None = None
    economy: Economy | None = None
    damage_made: int | None = Field(None, examples=[3067])
    damage_received: int | None = Field(None, examples=[3115])


class Platform1(Platform):
    pass


class Observer(BaseModel):
    puuid: UUID | None = None
    name: str | None = None
    tag: str | None = None
    platform: Platform1 | None = None
    session_playtime: SessionPlaytime | None = None
    team: str | None = None
    level: float | None = None
    player_card: UUID | None = None
    player_title: UUID | None = None
    party_id: UUID | None = None


class Coach(BaseModel):
    puuid: UUID | None = None
    team: str | None = None


class Customization(BaseModel):
    icon: str | None = None
    image: str | None = None
    primary: str | None = None
    secondary: str | None = None
    tertiary: str | None = None


class Roaster(BaseModel):
    members: list[str] | None = None
    name: str | None = None
    tag: str | None = None
    customization: Customization | None = None


class Team(BaseModel):
    has_won: bool | None = Field(None, examples=[True])
    rounds_won: int | None = Field(None, examples=[13])
    rounds_lost: int | None = Field(None, examples=[10])
    roaster: Roaster | None = None


class PremierInfo(BaseModel):
    tournament_id: str | None = None
    matchup_id: str | None = None


class Metadata(BaseModel):
    map: Maps | None = None
    game_version: str | None = Field(
        None, examples=["release-03.12-shipping-16-649370"]
    )
    game_length: int | None = Field(None, examples=[2356581])
    game_start: int | None = Field(None, examples=[1641934366])
    game_start_patched: str | None = Field(
        None, examples=["Tuesday, January 11 2022 9:52 PM"]
    )
    rounds_played: int | None = Field(None, examples=[23])
    mode: Modes | None = None
    mode_id: ModeIds | None = None
    queue: str | None = Field(None, examples=["Standard"])
    season_id: UUID | None = None
    platform: str | None = Field(None, examples=["PC"])
    matchid: UUID | None = None
    premier_info: PremierInfo | None = None
    region: Regions | None = None
    cluster: str | None = Field(None, examples=["London"])


class Players(BaseModel):
    all_players: list[Player] | None = None
    red: list[Player] | None = None
    blue: list[Player] | None = None


class Teams(BaseModel):
    red: Team | None = None
    blue: Team | None = None


class PlantLocation(BaseModel):
    x: int | None = Field(None, examples=[-1325])
    y: int | None = Field(None, examples=[-1325])


class PlantedBy(BaseModel):
    puuid: str | None = Field(None, examples=["54942ced-1967-5f66-8a16-1e0dae875641"])
    display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    team: str | None = Field(None, examples=["Red"])


class Location(BaseModel):
    x: int | None = Field(None, examples=[5177])
    y: int | None = Field(None, examples=[-8908])


class PlayerLocationsOnPlantItem(BaseModel):
    player_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    player_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    player_team: str | None = Field(None, examples=["Red"])
    location: Location | None = None
    view_radians: float | None = Field(None, examples=[0.5277854])


class PlantEvents(BaseModel):
    plant_location: PlantLocation | None = None
    planted_by: PlantedBy | None = None
    plant_site: str | None = Field(None, examples=["A"])
    plant_time_in_round: int | None = Field(None, examples=[26345])
    player_locations_on_plant: list[PlayerLocationsOnPlantItem] | None = None


class DefuseLocation(PlantLocation):
    pass


class DefusedBy(PlantedBy):
    pass


class PlayerLocationsOnDefuseItem(PlayerLocationsOnPlantItem):
    pass


class DefuseEvents(BaseModel):
    defuse_location: DefuseLocation | None = None
    defused_by: DefusedBy | None = None
    defuse_time_in_round: int | None = Field(None, examples=[26345])
    player_locations_on_defuse: None | (list[PlayerLocationsOnDefuseItem]) = None


class AbilityCasts1(BaseModel):
    c_casts: int | None = Field(None, examples=[2])
    q_casts: int | None = Field(None, examples=[5])
    e_casts: int | None = Field(None, examples=[20])
    x_casts: int | None = Field(None, examples=[1])


class DamageEvent(BaseModel):
    receiver_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    receiver_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    receiver_team: str | None = Field(None, examples=["Red"])
    bodyshots: int | None = Field(None, examples=[3])
    damage: int | None = Field(None, examples=[156])
    headshots: int | None = Field(None, examples=[1])
    legshots: int | None = Field(None, examples=[0])


class VictimDeathLocation(BaseModel):
    x: int | None = Field(None, examples=[7266])
    y: int | None = Field(None, examples=[-5096])


class DamageWeaponAssets(BaseModel):
    display_icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/weapons/9c82e19d-4575-0200-1a81-3eacf00cf872/displayicon.png"
        ],
    )
    killfeed_icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/weapons/9c82e19d-4575-0200-1a81-3eacf00cf872/killstreamicon.png"
        ],
    )


class PlayerLocationsOnKillItem(PlayerLocationsOnPlantItem):
    pass


class Assistant(BaseModel):
    assistant_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    assistant_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    assistant_team: str | None = Field(None, examples=["Red"])


class KillEvent(BaseModel):
    kill_time_in_round: int | None = Field(None, examples=[43163])
    kill_time_in_match: int | None = Field(None, examples=[890501])
    killer_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    killer_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    killer_team: str | None = Field(None, examples=["Red"])
    victim_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    victim_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    victim_team: str | None = Field(None, examples=["Red"])
    victim_death_location: VictimDeathLocation | None = None
    damage_weapon_id: str | None = Field(
        None,
        examples=["9C82E19D-4575-0200-1A81-3EACF00CF872"],
    )
    damage_weapon_name: str | None = Field(None, examples=["Vandal"])
    damage_weapon_assets: DamageWeaponAssets | None = None
    secondary_fire_mode: bool | None = Field(None, examples=[False])
    player_locations_on_kill: list[PlayerLocationsOnKillItem] | None = []
    assistants: list[Assistant] | None = []


class Assets1(BaseModel):
    display_icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/weapons/462080d1-4035-2937-7c09-27aa2a5c27a7/displayicon.png"
        ],
    )
    killfeed_icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/weapons/462080d1-4035-2937-7c09-27aa2a5c27a7/killstreamicon.png"
        ],
    )


class Weapon(BaseModel):
    id: str | None = Field(None, examples=["462080D1-4035-2937-7C09-27AA2A5C27A7"])
    name: str | None = Field(None, examples=["Spectre"])
    assets: Assets1 | None = None


class Assets2(BaseModel):
    display_icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/gear/822bcab2-40a2-324e-c137-e09195ad7692/displayicon.png"
        ],
    )


class Armor(BaseModel):
    id: str | None = Field(None, examples=["822BCAB2-40A2-324E-C137-E09195AD7692"])
    name: str | None = Field(None, examples=["Heavy Shields"])
    assets: Assets2 | None = None


class Economy1(BaseModel):
    loadout_value: int | None = Field(None, examples=[3900])
    weapon: Weapon | None = None
    armor: Armor | None = None
    remaining: int | None = Field(None, examples=[5300])
    spent: int | None = Field(None, examples=[1550])


class PlayerStat(BaseModel):
    ability_casts: AbilityCasts1 | None = None
    player_puuid: str | None = Field(
        None,
        examples=["54942ced-1967-5f66-8a16-1e0dae875641"],
    )
    player_display_name: str | None = Field(None, examples=["Henrik3#EUW3"])
    player_team: str | None = Field(None, examples=["Red"])
    damage_events: list[DamageEvent] | None = []
    damage: int | None = Field(None, examples=[282])
    bodyshots: int | None = Field(None, examples=[7])
    headshots: int | None = Field(None, examples=[1])
    legshots: int | None = Field(None, examples=[1])
    kill_events: list[KillEvent] | None = []
    kills: int | None = Field(None, examples=[2])
    score: int | None = Field(None, examples=[430])
    economy: Economy1 | None = None
    was_afk: bool | None = Field(None, examples=[False])
    was_penalized: bool | None = Field(None, examples=[False])
    stayed_in_spawn: bool | None = Field(None, examples=[False])


class Round(BaseModel):
    winning_team: str | None = Field(None, examples=["Red"])
    end_type: str | None = Field(None, examples=["Eliminated"])
    bomb_planted: bool | None = Field(None, examples=[True])
    bomb_defused: bool | None = Field(None, examples=[False])
    plant_events: PlantEvents | None = None
    defuse_events: DefuseEvents | None = None
    player_stats: list[PlayerStat] | None = None


class Match(BaseModel):
    metadata: Metadata | None = None
    players: Players | None = None
    observers: list[Observer] | None = None
    coaches: list[Coach] | None = None
    teams: Teams | None = None
    rounds: list[Round] | None = None


class LocalizedName(BaseModel):
    ar_AE: str | None = Field(None, alias="ar-AE")
    de_DE: str | None = Field(None, alias="de-DE")
    en_GB: str | None = Field(None, alias="en-GB")
    en_US: str | None = Field(None, alias="en-US")
    es_ES: str | None = Field(None, alias="es-ES")
    es_MX: str | None = Field(None, alias="es-MX")
    fr_FR: str | None = Field(None, alias="fr-FR")
    id_ID: str | None = Field(None, alias="id-ID")
    it_IT: str | None = Field(None, alias="it-IT")
    ja_JP: str | None = Field(None, alias="ja-JP")
    ko_KR: str | None = Field(None, alias="ko-KR")
    pl_PL: str | None = Field(None, alias="pl-PL")
    pt_BR: str | None = Field(None, alias="pt-BR")
    ru_RU: str | None = Field(None, alias="ru-RU")
    th_TH: str | None = Field(None, alias="th-TH")
    tr_TR: str | None = Field(None, alias="tr-TR")
    vi_VN: str | None = Field(None, alias="vi-VN")
    zn_CN: str | None = Field(None, alias="zn-CN")
    zn_TW: str | None = Field(None, alias="zn-TW")


class ContentItem(BaseModel):
    name: str | None = None
    localizedNames: list[LocalizedName] | None = None
    id: str | None = None
    assetName: str | None = None
    assetPath: str | None = None


Content = List[ContentItem]


class LeaderboardItem(BaseModel):
    PlayerCardID: str | None = Field(
        None,
        examples=["8edf22c5-4489-ab41-769a-07adb4c454d6"],
    )
    TitleID: str | None = Field(None, examples=["82de085a-4c2b-da95-a139-048e4ce83dae"])
    IsBanned: bool | None = Field(None, examples=[False])
    IsAnonymized: bool | None = Field(None, examples=[False])
    puuid: str | None = Field(None, examples=["c3b5b276-a43d-53f2-a897-038bc60b6682"])
    gameName: str | None = Field(None, examples=["Liquid ScreaM"])
    tagLine: str | None = Field(None, examples=["1TAP"])
    leaderboardRank: int | None = Field(None, examples=[1])
    rankedRating: int | None = Field(None, examples=[1222])
    numberOfWins: int | None = Field(None, examples=[67])
    competitiveTier: int | None = Field(None, examples=[24])


Leaderboard = List[LeaderboardItem]


class Translation(BaseModel):
    content: str | None = Field(
        None,
        examples=[
            "The platform is currently unavailable while we perform emergency maintenance."
        ],
    )
    locale: str | None = Field(None, examples=["en_US"])


class Update(BaseModel):
    created_at: str | None = Field(None, examples=["2022-01-12T22:11:07.645499+00:00"])
    updated_at: str | None = Field(None, examples=["2022-01-12T23:00:00.000000+00:00"])
    publish: bool | None = Field(None, examples=[True])
    id: int | None = Field(None, examples=[6658])
    translations: list[Translation] | None = None
    publish_locations: list[str] | None = None
    author: str | None = Field(None, examples=["Riot Games"])


class Title(BaseModel):
    content: str | None = Field(None, examples=["Emergency Maintenance In Progress"])
    locale: str | None = Field(None, examples=["en_US"])


class StatusItem(BaseModel):
    created_at: str | None = Field(None, examples=["2022-01-12T22:11:07.530569+00:00"])
    archive_at: str | None = Field(None, examples=["2022-01-13T10:00:00.000000+00:00"])
    updates: list[Update] | None = None
    platforms: list[str] | None = None
    updated_at: str | None = Field(None, examples=["2022-01-12T23:00:00.000000+00:00"])
    id: int | None = Field(None, examples=[4175])
    titles: list[Title] | None = None
    maintenance_status: str | None = Field(None, examples=["in_progress"])
    incident_severity: str | None = Field(None, examples=["warning"])


Status = List[StatusItem]


class Images(BaseModel):
    small: str | None = None
    large: str | None = None
    triangle_down: str | None = None
    triangle_up: str | None = None


class Data(BaseModel):
    currenttier: int | None = Field(None, examples=[12])
    currenttier_patched: str | None = Field(None, examples=["Gold 1"])
    images: Images | None = None
    ranking_in_tier: int | None = Field(None, examples=[20])
    mmr_change_to_last_game: int | None = Field(None, examples=[-16])
    elo: int | None = Field(None, examples=[920])
    name: str | None = Field(None, examples=["Henrik3"])
    tag: str | None = Field(None, examples=["EUW3"])
    old: bool | None = Field(None, examples=[True])


class V1mmr(BaseModel):
    status: int | None = Field(None, examples=[200])
    data: Data | None = None


class CurrentData(BaseModel):
    currenttier: int | None = Field(None, examples=[12])
    currenttierpatched: str | None = Field(None, examples=["Gold 1"])
    images: Images | None = None
    ranking_in_tier: int | None = Field(None, examples=[20])
    mmr_change_to_last_game: int | None = Field(None, examples=[-16])
    elo: int | None = Field(None, examples=[920])
    old: bool | None = Field(None, examples=[True])


class HighestRank(BaseModel):
    old: bool | None = Field(None, examples=[False])
    tier: int | None = Field(None, examples=[19])
    patched_tier: str | None = Field(None, examples=["Diamond 2"])
    season: str | None = Field(None, examples=["e5a3"])


class BySeason1(BaseModel):
    e6a3: BySeason | None = None
    e6a2: BySeason | None = None
    e6a1: BySeason | None = None
    e5a3: BySeason | None = None
    e5a2: BySeason | None = None
    e5a1: BySeason | None = None
    e4a3: BySeason | None = None
    e4a2: BySeason | None = None
    e4a1: BySeason | None = None
    e3a3: BySeason | None = None
    e3a2: BySeason | None = None
    e3a1: BySeason | None = None
    e2a3: BySeason | None = None
    e2a2: BySeason | None = None
    e2a1: BySeason | None = None
    e1a3: BySeason | None = None
    e1a2: BySeason | None = None
    e1a1: BySeason | None = None


class Data1(BaseModel):
    name: str
    tag: str
    current_data: CurrentData | None = None
    highest_rank: HighestRank | None = None
    by_season: BySeason1 | None = None


class V2mmr(BaseModel):
    status: int | None = Field(None, examples=[200])
    data: Data1 | None = None


class Map(BaseModel):
    name: str | None = Field(None, examples=["Icebox"])
    id: str | None = Field(None, examples=["e2ad5c54-4114-a870-9641-8ea21279579a"])


class Datum(BaseModel):
    currenttier: int | None = Field(None, examples=[12])
    currenttier_patched: str | None = Field(None, examples=["Gold 1"])
    images: Images | None = None
    match_id: str | None = Field(
        None,
        examples=["e5a3301c-c8e5-43bc-be94-a5c0d5275fd4"],
    )
    map: Map | None = None
    season_id: str | None = Field(
        None,
        examples=["34093c29-4306-43de-452f-3f944bde22be"],
    )
    ranking_in_tier: int | None = Field(None, examples=[20])
    mmr_change_to_last_game: int | None = Field(None, examples=[-16])
    elo: int | None = Field(None, examples=[920])
    date: str | None = Field(None, examples=["Tuesday, January 11, 2022 9:52 PM"])
    date_raw: int | None = Field(None, examples=[1641934366])


class V1mmrh(BaseModel):
    status: int | None = Field(None, examples=[200])
    name: str | None = Field(None, examples=["Henrik3"])
    tag: str | None = Field(None, examples=["EUW3"])
    data: list[Datum] | None = None


class V3matches(BaseModel):
    status: str | None = Field(None, examples=[200])
    data: list[Match] | None = None


V1leaderboard = Leaderboard


class V2leaderboard(BaseModel):
    last_update: int | None = Field(None, examples=[1641219805])
    next_update: int | None = Field(None, examples=[1641222865])
    total_players: int | None = Field(None, examples=[37463])
    radiant_threshold: int | None = Field(None, examples=[550])
    immortal_3_threshold: int | None = Field(None, examples=[200])
    immortal_2_threshold: int | None = Field(None, examples=[100])
    immortal_1_threshold: int | None = Field(None, examples=[0])
    players: Leaderboard | None = None


class Item1(BaseModel):
    ItemTypeID: str | None = None
    ItemID: str | None = None
    Amount: str | None = None


class Item(BaseModel):
    Item: Item1 | None = None
    BasePrice: int | None = None
    CurrencyID: str | None = None
    DiscountPercent: float | None = None
    DiscountedPrice: int | None = None
    IsPromoItem: bool | None = None


class BundleRaw(BaseModel):
    ID: str | None = None
    DataAssetID: str | None = None
    CurrencyID: str | None = None
    Items: list[Item] | None = None
    DurationRemainingInSeconds: int | None = None
    Wholesaleonly: bool | None = None


class Item2(BaseModel):
    uuid: str | None = None
    name: str | None = None
    image: str | None = None
    type: str | None = None
    amount: int | None = None
    discount_percent: float | None = None
    base_price: int | None = None
    discounted_price: int | None = None
    promo_item: bool | None = None


class BundleParsed(BaseModel):
    bundle_uuid: str | None = None
    seconds_remaining: int | None = None
    bundle_price: float | None = None
    whole_sale_only: bool | None = None
    expires_at: str | None = None
    items: list[Item2] | None = None


class FeaturedBundleType(BaseModel):
    Bundle: BundleRaw | None = None
    Bundles: list[BundleRaw] | None = None
    BundleRemainingDurationInSeconds: int | None = None


class Data2(BaseModel):
    FeaturedBundle: FeaturedBundleType | None = None


class V1storefeatured(BaseModel):
    status: int | None = None
    data: Data2 | None = None


class V2storefeatured(BaseModel):
    status: int | None = None
    data: list[BundleParsed] | None = None


class Type(Enum):
    skin_level = "skin_level"
    skin_chroma = "skin_chroma"
    buddy = "buddy"
    spray = "spray"
    player_card = "player_card"
    player_title = "player_title"


class ContentTier(BaseModel):
    name: str | None = Field(None, examples=["Deluxe Edition"])
    dev_name: str | None = Field(None, examples=["Exclusive"])
    icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/contenttiers/e046854e-406c-37f4-6607-19a9ba8426fc/displayicon.png"
        ],
    )


class V2storeoffer(BaseModel):
    offer_id: str | None = Field(
        None,
        examples=["a3dba920-44ee-d7c5-5227-99a80aee3bd9"],
    )
    cost: int | None = Field(None, examples=[2175])
    name: str | None = Field(None, examples=["Araxys Vandal"])
    icon: str | None = Field(
        None,
        examples=[
            "https://media.valorant-api.com/weaponskinlevels/a3dba920-44ee-d7c5-5227-99a80aee3bd9/displayicon.png"
        ],
    )
    type: Type | None = None
    skin_id: str | None = Field(None, examples=["4c926aa9-4f26-bc80-c486-9b888333373f"])
    content_tier: ContentTier | None = None


class Data3(BaseModel):
    offers: list[V2storeoffer] | None = None


class V2storeoffers(BaseModel):
    status: int | None = None
    data: Data3 | None = None


class League(BaseModel):
    name: str | None = Field(None, examples=["Challengers DACH"])
    identifier: str | None = Field(None, examples=["vrl_dach"])
    icon: str | None = Field(
        None,
        examples=[
            "https://static.lolesports.com/leagues/1672932144616_DACH_ICON_400_400.png"
        ],
    )
    region: str | None = Field(None, examples=["EMEA"])


class Tournament(BaseModel):
    name: str | None = Field(None, examples=["challengers_emea_leagues_split_1"])
    season: str | None = Field(None, examples=["2023"])


class Type1(Enum):
    playAll = "playAll"
    bestOf = "bestOf"


class GameType(BaseModel):
    type: Type1 | None = None
    count: int | None = Field(None, examples=[2])


class Record(BaseModel):
    wins: int | None = Field(None, examples=[0])
    losses: int | None = Field(None, examples=[1])


class Team1(BaseModel):
    name: str | None = Field(None, examples=["Angry Titans"])
    code: str | None = Field(None, examples=["AT"])
    icon: str | None = Field(
        None,
        examples=[
            "https://static.lolesports.com/teams/1644488801867_AT_red_icon2x.png"
        ],
    )
    has_won: bool | None = Field(None, examples=[False])
    game_wins: int | None = Field(None, examples=[0])
    record: Record | None = None


class Match1(BaseModel):
    id: str | None = Field(None, examples=["109625073196211557"])
    game_type: GameType | None = None
    teams: list[Team1] | None = None


class V1esportscheduleitem(BaseModel):
    date: str | None = Field(None, examples=["2023-01-17T20:00:00Z"])
    state: str | None = Field(None, examples=["completed"])
    type: str | None = Field(None, examples=["match"])
    vod: str | None = Field(None, examples=["https://youtu.be/PrQ-LBZ4W-E"])
    league: League | None = None
    tournament: Tournament | None = None
    match: Match1 | None = None


class V1esportschedule(BaseModel):
    status: int | None = None
    data: list[V1esportscheduleitem] | None = None


class Map1(BaseModel):
    id: str
    name: str


class Season(BaseModel):
    id: str
    short: str


class Meta(BaseModel):
    id: str | None = None
    map: Map1 | None = None
    version: str | None = None
    mode: str | None = None
    started_at: str | None = None
    season: Season | None = None
    region: str | None = None
    cluster: str | None = None


class Character(Map1):
    pass


class Shots(BaseModel):
    head: float
    body: float
    leg: float


class Damage(BaseModel):
    made: float
    received: float


class Stats1(BaseModel):
    puuid: str
    team: str
    level: float
    character: Character
    tier: float
    score: float
    kills: float
    deaths: float
    assists: float
    shots: Shots
    damage: Damage


class Teams1(BaseModel):
    red: float
    blue: float


class V1LifetimeMatchesItem(BaseModel):
    meta: Meta
    stats: Stats1
    teams: Teams1


class Results(BaseModel):
    total: float | None = None
    returned: float | None = None
    before: float | None = None
    after: float | None = None


class V1LifetimeMatches(BaseModel):
    status: int | None = None
    name: str | None = None
    tag: str | None = None
    results: Results | None = None
    data: list[V1LifetimeMatchesItem] | None = None


class Stats2(BaseModel):
    wins: float | None = None
    matches: float | None = None
    losses: float | None = None


class Placement(BaseModel):
    points: float | None = None
    conference: str | None = None
    division: float | None = None
    place: float | None = None


class MemberItem(BaseModel):
    puuid: str | None = None
    name: str | None = None
    tag: str | None = None


class Data4(BaseModel):
    id: UUID | None = None
    name: str | None = None
    tag: str | None = None
    enrolled: bool | None = None
    stats: Stats2 | None = None
    placement: Placement | None = None
    customization: Customization | None = None
    member: list[MemberItem] | None = None


class V1PremierTeam(BaseModel):
    status: int | None = None
    data: Data4 | None = None


class LeagueMatch(BaseModel):
    id: UUID | None = None
    points_before: float | None = None
    points_after: float | None = None
    started_at: datetime | None = None


class Data5(BaseModel):
    league_matches: list[LeagueMatch] | None = None


class V1PremierTeamHistory(BaseModel):
    status: float | None = None
    data: Data5 | None = None


class V1PartialPremierTeam(BaseModel):
    id: UUID | None = None
    name: str | None = None
    tag: str | None = None
    conference: PremierConferences | None = None
    division: float | None = None
    affinity: Affinities | None = None
    region: Regions | None = None
    losses: float | None = None
    wins: float | None = None
    score: float | None = None
    ranking: float | None = None
    customization: Customization | None = None


class V1PremierSearch(BaseModel):
    status: float | None = None
    data: list[V1PartialPremierTeam] | None = None


class V1PremierLeaderboard(V1PremierSearch):
    pass


class Pod(BaseModel):
    pod: str | None = None
    name: str | None = None


class Datum1(BaseModel):
    id: UUID | None = None
    affinity: Affinities | None = None
    pods: list[Pod] | None = None
    region: Regions | None = None
    timezone: str | None = None
    name: PremierConferences | None = None
    icon: str | None = None


class V1PremierConference(BaseModel):
    status: float | None = None
    data: list[Datum1] | None = None


class ConferenceSchedule(BaseModel):
    conference: PremierConferences | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None


class Map2(BaseModel):
    name: Maps | None = None
    id: UUID | None = None


class MapSelection(BaseModel):
    type: PremierSeasonsEventMapSelectionTypes | None = None
    maps: list[Map2] | None = None


class Event(BaseModel):
    id: UUID | None = None
    type: PremierSeasonsEventTypes | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    conference_schedules: list[ConferenceSchedule] | None = None
    map_selection: MapSelection | None = None
    points_required_to_participate: float | None = None


class Datum2(BaseModel):
    id: UUID | None = None
    championship_event_id: UUID | None = None
    championship_points_required: float | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    enrollment_starts_at: datetime | None = None
    enrollment_ends_at: datetime | None = None
    events: list[Event] | None = None


class V1PremierSeason(BaseModel):
    status: float | None = None
    data: list[Datum2] | None = None


class PartySize(BaseModel):
    max: float | None = None
    min: float | None = None
    invalid: list[float] | None = None
    full_party_bypass: bool | None = None


class HighSkill(BaseModel):
    max_party_size: float | None = None
    min_tier: float | None = None
    max_tier: float | None = None


class MaxTier(BaseModel):
    id: float | None = None
    name: Tiers | None = None


class SkillDisparityItem(BaseModel):
    tier: float | None = None
    name: Tiers | None = None
    max_tier: MaxTier | None = None


class GameRules(BaseModel):
    overtime_win_by_two: bool | None = None
    allow_lenient_surrender: bool | None = None
    allow_drop_out: bool | None = None
    assign_random_agents: bool | None = None
    skip_pregame: bool | None = None
    allow_overtime_draw_vote: bool | None = None
    overtime_win_by_two_capped: bool | None = None
    premier_mode: bool | None = None


class Map4(BaseModel):
    id: UUID | None = None
    name: Maps | None = None


class Map3(BaseModel):
    map: Map4 | None = None
    enabled: bool | None = None


class Datum3(BaseModel):
    mode: Modes | None = None
    mode_id: ModeIds | None = None
    enabled: bool | None = None
    team_size: float | None = None
    number_of_teams: float | None = None
    party_size: PartySize | None = None
    high_skill: HighSkill | None = None
    ranked: bool | None = None
    tournament: bool | None = None
    skill_disparity: list[SkillDisparityItem] | None = None
    required_account_level: float | None = None
    game_rules: GameRules | None = None
    platforms: list[Platforms] | None = None
    maps: list[Map3] | None = None


class V1QueueStatus(BaseModel):
    status: float | None = None
    data: list[Datum3] | None = None


class Tier(MaxTier):
    pass


class Map5(Map4):
    pass


class Season1(BaseModel):
    id: UUID | None = None
    short: Seasons | None = None


class V1LifetimeMmrHistoryItem(BaseModel):
    match_id: UUID | None = None
    tier: Tier | None = None
    map: Map5 | None = None
    season: Season1 | None = None
    ranking_in_tier: float | None = None
    last_mmr_change: float | None = None
    elo: float | None = None
    date: datetime | None = None


class V1LifetimeMmrHistory(BaseModel):
    status: int | None = None
    name: str | None = None
    tag: str | None = None
    results: Results | None = None
    data: list[V1LifetimeMmrHistoryItem] | None = None


class Card1(BaseModel):
    small: str | None = None
    large: str | None = None
    wide: str | None = None
    id: str | None = None


class Data6(BaseModel):
    puuid: str | None = None
    region: str | None = None
    account_level: int | None = None
    name: str | None = None
    tag: str | None = None
    card: Card1 | None = None
    last_update: str | None = None
    last_update_raw: int | None = None


class V1Account(BaseModel):
    status: int | None = None
    data: Data6 | None = None
