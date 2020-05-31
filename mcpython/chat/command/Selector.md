***Selector.py - documentation - last updated on 6.6.2020 by uuk***
___

    class Selector extends mcpython.event.Registry.IRegistryContent
        
        selector base class


        variable TYPE

        static
        function is_valid(entry) -> bool

        static
        function parse(entry, config)

    function load()

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @G.registry class PlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @G.registry class RandomPlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @G.registry class AllPlayerSelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)

        @G.registry class EntitySelector extends Selector

            variable NAME

            static
            function is_valid(entry) -> bool

            static
            function parse(entry, config)