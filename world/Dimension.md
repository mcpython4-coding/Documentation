***Dimension.py - documentation - last updated on 14.5.2020 by uuk***
___

    class DimensionDefinition
        function __init__(self, name: str, config: dict)
        function setStaticId(self, dimid)

    class DimensionHandler
        function __init__(self)
        function finish(self)
        function add_default_dimensions(self)
        function add_dimension(self, dim: DimensionDefinition)
        function init_dims(self)

    variable G.dimensionhandler


    class Dimension
        function __init__(self, world, id, name: str, genconfig={})
        function get_chunk(self, cx, cz, generate=True, create=True) -> world.Chunk.Chunk or None
        function get_chunk_for_position(self, position, **kwargs) -> world.Chunk.Chunk or None
        function get_block(self, position)
        function add_block(self, position: tuple, blockname
        function remove_block(self, position: tuple, immediate=True, block_update=True, blockupdateself=True)
        function check_neighbors(self, position)
        function show_block(self, position, immediate=True)
        function hide_block(self, position, immediate=True)
        function draw(self)
        function __del__(self)