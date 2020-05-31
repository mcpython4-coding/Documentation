***Entity.py - documentation - last updated on 6.6.2020 by uuk***
___

    class Entity extends mcpython.event.Registry.IRegistryContent
        
        dummy class for every entity,
        only used by the player at the moment (as no more entities are implemented)
        feel free to use, general functions for cross-mod work


        variable TYPE

        variable SUMMON_ABLE - if the entity can be used in /summom-command

        static
        function create_new(cls, position, *args, **kwargs)
            
            creates an new entity and set up it correctly for later use
            :param position: the position to create at
            :param args: args to send to the constructor
            :param kwargs: kwargs to send to the constructor
            :return: the created entity
            todo: make added to world
            for moder: use this rather than raw constructor


        function __init__(self, dimension=None)
            
            creates an new entity for the world
            for moder: you SHOULD implement an custom constructor which set the bellow values to an "good" value


            variable self.dimension

            variable self.__position

            variable self.rotation

            variable self.inventories

            variable self.harts

            variable self.chunk

            variable self.uuid

            variable self.movement

        function __del__(self)

        function __str__(self)

        function set_position(self, position: tuple): self.teleport(position)
                
                # only for some small use-cases. WARNING: will  N O T  do any internal handling for updating the position
                def set_position_unsafe(self, position: tuple): self.__position = position
                
                def teleport(self, position, dimension=None, force_chunk_save_update=False):

        function set_position_unsafe(self, position: tuple): self.__position = position
                
                def teleport(self, position, dimension=None, force_chunk_save_update=False):

        function teleport(self, position, dimension=None, force_chunk_save_update=False)
            
            called when the entity should be teleported
            :param position: the position to teleport to
            :param dimension: to which dimension-id to teleport to, if None, no dimension change is used
            :param force_chunk_save_update: if the system should force to update were player data is stored


        variable position

        function tell(self, msg: str)
            
            tells the entity an message. Not intended to inter-mod com
            Should be used by say-commands
            :param msg: the msg to tell


        function kill(self, drop_items=True, kill_animation=True)
            
            called to kill the entity [remove the entity from world]
            :param drop_items: if items should be dropped
            :param kill_animation: if the kill animation should be played
            todo: drop items


        function pick_up(self, itemstack: mcpython.gui.ItemStack.ItemStack) -> bool
            
            let the entity pick up an item and insert it into its inventory
            :param itemstack: the itemstack to use
            :return: if it was successful or not
            for moder: see world/player.py as an example how this could work


        function damage(self, damage, reason=None)
            
            applies damage to the entity
            FOR MODER:
                this function is an default implementation. for an working example, see the player entity
                - you may want to apply armor calculation code
                - you may want to override this method for an custom implementation
            :param damage: the damage to apply
            :param reason: the reason for the damage, may be entity or str [something like DamageSource in mc]


        function on_interact(self, player, button, modifiers, itemstack)
            
            called when the player tries to interact with the entity
            :param player: the player doing so, WARNING: only type-hinted for entity, not world/player.py:Player
            :param button: the button used
            :param modifiers: the modifiers used
            :param itemstack: the itemstack held in hand
            todo: make called
            todo: damage entity when needed
            for moder: should damage entity if needed


        function get_inventories(self) -> list
            
            will return an list of all currently arrival inventories for this entity
            :return:


        function draw(self)
            
            called to draw the entity


        function tick(self)
            
            called every tick to update the entity
            can be used to update animations, movement, do path finding stuff, damage other entities, ...


        function dump(self)
            
            dumps the entity into an save-able version
            :return: an pickle-able version, excluding position, rotation and harts, should include inventory serializer
                calls to make sure that everything works


        function load(self, data)
            
            loads data into the entity, previous saved
            For Moder:
                you CAN include an version entry to make sure you can fix the data version
            :param data: the data to load from
