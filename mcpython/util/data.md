***data.py - documentation - last updated on 19.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    Some util functions around data
    Contains methods for simplejson 'ing binary data [for the codec system]
    and a helper function for transforming all mutable lists to immutable tuples in data structures


    function bytes_to_json(data: bytes)

    function json_to_bytes(data: dict) -> bytes

    function lists_to_tuples(data, levels=-1)