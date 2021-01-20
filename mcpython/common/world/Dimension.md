***Dimension.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class DimensionDefinition
        
        class for an dimension placeholder


        function __init__(self, name: str, config: dict)
            
            will create an new placeholder
            WARNING: must be send to shared.dimension_handler
            :param name: the dimension name
            :param config: the config for it


            variable self.name

            variable self.id

            variable self.config

        function setStaticId(self, dim_id: int)
            
            will set the id of the dimension (when static)
            :param dim_id: the id for the dimension
            :return: self


    class DimensionHandler
        
        Handler for the dimensions
        Works together with the World-class in handling the system
        This class holds general data about the status of the game dimensions, not for an world instance
        todo: make it fully data-driven


        function __init__(self)

            variable self.dimensions

            variable self.unfinished_dims

        function finish(self)
            
            Called to finish up and assign ids to dynamic dimensions


        function add_default_dimensions(self)
            
            Implementation for mcpython: will add the dimensions used by the core into the system


        function add_dimension(self, dim: DimensionDefinition)
            
            Will add an new dimension definition into the system
            :param dim: the dimension definition to add


        function init_dims(self)
            
            Will create all dimension in the active world


    variable shared.dimension_handler

    class Dimension extends mcpython.common.world.AbstractInterface.IDimension
        
        Class holding a whole dimension
        Default cross-side implementation


        variable BATCH_COUNT
            normal, alpha; mods are free to add more; todo: add better API

        function __init__(self, world_in, dim_id: int, name: str, gen_config=None)
            
            Creates a new dimension. Should be registered to the world instance.
            Can be automated by using the appropriate function at dimension
            :param world_in: the world instance to use
            :param dim_id: the id for it
            :param name: the name for it
            :param gen_config: the config to use for generation


                variable gen_config

            variable self.batches
                batches, see above for usages

            variable self.height_range

        function tick(self)

        function unload_chunk(self, chunk: mcpython.common.world.AbstractInterface.IChunk)

        function get_dimension_range(self) -> typing.Tuple[int, int]

        function get_id(self)

        function get_chunk(
                self,
                cx: typing.Union[int, typing.Tuple[int, int]],
                cz: int = None,
                generate: bool = True,
                create: bool = True,
                ) -> typing.Optional[mcpython.common.world.AbstractInterface.IChunk]:
            
            Used to get an chunk instance with an given position
            :param cx: the chunk x position or an tuple of (x, z)
            :param cz: the chunk z position or None íf cx is tuple
            :param generate: if the chunk should be scheduled for generation if it is not generated
            :param create: if the chunk instance should be created when it does not exist
            :return: the chunk instance or None


        function get_chunk_for_position(
                self,
                position: typing.Union[
                typing.Tuple[float, float, float],
                mcpython.common.block.AbstractBlock.AbstractBlock,
                ],
                **kwargs
                ) -> typing.Optional[mcpython.common.world.AbstractInterface.IChunk]:
            
            Gets an chunk for an position
            :param position: the position to use or the block instance to use
            :param kwargs: same as get_chunk()
            :return: the chunk instance or None


                variable position

        function get_block(
                self, position: typing.Tuple[int, int, int]
                ) -> typing.Union[mcpython.common.block.AbstractBlock.AbstractBlock, str, None]:

            variable chunk

        function add_block(
                self,
                position: tuple,
                block_name: str,
                immediate=True,
                block_update=True,
                block_update_self=True,
                lazy_setup: typing.Callable = None,
                check_build_range=True,
                block_state=None,
                ):

            variable chunk

        function remove_block(
                self, position: tuple, immediate=True, block_update=True, block_update_self=True
                ):

            variable chunk

        function check_neighbors(self, position: typing.Tuple[int, int, int])

        function show_block(self, position, immediate=True)

        function hide_block(self, position, immediate=True)

        function draw(self)

            variable pad

                    variable chunk

        function __del__(self)

        function get_world_generation_config_for_layer(self, layer_name: str)

        function set_world_generation_config_for_layer(self, layer_name, layer_config)

        function get_world_generation_config_entry(self, name: str, default=None)

        function set_world_generation_config_entry(self, name: str, value)

        function get_name(self) -> str