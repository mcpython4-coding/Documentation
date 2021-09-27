***ExtensionPoint.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractExtensionPoint extends ABC

    class ModLoaderExtensionPoint extends AbstractExtensionPoint
        
        Definition of a mod loader extension point
        Allows you to define custom mod loaders
        NAME: the name of the loader
        The correct loading method will be invoked with the data; The extension point should do the needed stuff


        variable NAME: str

        variable ENABLE_MODS_TOML

        variable ENABLE_MOD_JSON

        variable EXTENSION_POINTS

        static
        function __init_subclass__(cls, **kwargs)

                variable cls.EXTENSION_POINTS[1][cls.NAME]

        static
        function load_mod_from_toml(cls, source_file, data)

        static
        function load_mod_from_json(cls, source_file, data)