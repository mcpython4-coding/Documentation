***FallingBlockEntity.py - documentation - last updated on 20.7.2020 by uuk***
___

    @G.registry class FallingBlock extends mcpython.entity.Entity.Entity
        
        Class for the falling block entity


        variable NAME

        function __init__(self, *args, representing_block: mcpython.block.Block.Block = None, **kwargs)

            variable self.block - todo: store in nbt

            variable self.nbt_data["motion"]

        function draw(self)

        function tick(self)

        function kill(self, *args, **kwargs)