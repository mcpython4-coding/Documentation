***ILog.py - documentation - last updated on 16.5.2020 by uuk***
___

    class ILog extends block.Block.Block
        
        base class for logs


        function __init__(self, *args, **kwargs)

            variable self.axis

        function get_model_state(self): return {"axis"

        function set_model_state(self, state: dict)

        static function get_all_model_states() -> list