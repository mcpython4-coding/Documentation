***BlockCoralBlock.py - documentation - last updated on 8.6.2020 by uuk***
___

    class ICoralBlock extends mcpython.block.Block.Block
        
        base class for every coral block


        variable ENABLE_RANDOM_TICKS

        function on_random_update(self)

    @G.registry class BrainCoralBlock extends ICoralBlock
        
        class for brain coral block


        variable NAME: str

    @G.registry class BubbleCoralBlock extends ICoralBlock
        
        class for bubble coral block


        variable NAME: str

    @G.registry class FireCoralBlock extends ICoralBlock
        
        class for fire coral block


        variable NAME: str

    @G.registry class HornCoralBlock extends ICoralBlock
        
        class for horn coral block


        variable NAME: str

    @G.registry class TubeCoralBlock extends ICoralBlock
        
        class for tube coral block


        variable NAME: str