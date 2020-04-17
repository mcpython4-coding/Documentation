----

**block/BlockGrassBlock.py - Documentation - Last updated on 17.04.2020 by uuk**

----

These file contains the block-code for the grass block block

    class BlockGrassBlock extends block.Block.Block
        overriding attribute NAME: str - the name of the block
        
        overriding function get_model_state -> dict<str -> str>
            will get the model state of the block
            in this case, {"snowy": "false"} as snow is not implemented yet
            
        overriding function on_random_update
            will update to dirt if needed
