***shared.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable launch_wrapper

    variable profiler

    variable invalidate_cache

    variable dev_environment - dynamical set on build

    variable NO_LOG_ESCAPE

    variable local

    variable home

    variable build

    variable tmp

    variable data_gen

    variable data_gen_exit - default vanilla behaviour

    variable NO_WINDOW

    variable IS_CLIENT

    variable IS_NETWORKING

    variable IS_TEST_ENV

    variable ENABLE_ANIMATED_TEXTURES

    variable CURRENT_EVENT_SUB
        Used by the mod loading system to store the name of the mod doing stuff currently
        Only updated when currently loading the game

    variable CURRENT_REF_MAP
        The current mixin ref map, used by the JVM when needed

    variable STORAGE_VERSION - the version of the storage format

    variable window
        the window instance, client-only

    variable chat
        the chat instance, client only todo: migrate to player

    variable world - the world instance

    variable event_handler - the global event handler

    variable tick_handler - the global tick handler

    variable registry - the registry manager

    variable command_parser - the command parser

    variable state_handler - the state manager

    variable inventory_handler - the inventory manager instance

    variable world_generation_handler - the world generator manager instance

    variable biome_handler - the biome manger instance

    variable crafting_handler - the crafting manager instance

    variable tag_handler - the tag handler instance

    variable dimension_handler - the dimension handler instance

    variable loot_table_handler - the loot table manager instance

    variable entity_manager - the entity manager instance

    variable capability_manager - the capability manager instance

    variable model_handler - the model handler instance, client-only

    variable mod_loader - the mod loader instance

        variable rendering_helper

        variable rendering_helper

    variable NEXT_EVENT_BUS_ID

    variable CLIENT_NETWORK_HANDLER

    variable SERVER_NETWORK_HANDLER

    variable NETWORK_MANAGER

    variable ENABLE_MOD_LOADER

    variable ENABLE_DATAPACK_LOADER

    variable ENABLE_RESOURCE_PACK_LOADER