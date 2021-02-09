***RegistryInfo.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class RegistryInfo extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer
        
        Serializer storing the content of various registries


        variable PART

        static
        function load(cls, save_file)

            variable type_change_builder

            variable registry_miss_match

                variable registry_miss_match[registry.name]

                    variable entries

                        variable compressed

        static
        function save(cls, data, save_file)