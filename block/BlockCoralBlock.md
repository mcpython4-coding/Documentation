----

**block/BlockCoralBlock.py - Documentation - Last updated on 03.03.2020 by uuk**

----

This file contains the base class for every coral & the coral block declaration


    class ICoralBlock extends block.Block.Block
        Base class for every coral block
        
        overriding function on_random_update
            will transform the block to dead variant
            
    class BrainCoralBlock & BubbleCoralBlock & FireCoralBlock & HornCoralBlock & TubeCoralBlock extends ICoralBlock
        block-classes for living coral block
        
    Code for constructing the dead variants