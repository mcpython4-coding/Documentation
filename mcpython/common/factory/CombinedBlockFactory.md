***CombinedBlockFactory.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable WALL_TEMPLATE

    variable SLAB_TEMPLATE

    function generate_full_block_slab_wall(
            generator: DataGeneratorInstance,
            name: str,
            texture: str = None,
            enable=(True, True, True),
            callback=None,
            slab_name=None,
            wall_name=None,
            generate_recipes=(True, True),
            textures=None,
            ):

            variable texture

            variable slab_name

            variable wall_name

            variable enable

    function generate_full_block(generator, name: str, texture: str = None, callback=None)

    function generate_slab_block(
            generator,
            name: str,
            texture: str = None,
            callback=None,
            generate_recipe=True,
            full=None,
            ):

            variable texture

            variable full

    function generate_wall_block(
            generator, name: str, texture: str = None, callback=None, generate_recipe=True
            ):

            variable texture

    function generate_log_block(
            generator,
            name: str,
            front_texture: str = None,
            side_texture: str = None,
            callback=None,
            ):

            variable front_texture

            variable side_texture

    class CombinedFullBlockFactoryMode extends enum.Enum
        
        enum representing different "kinds" of cubes for the CombinedFullBlockFactory


        variable CUBE

        variable CUBE_ALL

        variable BOTTOM_TOP

        variable COLUMN

        variable COLUMN_HORIZONTAL

        variable DIRECTIONAL

        variable TOP

        function __init__(self, parent_name: str, texture_names: set)

            variable self.parent

            variable self.texture_names

    class CombinedFullBlockFactory
        
        Factory for creating any kind of blocks with only one model (like any full blocks).
        This does NOT include slabs as they are based on two models


        variable GLOBAL_NAME

        function __init__(
                self, modname: str, generator: DataGeneratorInstance, on_create_callback=None
                ):

                variable modname

            variable self.generator

            variable self.mode

            variable self.textures

            variable self.modname

            variable self.name

            variable self.on_create_callback

        function set_name(self, name: str)

        function setMode(self, mode: CombinedFullBlockFactoryMode)

        function setTextureVariable(self, name: str, location: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    class CombinedSlabFactory
        
        CombinedFactory for slabs


        variable GLOBAL_NAME

        variable SLAB_TEXTURES

        function __init__(
                self,
                texture: str,
                modname: str,
                generator: DataGeneratorInstance,
                on_create_callback=None,
                full_model=None,
                ):
            
            will create an n ew CombinedSlabFactory
            :param texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param generator: the generator to use
            :param on_create_callback: callback when BlockFactory is active
            :param full_model: the model for the full block, if existent


            variable self.generator

            variable self.texture

            variable self.modname

            variable self.name

            variable self.on_create_callback

            variable self.full_model

        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    class CombinedWallFactory
        
        CombinedFactory for walls


        variable GLOBAL_NAME

        function __init__(
                self,
                texture: str,
                modname: str,
                generator: DataGeneratorInstance,
                on_create_callback=None,
                ):
            
            will create an n ew CombinedWallFactory
            :param texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param generator: the config to use
            :param on_create_callback: callback when BlockFactory is active


            variable self.generator

            variable self.texture

            variable self.modname

            variable self.name

            variable self.on_create_callback

        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    class CombinedLogFactory
        
        CombinedFactory for logs


        variable GLOBAL_NAME

        function __init__(
                self,
                front_texture: str,
                side_texture: str,
                modname: str,
                generator: DataGeneratorInstance,
                on_create_callback=None,
                ):
            
            will create an new CombinedWallFactory
            :param front_texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param generator: the config to use
            :param on_create_callback: callback when BlockFactory is active


            variable self.generator

            variable self.front_texture

            variable self.side_texture

            variable self.modname

            variable self.name

            variable self.on_create_callback

        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    function set_global_mod_name(modname: typing.Union[str, None])