***CombinedBlockFactory.py - documentation - last updated on 29.7.2020 by uuk***
___

    variable WALL_TEMPLATE

    variable SLAB_TEMPLATE

    function generate_full_block_slab_wall(config: mcpython.datagen.Configuration.DataGeneratorConfig, name: str,
            texture: str = None, enable=(True, True, True), callback=None,
            slab_name=None, wall_name=None, generate_recipes=(True, True), textures=None):

    function generate_full_block(config, name: str, texture: str = None, callback=None)

    function generate_slab_block(config, name: str, texture: str = None, callback=None, generate_recipe=True, full=None)

    function generate_wall_block(config, name: str, texture: str = None, callback=None, generate_recipe=True)

    function generate_log_block(config, name: str, front_texture: str = None, side_texture: str = None, callback=None)

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

        function __init__(self, modname=None, config=None, on_create_callback=None)

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

        function __init__(self, texture: str, modname=None, config=None, on_create_callback=None, full_model=None)
            
            will create an n ew CombinedSlabFactory
            :param texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param config: the config to use
            :param on_create_callback: callback when BlockFactory is active
            :param full_model: the model for the full block, if existent


        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    class CombinedWallFactory
        
        CombinedFactory for walls


        variable GLOBAL_NAME

        function __init__(self, texture: str, modname=None, config=None, on_create_callback=None)
            
            will create an n ew CombinedWallFactory
            :param texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param config: the config to use
            :param on_create_callback: callback when BlockFactory is active


        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    class CombinedLogFactory
        
        CombinedFactory for logs


        variable GLOBAL_NAME

        function __init__(self, front_texture: str, side_texture: str, modname=None, config=None, on_create_callback=None)
            
            will create an new CombinedWallFactory
            :param texture: the texture for the slab
            :param modname: the modname, if not set globally
            :param config: the config to use
            :param on_create_callback: callback when BlockFactory is active


        function set_name(self, name: str)

        function build(self)

        function __generate_data_gen(self)

        function __generate_factories(self)

    function set_global_mod_name(modname: typing.Union[str, None])