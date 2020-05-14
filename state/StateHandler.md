***StateHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateHandler
        function __init__(self)
        function switch_to(self, statename: str or None, immediate=True)
        function _switch_to(self, statename)
        function add_state(self, state: State.State)
        function update_exclusive(self)

    variable handler

    function load()