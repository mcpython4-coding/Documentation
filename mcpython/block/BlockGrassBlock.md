***BlockGrassBlock.py - documentation - last updated on 26.7.2020 by uuk***
___

    class BlockGrassBlock extends Block.Block
        
        base class for grass


        variable NAME

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable BEST_TOOLS_TO_BREAK

        variable ENABLE_RANDOM_TICKS

        function get_model_state(self) -> dict

        function on_random_update(self)

    @G.modloader("minecraft", "stage:block:load")
    function load()