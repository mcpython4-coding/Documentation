----

**block/BlockDirt.py - Documentation - Last updated on 16.04.2020 by uuk**

----


Code for the dirt-block

    class BlockDirt extends block.Block.Block
        static attribute NAME: str - the name of the block
        
        overriding function on_random_update
            called on random update, will try to convert to grass_block if possible
