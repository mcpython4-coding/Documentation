***Dimension.py - documentation - last updated on 6.6.2020 by uuk***
___

    class DimensionDefinition
        
        class for an dimension placeholder


        function __init__(self, name: str, config: dict)
            
            will create an new placeholder
            WARNING: must be send to G.dimensionhandler
            :param name: the dimension name
            :param config: the config for it


            variable self.name

            variable self.id

            variable self.config

        function setStaticId(self, dimid: int)
            
            will set the id of the dimension (when static)
            :param dimid: the id for the dimension
            :return: self


    class DimensionHandler
        
        Handler for the dimensions
        Works together with the World-class in handling the system
        This class holds general data about the status of the game dimensions, not for an world instance


        function __init__(self)

            variable self.dimensions

            variable self.unfinisheddims

        function finish(self)
            
            called to finish up and assign ids to dynamic dimensions


        function add_default_dimensions(self)
            
            implementation for mcpython: will add the dimensions used by the core into the system


        function add_dimension(self, dim: DimensionDefinition)
            
            will add an new dimension definition into the system
            :param dim: the dimension defintion to add


        function init_dims(self)
            
            will create all dimension in the active world


    variable G.dimensionhandler

    class Dimension
        
        class holding an whole dimension


        function __init__(self, world_in, dim_id: int, name: str, genconfig=None)
            
            Creates an new dimension. Must be send also to the World-instance
            :param world_in: the world instance to use
            :param dim_id: the id for it
            :param name: the name for it
            :param genconfig: the config to use for generation


            variable self.id

            variable self.world

            variable self.chunks

            variable self.name

            variable self.worldgenerationconfig

            variable self.worldgenerationconfigobjects

            variable self.batches - normal, alpha
                normal batch

        function get_chunk(self, cx: typing.Union[int, typing.Tuple[int, int]], cz: int = None, generate: bool = True,
                create: bool = True) -> typing.Union[mcpython.world.Chunk.Chunk, None]:
            
            used to get an chunk instance with an given position
            :param cx: the chunk x position or an tuple of (x, z)
            :param cz: the chunk z position or None íf cx is tuple
            :param generate: if the chunk should be scheduled for generation if it is not generated
            :param create: if the chunk instance should be created when it does not exist
            :return: the chunk instance or None


        function get_chunk_for_position(self,
                position: typing.Union[typing.Tuple[float, float, float], mcpython.block.Block.Block],
                **kwargs) -> typing.Union[mcpython.world.Chunk.Chunk, None]:
            
            gets an chunk for an position
            :param position: the position to use or the block instance to use
            :param kwargs: same as get_chunk()
            :return: the chunk instance or None


        @deprecation.deprecated("dev1-4", "a1.3.0")
        function get_block(self, position: typing.Tuple[int, int, int]) -> typing.Union[mcpython.block.Block.Block, str, None]

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function add_block(self, position: tuple, blockname: str, immediate=True, block_update=True, blockupdateself=True,
                args=[], kwargs={}):

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function remove_block(self, position: tuple, immediate=True, block_update=True, blockupdateself=True)

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function check_neighbors(self, position: typing.Tuple[int, int, int])

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function show_block(self, position, immediate=True)

        @deprecation.deprecated("dev1-4", "a1.3.0")
        function hide_block(self, position, immediate=True)

        function draw(self)

        function __del__(self)