***config.py - documentation - last updated on 9.5.2020 by uuk***
___

This file is used for configuration of various parts of the game


    variable MC_VERSION_BASE: str - the version based on

    variable VERSION_TYPE: str - the type of version

    variable VERSION_NAME: str - the name of the version

    variable VERSION_ORDER: typing.List[str]
        list of all versions since 19w52a to indicate order of release; used in save files

    variable FULL_VERSION_NAME: str
        the name of the version as an full name with all information needed

    variable TICKS_PER_SEC: int - how many ticks per second should be executed

    variable WALKING_SPEED: int - how fast to walk

    variable SPRINTING_SPEED: int - how fast to sprint

    variable FLYING_SPEED: int - how fast to fly

    variable FLYING_SPRINTING_SPEED: int - how fast to sprint-fly

    variable GAMEMODE_3_SPEED: int - how fast to fly in gamemode 3

    variable GAMEMODE_3_SPRINTING_SPEED: int - how fast to sprint-fly in gamemode 3

    variable SPEED_DICT: typing.Dict[int,typing.List[int]]

    variable GRAVITY: float - gravity, in -m/s^2 -> speed is calculated with v -= GRAVITY * dt

    variable TERMINAL_VELOCITY: int - maximum speed downwards

    variable MAX_JUMP_HEIGHT: float - About the height of a block. used to determine how height to jump

    variable JUMP_SPEED: float
        To derive the formula for calculating jump speed, first solve
    v_t = v_0 + a * t
    for the time at which you achieve maximum height, where a is the acceleration
    due to gravity and v_t = 0. This gives:
    t = - v_0 / a
    Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
    s = s_0 + v_0 * t + (a * t^2) / 2

    variable PLAYER_HEIGHT: float - the height of the player, in blocks; WARNING: will be removed in the future

    variable _ADVANCED_FACES: typing.List[typing.List[typing.List[typing.Tuple[int,int,int]]]]

    variable ADVANCED_FACES: typing.List[typing.Tuple[int,int,int]]

    variable RANDOM_TICK_RANGE: int - how far to execute random ticks away from player

    variable USE_MISSING_TEXTURES_ON_MISS_TEXTURE: bool
        if missing texture should be used when no texture was selected for an face

    variable CPU_USAGE_REFRESH_TIME: float - how often to refresh cpu usage indicator

    variable FOG_DISTANCE: int - something like view distance, but will no force the chunks to generate

    variable BIOME_HEIGHT_RANGE_MAP: typing.Dict[str,typing.Tuple[int,int]] - an dict of biomename: height range storing the internal height range

    variable CHUNK_GENERATION_RANGE: int
        how far to generate chunks on sector change, in chunks from the chunk the player is in, in an square with
    CHUNK_GENERATION_RANGE * 2 + 1 -size

    variable WRITE_NOT_FORMATTED_EXCEPTION: bool - if exceptions should be not formatted-printed to console by logger
