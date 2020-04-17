----

**block/BlockFence.py - Documentation - Last updated on 16.04.2020 by uuk**

----


class for every fence

    class IFence extends block.Block.Block
        
        static attribute FENCE_TYPE_NAME: set - an list of type-names used for connecting
        
        static attribute BBOX - unused attribute to set the bounding box from
        
        attribute connections: dict<str[face name] -> bool> - an dict representing the connections
        
        overriding attribute BLOCK_ITEM_GENERATOR_STATE: dict<str[face name] -> str[bool.lower()]> - the state for block item gen
        
        overriding function __init__ [...]
            construct an new fence-object 
            
        overriding function get_model_state -> dict
            returns the constructed model state from the attribute connections
            
        overriding function on_block_update
            will update connections & visible state
            
        overriding set_model_state state: dict
            deserializes the previous stored data
            
        function connects_to face: util.enums.EnumSide blockinstance: block.Block.Block -> bool
            will check if connecting to
            
    class IWoodenFence extends block.BlockFence.IFence
        overriding attribute FENCE_TYPE_NAME: set - the wooden fence type
        
    class AcaciaFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
        
    class BirchFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
    
    class DarkOakFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
    
    class JungleFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
    
    class OakFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
    
    class SpruceFence extends block.BlockFence.IWoodenFence
        overriding attribute NAME: str - the name of the block
        
    class NetherBrickFence extends block.BlockFence.IFence
        overriding attribute NAME: str - the name of the block
        
        overriding attribute FENCE_TYPE_NAME: set - the fence type

