***Selector.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Selector extends mcpython.common.event.Registry.IRegistryContent
        
        Selector base class


        variable TYPE

        static
        function is_valid(entry) -> bool

        static
        function parse(entry, config)

    function load()

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @shared.registry class PlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @shared.registry class RandomPlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @shared.registry class AllPlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @shared.registry class EntitySelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)