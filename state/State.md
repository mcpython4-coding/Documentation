***State.py - documentation - last updated on 26.5.2020 by uuk***
___

    class State extends event.Registry.IRegistryContent
        
        base class


        variable IS_MOUSE_EXCLUSIVE

        variable CONFIG_LOCATION - default location: data/{mod}/states/{name}.json

        static function is_mouse_exclusive(cls):  # todo

        function __init__(self)

            variable self.part_dict

            variable self.parts - todo: remove

            variable self.eventbus

                variable statepart.master - StateParts get an list of steps to get to them as an list

        function activate(self)

        function deactivate(self)

        function bind_to_eventbus(self):  # todo

        function get_parts(self) -> list:  # todo

        function on_activate(self):  # todo

        function on_deactivate(self):  # todo