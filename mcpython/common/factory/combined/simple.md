***simple.py - documentation - last updated on 25.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    function colorize_texture(
            factory: "CombinedFactoryInstance",
            image: PIL.Image.Image,
            color: typing.Tuple[int, int, int, int],
            ) -> PIL.Image.Image:

    class CombinedFactoryInstance
        
        Factory system for constructing a whole block/item group at ones
        This is the simple variant, allowing for configuration and than single block construction
        todo: add a variant with template system for defining e.g. wood which than construct all needed wood items for
            it


        variable FILE_COUNTER

        function __init__(
                self,
                target_base_name: str,
                default_texture: str = "assets/missing_texture.png",
                color: typing.Tuple[int, int, int, int] = None,
                color_texture_consumer: typing.Callable[
                [
                "CombinedFactoryInstance",
                PIL.Image.Image,
                typing.Tuple[int, int, int, int],
                ],
                PIL.Image.Image,
                ] = colorize_texture,
                ):

            variable default_texture: str
            
            Creates a new CombinedFactoryInstance instance
            :param target_base_name: the base name of the block
            :param default_texture: the default texture file
            :param color: a optional color to color the texture in
            :param color_texture_consumer: a consumer for colorizing the textures


            variable self.target_base_name

            variable self.default_texture

            variable self.color

            variable self.color_texture_consumer

        function create_colored_texture(
                self, texture: typing.Union[PIL.Image.Image, str], color=None
                ):
            
            Helper function for colorizing the texture at runtime
            :param texture: the texture to transform
            :param color: optional: the color, when differing from color attribute


                variable texture

            variable file

                variable color

        function create_full_block(self, suffix=None, texture=None, color=None, **consumers)
            
            Creates a full block using the "minecraft:block/cube_all"-model
            :param suffix: suffix for the name, when None, the name itself is used, when not None, a _ is inserted in
                between
            :param texture: the texture to use, None for default
            :param color: color to use for colorizing; None for default
            :param consumers: the consumers send to create_block_simple()


        function create_block_simple(
                self,
                name: str,
                textures=None,
                block_parent="minecraft:block/block",
                model_info=None,
                block_factory_consumer: typing.Callable[
                ["CombinedFactoryInstance", typing.Any], None
                ] = None,
                block_model_consumer: typing.Callable[
                ["CombinedFactoryInstance", dict], dict
                ] = None,
                item_model_consumer: typing.Callable[
                ["CombinedFactoryInstance", dict], dict
                ] = None,
                block_state_consumer: typing.Callable[
                ["CombinedFactoryInstance", dict], dict
                ] = None,
                ):
            
            Helper method for creating a full set of block & item with needed data
            Use the consumers to modify the generated content if you need to
            :param name: the name of the block/item
            :param textures: the textures to use
            :param block_parent: the block model parent
            :param block_factory_consumer: a consumer taking a BlockFactory
            :param block_model_consumer: a consumer for the block model data, returning modified data
            :param item_model_consumer: a consumer for the item model data, returning modified data
            :param block_state_consumer: a consumer for the block state data, returning modified data


            variable mod_name

                variable mod_name

            variable model_name

            @shared.mod_loader(mod_name, "stage:block:factory_usage")
            function block_instance()

                variable instance

                @shared.mod_loader(mod_name, "stage:model:model_search")
                function block_model()

                @shared.mod_loader(mod_name, "stage:model:blockstate_search")
                function block_state()

        function generate_log_like(
                self,
                suffix=None,
                front_texture=None,
                side_texture=None,
                color=None,
                **consumers,
                ):
            
            Creates a set for a log like block
            :param suffix: the name suffix
            :param front_texture: the front texture
            :param side_texture: the side texture
            :param color: the color for the texture
            :param consumers: consumers for the data


                variable front_texture

                variable side_texture

            variable name

            variable front_texture

            variable side_texture

            variable textures

        function create_button_block(self, suffix=None, texture=None, color=None, **consumers)

                variable mod_name

                    variable mod_name

                @shared.mod_loader(mod_name, "stage:model:model_search")
                function generate_models()

        function create_slab_block(self, suffix=None, texture=None, color=None, **consumers)

        function create_multi_variant_block(
                self,
                name: str,
                *states,
                block_factory_consumer: typing.Callable[
                ["CombinedFactoryInstance", typing.Any], None
                ] = None,
                block_state_consumer: typing.Callable[
                ["CombinedFactoryInstance", dict], dict
                ] = None,
                block_state_parent=None,
                block_state_alias=None,
                ):

            variable mod_name

                variable mod_name

            variable model_name

            @shared.mod_loader(mod_name, "stage:block:factory_usage")
            function block_instance()

                variable instance

                @shared.mod_loader(mod_name, "stage:model:model_search")
                function block_model()

                @shared.mod_loader(mod_name, "stage:model:blockstate_search")
                function block_state()

                        variable data["parent"]

                        variable data["alias"]

                        variable data

        function create_wall(self, suffix=None, texture=None, color=None, **consumers)

        function create_multipart_block(
                self,
                name: str,
                *parts,
                block_factory_consumer: typing.Callable[
                ["CombinedFactoryInstance", typing.Any], None
                ] = None,
                block_state_consumer: typing.Callable[
                ["CombinedFactoryInstance", dict], dict
                ] = None,
                ):

            variable mod_name

                variable mod_name

            variable model_name

            @shared.mod_loader(mod_name, "stage:block:factory_usage")
            function block_instance()

                variable instance

                @shared.mod_loader(mod_name, "stage:model:model_search")
                function block_model()

                @shared.mod_loader(mod_name, "stage:model:blockstate_search")
                function block_state()

        function inner_generate_model(self, variant, model_name: str)

            variable data

                variable data