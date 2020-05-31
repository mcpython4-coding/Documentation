***IAllDirectionOrientableBlock.py - documentation - last updated on 6.6.2020 by uuk***
___

    class IAllDirectionOrientableBlock extends mcpython.block.Block.Block

        variable MODEL_FACE_NAME

        function __init__(self, *args, **kwargs)

            variable self.face

                    variable self.face

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        static
        function get_all_model_states(cls) -> list