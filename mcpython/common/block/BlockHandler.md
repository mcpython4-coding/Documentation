***BlockHandler.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable tag_holder

    function register_block(registry, cls)

            variable name

            variable block_registry.full_table[name]

            variable block_registry.full_table[name.split(":")[-1]]

            variable instance

                variable cls.IS_SOLID

                variable cls.CAN_CONDUCT_REDSTONE_POWER

                variable cls.CAN_MOBS_SPAWN_ON

    variable block_registry

    variable block_registry.full_table - an table of localized & un-localized block names

    function load()
        
        loads all blocks that should be loaded, only the ones for blocks may be loaded somewhere else