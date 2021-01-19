***General.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class WorldConfigFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, save_file, data: dict) -> dict

    class WorldGeneralFixer extends mcpython.common.world.datafixers.IDataFixer.IPartFixer
        
        Class representing an fix for the config-entry


        variable TARGET_SERIALIZER_NAME

        static
        function fix(cls, save_file, data: dict) -> dict

    @shared.registry class General extends mcpython.common.world.serializer.IDataSerializer.IDataSerializer

        variable PART

        static
        function apply_part_fixer(cls, save_file, fixer)

                variable data

                variable data["config"]

                variable data

                variable data

        static
        function load(cls, save_file)

            variable save_file.version

            variable player_name

            variable shared.world.config

            variable wd

            variable mcpython.server.worldgen.noise.NoiseManager.manager.default_implementation

        static
        function save(cls, data, save_file)