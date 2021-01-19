***shared.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable invalidate_cache

    variable debug_events

    variable dev_environment - dynamical set on build

    variable local

    variable home

    variable build

    variable tmp

    variable data_gen

    variable data_gen_exit - default vanilla behaviour

    variable NO_WINDOW

    variable IS_CLIENT

    variable STORAGE_VERSION - the version of the storage format

    variable NO_LOG_ESCAPE

    variable window - the window instance, client-only

    variable world - the world instance

    variable chat - the chat instance todo: migrate to player

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

    variable entity_handler - the entity manager instance

    variable model_handler - the model handler instance, client-only

    variable mod_loader - the mod loader instance

    variable rendering_helper

    variable NEXT_EVENT_BUS_ID

    variable CLIENT_NETWORK_HANDLER

    variable SERVER_NETWORK_HANDLER