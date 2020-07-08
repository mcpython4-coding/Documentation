***StateHandler.py - documentation - last updated on 8.6.2020 by uuk***
___

    class StateHandler

        function __init__(self)

            variable self.states

            variable self.CANCEL_SWITCH_STATE

        function switch_to(self, statename: str, immediate=True)

        function _switch_to(self, statename: str)

        function add_state(self, state_instance: State.State)

        function update_exclusive(self)

    variable handler

    function load()