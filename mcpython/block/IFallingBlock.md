***IFallingBlock.py - documentation - last updated on 8.6.2020 by uuk***
___

    class IFallingBlock extends mcpython.block.Block.Block
        
        base injection class for falling block


        function __init__(self, *args, **kwargs)

            variable self.fall_cooldown

        function on_block_update(self)

        function fall(self, check=True)
            
            let the block fall
            :param check: weither to check if the block can fall to that position or not
