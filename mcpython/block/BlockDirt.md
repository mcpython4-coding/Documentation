***BlockDirt.py - documentation - last updated on 26.7.2020 by uuk***
___

    class BlockDirt extends Block.Block
        
        base class for dirt
        todo: implement -> grass convert


        variable NAME: str

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable BEST_TOOLS_TO_BREAK

        variable ENABLE_RANDOM_TICKS

        function on_random_update(self)

    @G.modloader("minecraft", "stage:block:load")
    function load()