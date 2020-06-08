***State.py - documentation - last updated on 8.6.2020 by uuk***
___

    class State extends mcpython.event.Registry.IRegistryContent
        
        base class


        variable IS_MOUSE_EXCLUSIVE

        variable CONFIG_LOCATION - default location: data/{mod}/states/{name}.json

        static
        function is_mouse_exclusive(cls):  # todo: make attribute
                return cls.IS_MOUSE_EXCLUSIVE
                
                def __init__(self):

        function __init__(self)

            variable self.part_dict

            variable self.parts - todo: remove

            variable self.eventbus

                variable statepart.master - StateParts get an list of steps to get to them as an list

        function activate(self)

        function deactivate(self)

        function on_deactivate(self):  # todo: remove
                pass
                
                