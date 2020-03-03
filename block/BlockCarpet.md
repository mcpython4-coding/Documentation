----

**block/BlockCarpet.py - Documentation - Last updated on 02.03.2020 by uuk**

----

The file contains code for creating the carpet's from the color name


    static attribute carpet_bbox: block.BoundingBox.BoundingBox - the bounding box of an carpet
    
    static function create_carpet color: str
        creates an new carpet block-class
        
        class Carpet extends block.Block.Block
            the generated block-class
            
            static overriding attribute NAME: str - the name of the carpet block
            
            overriding function on_block_update
                used to brake carpet when block under the carpet is broken
                
            overriding function is_solid_side side: util.enums.EnumSide
                only the side on the down is solid
                
            overriding function get_view_bbox
                returns the default bbox
                
            static overriding function modify_block_item itemfactory: factory.ItemFactory.ItemFactory
                sets the fuel level of the block