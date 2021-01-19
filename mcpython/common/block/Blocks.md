***Blocks.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    function remove_if_downer_block_not_solid(instance)
        
        Helper function for downer implementation.
        Will remove THIS block when the block below is air or an not-generated block
        :param instance: the block-instance to check


    function load_blocks()

    @shared.mod_loader("minecraft", "stage:combined_factory:blocks")
    function combined_load()

    function load_misc(generator: DataGeneratorInstance)

        function set_purpur_block(_, factory)

    function load_wood(generator: DataGeneratorInstance)

        function set_stem(_, factory)

        function set_leaves(_, factory)

    function load_value_ables(generator: DataGeneratorInstance)

        function set_material_block(_, factory)

    function load_stones(generator: DataGeneratorInstance)

        function set_basalt(_, factory)

        function set_bedrock(_, factory)

        function set_end_stone(_, factory)

        function set_dirt(_, factory)

        function set_obsidian(_, factory)

        function set_fall_able(_, factory)

    function load_colored(generator: DataGeneratorInstance)

        function set_concrete_powder(_, factory)

        function set_terracotta(_, factory)

        function set_wool(_, factory)

        function set_stained_glass(_, factory)

        function set_brick(_, factory)