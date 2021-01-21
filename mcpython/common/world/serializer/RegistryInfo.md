***RegistryInfo.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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