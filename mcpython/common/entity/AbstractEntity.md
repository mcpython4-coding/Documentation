***AbstractEntity.py - documentation - last updated on 18.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractEntity extends mcpython.common.event.Registry.IRegistryContent
        
        Dummy class for every entity,
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
            for moder: use this rather than raw constructor as it is the more "safe" way of doing it


        static
        function init_renderers(cls)

        function __init__(self, dimension=None)
            
            creates an new entity for the world
            for moder: you SHOULD implement an custom constructor which set the bellow values to an "good" value


            variable self.dimension

            variable self.entity_height

            variable self.parent - the entity this is riding todo: move into nbt

            variable self.child - the entity this is ridden by  todo: move into nbt

            variable self.nbt_data

        function __del__(self)

        function __str__(self)

        function get_position(self)

        function set_position(self, position: tuple)

        variable position

        function get_motion(self)

        function set_motion(self, motion: tuple)

        function get_dimension(self)

        variable movement

        function set_position_unsafe(self, position: tuple)

        function teleport(self, position, dimension=None, force_chunk_save_update=False)
            
            called when the entity should be teleported
            :param position: the position to teleport to
            :param dimension: to which dimension-id to teleport to, if None, no dimension change is used
            :param force_chunk_save_update: if the system should force to update were player data is stored


        function tell(self, msg: str)
            
            Tells the entity an message. Not intended to inter-mod com
            Should be used by say-commands
            :param msg: the msg to tell


        function kill(
                self,
                drop_items=True,
                kill_animation=True,
                damage_source: mcpython.common.entity.DamageSource.DamageSource = None,
                force=False,
                internal=False,
                ):
            
            Called to kill the entity [remove the entity from world]
            THIS IS THE FINAL REMOVAL METHOD. THIS DOES NOT HAVE MUCH CHECKS IF IT SHOULD BE ABLE TO BE KILLED!
            Is not affected by nbt-tag "invulnerable". Must be handled separately.
            :param drop_items: if items should be dropped
            :param kill_animation: if the kill animation should be played
            :param damage_source: the source of the damage
            :param force: if it should be forced or not
            :param internal: when this is set, this is a normal de-spawn / unload call
            todo: drop items if selected
            todo: play kill animation if selected


        function pick_up_item(
                self, itemstack: mcpython.common.container.ItemStack.ItemStack
                ) -> bool:
            
            Let the entity pick up an item and insert it into its inventory
            :param itemstack: the itemstack to use
            :return: if it was successful or not
            for moder: see world/player.py as an example how this could work
            Subclasses should implement this when they have an inventory for it


        function damage(
                self, damage, reason: mcpython.common.entity.DamageSource.DamageSource = None
                ):
            
            Applies damage to the entity
            FOR MODER:
                this function is an default implementation. for an working example, see the player entity
                - you may want to apply armor calculation code
                - you may want to override this method for an custom implementation
            :param damage: the damage to apply
            :param reason: the reason for the damage, as an DamageSource-instance


        function on_interact(self, player, button, modifiers, itemstack)
            
            Called when the player tries to interact with the entity
            :param player: the player doing so, WARNING: only type-hinted for entity, not world/player.py:Player
            :param button: the button used
            :param modifiers: the modifiers used
            :param itemstack: the itemstack held in hand
            todo: make called
            todo: damage entity when needed
            for moder: should damage entity if needed


        function get_inventories(self) -> list
            
            Will return an list of all currently arrival inventories for this entity


        function on_inventory_cleared(self)
            
            Called by /clear when the inventory of the entity should be cleared


        function draw(self)
            
            Called to draw the entity


        function tick(self, dt: float)
            
            Called every tick to update the entity
            Can be used to update animations, movement, do path finding stuff, damage other entities, ...


        function dump(self)
            
            Dumps the entity into an save-able version
            :return: an pickle-able version, excluding position, rotation and harts, should include inventory serializer
                calls to make sure that everything works
            The nbt data is auto-saved
            Only extra stuff should be saved!


        function load(self, data)
            
            Loads data into the entity, previous saved
            For Moder:
                you CAN include an version entry to make sure you can fix the data version
            :param data: the data to load from
            The nbt data is auto-loaded before this event is called
