***BlockCarpet.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable carpet_bbox

    class ICarpet extends mcpython.block.Block.Block
        
        base class for every carpet


        function __init__(self, *args, **kwargs)
            
            creates an new carpet class


            variable self.face_solid

        function on_block_update(self)

        function get_view_bbox(self): return carpet_bbox
                
                @classmethod
                def modify_block_item(cls, itemfactory):

        static
        function modify_block_item(cls, itemfactory)

    function create_carpet(carpet_color: str)
        
        generator function for carpets. Will create an new class for an carpet
        :param carpet_color: the color name of the carpet
        :return: the generated class


        @G.registry class Carpet extends ICarpet

            variable NAME: str - the name of the block