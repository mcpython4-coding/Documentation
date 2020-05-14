***StateHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateHandler

        function __init__(self)

            variable self.states

            variable self.CANCEL_SWITCH_STATE

        function switch_to(self, statename: str or None, immediate=True)

        function _switch_to(self, statename)

            variable self.CANCEL_SWITCH_STATE

            variable self.active_state: State.State

        function add_state(self, state: State.State)

            variable self.states[state.NAME]

        function update_exclusive(self)

    variable handler

    function load()