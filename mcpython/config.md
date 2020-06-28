***config.py - documentation - last updated on 28.6.2020 by uuk***
___

    variable MC_VERSION_BASE

    variable VERSION_TYPE

    variable VERSION_NAME
        possible: [<pre>]<version>, <normal mc snapshot format>, snapshot dev <number of snapshot> cycle <cycle number>

    variable DEVELOPING_FOR

    variable DEVELOPMENT_COUNTER

    variable VERSION_ORDER
        list of all versions since 19w52a to indicate order of release; used in save files todo: export to other file

    variable FULL_VERSION_NAME

    variable TICKS_PER_SEC - how many ticks per second should be executed, todo: remove (unused)

    variable WALKING_SPEED
        todo: remove definitions of "raw" values

    variable SPRINTING_SPEED

    variable FLYING_SPEED

    variable FLYING_SPRINTING_SPEED

    variable GAMEMODE_3_SPEED

    variable GAMEMODE_3_SPRINTING_SPEED

    variable SPEED_DICT

    variable GRAVITY - gravity, in -m/s^2 -> speed is calculated with v -= GRAVITY * dt

    variable TERMINAL_VELOCITY - maximum speed downwards

    variable MAX_JUMP_HEIGHT - About the height of a block.

    variable JUMP_SPEED
        To derive the formula for calculating jump speed, first solve
        v_t = v_0 + a * t
        for the time at which you achieve maximum height, where a is the acceleration
        due to gravity and v_t = 0. This gives:
        t = - v_0 / a
        Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
        s = s_0 + v_0 * t + (a * t^2) / 2

    variable PLAYER_HEIGHT - the height of the player, in blocks; WARNING: will be removed in the future todo: remove

    variable _ADVANCED_FACES
        todo: move to util.enums

    variable ADVANCED_FACES

    variable RANDOM_TICK_RANGE - how far to execute random ticks away from player

    variable USE_MISSING_TEXTURES_ON_MISS_TEXTURE - if missing texture should be used when no texture was selected for an face

    variable USE_MIP_MAPPING

    variable CPU_USAGE_REFRESH_TIME - how often to refresh cpu usage indicator

    variable FOG_DISTANCE - something like view distance, but will no force the chunks to generate

    variable BIOME_HEIGHT_RANGE_MAP - an dict of biomename: height range storing the internal height range

    variable CHUNK_GENERATION_RANGE
        how far to generate chunks on sector change, in chunks from the chunk the player is in, in an square with
        CHUNK_GENERATION_RANGE * 2 + 1 -size

    variable WRITE_NOT_FORMATTED_EXCEPTION - if exceptions should be not formatted-printed to console by logger

    variable ENABLE_PROFILING

    variable ENABLE_PROFILER_DRAW

    variable ENABLE_PROFILER_TICK

    variable ENABLE_PROFILER_GENERATION

    variable SHUFFLE_DATA

    variable SHUFFLE_INTERVAL

    an list of additional blocks to enable/disable when needed
    WARNING: this content is generated ONTOP of minecraft's content an uses their textures to generate. Please note
            that any of these objects look like original ones, but they are not (currently)
    WARNING: All additional blocks have currently no own loot table for drops. These might change in the future,
            but until than, they are PURELY decorative blocks
    WARNING: As these blocks are not part of the "normal" game, when they are enabled, they may NOT have the same
            behaviour flags build-in than the original ones (think about how an sand slab would behave)
    WARNING: block behaviour is mostly copied from base block and as so, e.g. bedrock slabs are unbreakable in survival
    WARNING (for modders): You might add your own entries onto this table. But make sure that you DO CHECK if they are
                        in the table when you read for block creation. Also note, these file is located in the 
                        minecraft-folder of the config folder.


    variable ENABLED_EXTRA_BLOCKS

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_plank_wall".format(wood)] - Oh, fancy, but what about fences?

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_wool_slab".format(color)]
            colored slabs and walls, why not? (excluding powder as it is something "special")

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_wool_wall".format(color)]

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_concrete_slab".format(color)]

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_concrete_wall".format(color)]

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_stained_glass_slab".format(color)]
            someone asked for more color, here you go!

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_stained_glass_wall".format(color)]

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_terracotta_slab".format(color)]

        variable ENABLED_EXTRA_BLOCKS["minecraft:{}_terracotta_wall".format(color)]

    function load()

        variable config

        variable speeds

        variable physics

        variable timing

        variable rendering

        variable profiler

        variable misc

        variable biomeconfig

        variable block_config

        @G.modloader("minecraft", "stage:mod:config:work")
        function load_data()

            variable USE_MISSING_TEXTURES_ON_MISS_TEXTURE

            variable WRITE_NOT_FORMATTED_EXCEPTION

            variable BIOME_HEIGHT_RANGE_MAP["minecraft:plains"]

            variable ENABLE_PROFILING

            variable ENABLE_PROFILER_DRAW

            variable ENABLE_PROFILER_TICK

            variable ENABLE_PROFILER_GENERATION

            variable SHUFFLE_DATA

            variable SHUFFLE_INTERVAL

                function on_shuffle(dt)

                    variable ENABLED_EXTRA_BLOCKS[key]

                    variable ENABLED_EXTRA_BLOCKS[key]