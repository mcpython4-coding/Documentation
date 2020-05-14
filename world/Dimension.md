***Dimension.py - documentation - last updated on 14.5.2020 by uuk***
___

    class DimensionDefinition

        function __init__(self, name: str, config: dict)

            variable self.name

            variable self.id

            variable self.config

        function setStaticId(self, dimid)

            variable self.id

    class DimensionHandler

        function __init__(self)

            variable self.dimensions

            variable self.unfinisheddims

        function finish(self)

            variable i

                variable dim.id

        function add_default_dimensions(self)

        function add_dimension(self, dim: DimensionDefinition)

                variable self.dimensions[dim.id]

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

                variable position

        function get_block(self, position)

            variable chunk

        function add_block(self, position: tuple, blockname

        function remove_block(self, position: tuple, immediate=True, block_update=True, blockupdateself=True)

        function check_neighbors(self, position)

        function show_block(self, position, immediate=True)

        function hide_block(self, position, immediate=True)

        function draw(self)

            variable pad

                    variable chunk

        function __del__(self)