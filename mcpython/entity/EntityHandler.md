***EntityHandler.py - documentation - last updated on 15.7.2020 by uuk***
___

    class EntityHandler
        
        Handler for entities in the current world


        function __init__(self)

            variable self.registry

            variable self.entity_map

        function add_entity(self, name, position, *args, dimension=None, uuid=None, check_summon=False, **kwargs)

        function tick(self)

    variable G.entityhandler

    function load()