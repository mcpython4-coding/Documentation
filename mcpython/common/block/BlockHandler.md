***BlockHandler.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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
