***BlockNetherPortal.py - documentation - last updated on 26.7.2020 by uuk***
___

    class NetherPortalBlock extends mcpython.block.Block.Block
        
        class for an nether portal


        variable PORTAL_HOLDING_BLOCKS

        variable NAME

        variable NO_COLLISION

        variable SOLID

        variable HARDNESS

        function __init__(self, *args, **kwargs)

            variable self.axis

                variable self.face_solid[key]

        function set_model_state(self, state: dict): self.axis = state.setdefault("axis", "x")
                
                @staticmethod
                def get_all_model_states() -> list: return [{"axis": "x"}, {"axis": "z"}]
                
                def on_block_update(self):

        static
        function get_all_model_states() -> list: return [{"axis": "x"}, {"axis": "z"}]
                
                def on_block_update(self):

        function on_block_update(self)

        function check_valid_surrounding(self)

        function check_valid_block(self, position: tuple, chunk=None)

        function on_no_collide_collide(self, player, previous: bool)

                variable player.in_nether_portal_since

    @G.modloader("minecraft", "stage:block:load")
    function load()