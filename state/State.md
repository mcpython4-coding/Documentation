***State.py - documentation - last updated on 14.5.2020 by uuk***
___

    class State extends event.Registry.IRegistryContent

        static function is_mouse_exclusive()

        function __init__(self)

            variable self.parts

            variable self.eventbus

                variable statepart.master - StateParts get an list of steps to get to them as an list

        function activate(self)

        function deactivate(self)

        function bind_to_eventbus(self)

        function get_parts(self) -> list

        function on_activate(self):  # todo

        function on_deactivate(self):  # todo