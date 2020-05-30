***Dimension.py - documentation - last updated on 30.5.2020 by uuk***
___

    class DimensionDefinition

        function __init__(self, name: str, config: dict)

            variable self.name

            variable self.id

            variable self.config

        function setStaticId(self, dimid)

    class DimensionHandler

        function __init__(self)

            variable self.dimensions

            variable self.unfinisheddims

        function finish(self)

        function add_default_dimensions(self)

        function add_dimension(self, dim: DimensionDefinition)

        function init_dims(self)

    variable G.dimensionhandler

    class Dimension

        function __init__(self, world, id, name: str, genconfig={})

            variable self.id

            variable self.world

            variable self.chunks

            variable self.name

            variable self.worldgenerationconfig

            variable self.worldgenerationconfigobjects

            variable self.batches - normal, alpha
                normal batch

        function get_chunk(self, cx, cz, generate=True, create=True) -> world.Chunk.Chunk or None

        function get_chunk_for_position(self, position, **kwargs) -> world.Chunk.Chunk or None

        function get_block(self, position)

        function add_block(self, position: tuple, blockname: str, immediate=True, block_update=True, blockupdateself=True,
                args=[], kwargs={}):

        function remove_block(self, position: tuple, immediate=True, block_update=True, blockupdateself=True)

        function check_neighbors(self, position): self.get_chunk_for_position(position).check_neighbors(position)
                
                def show_block(self, position, immediate=True):

        function show_block(self, position, immediate=True)

        function hide_block(self, position, immediate=True)

        function draw(self)

        function __del__(self)