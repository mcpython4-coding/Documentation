***AbstractEntity.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractEntity extends  mcpython.common.event.api.IRegistryContent,  ICapabilityContainer,  IBufferSerializeAble,  ABC,  
        
        Base class for every entity in the game
        MUST be implemented by all entities scheduled to be used with the EntityManager system
        Allows capability injects & lookups via the capability API
        DO NOT CHANGE STUFF AT THE FILE HEAD BY SUBCLASSES. IT WILL BREAK THE UNDERLYING STUFF
        Capabilities are auto-saved and this behaviour cannot be disabled currently.


        variable CAPABILITY_CONTAINER_NAME

        variable TYPE

        variable VERSION

        variable SUMMON_ABLE
            If the entity can be used in /summon-command

        static
        function create_new_entity(cls, position, *args, dimension=None, **kwargs)
            
            Creates a new entity and set up it correctly for later use
            :param position: the position to create at
            :param args: args to send to the constructor
            :param dimension: the dimension to spawn in
            :param kwargs: kwargs to send to the constructor
            :return: the created entity
            for moder: use this rather than raw constructor as it is the more "safe" way of doing it
            Does not spawn the entity in the real dimension


            variable entity

            variable entity.position

            variable instance

        static
        function init_renderers(cls)
            
            Use this to create your entity renderers
            Invoked only on client


        function __init__(self, dimension=None)
            
            Creates a new entity for the world
            for moder: you SHOULD implement a custom constructor which set the bellow values to "good" values
            For creating entities, use create_new_entity() - it is far more saver and does some internal stuff


            variable self.dimension

            variable self.unsafe_position - todo: move to nbt

            variable self.rotation - todo: move to nbt

            variable self.hearts - todo: move to nbt

            variable self.chunk

            variable self.uuid

            variable self.entity_height

            variable self.parent - the entity this is riding todo: move into nbt

            variable self.child - the entity this is ridden by  todo: move into nbt

            variable self.nbt_data
                dict holding entity data, automatically saved & loaded, when loading, data is put ontop of the existing dict

            variable self.dead

        function get_collision_box(self)

            variable version

                    variable fixer

                    variable write

                    variable buffer.stream

                    variable version

            variable dim_name

            variable self.dimension

            variable self.rotation

            variable self.uuid

                variable parent_uuid

                variable child_uuid

            variable self.nbt_data["motion"]

            variable self.nbt_data["invulnerable"]

        function add_to_chunk(self)

        function remove_from_chunk(self)

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
            
            Called when the entity should be teleported
            :param position: the position to teleport to
            :param dimension: to which dimension-id to teleport to, if None, no dimension change is used
            :param force_chunk_save_update: if the system should force updating were player data is stored


                variable before_dim

                variable before_dim

                variable dimension_id

                variable dimension_id

            variable sector_after

                variable self.unsafe_position

                variable self.unsafe_position

        function tell(self, msg: str)
            
            Tells the entity an message. Not intended to inter-mod com
            Should be used by say-commands
            :param msg: the msg to tell


            variable damage_source: mcpython.common.entity.DamageSource.DamageSource
            
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


            variable self.dead
            
            Let the entity pick up a item and insert it into its inventory
            :param itemstack: the itemstack to use
            :return: if it was successful or not
            for moder: see world/player.py as an example how this could work
            Subclasses should implement this when they have an inventory for it


        function damage(
                self, damage, reason: mcpython.common.entity.DamageSource.DamageSource = None
                ):
            
            Applies damage to the entity
            FOR MODER:
                This function is a default implementation. For a working example, see the player entity
                - you may want to apply armor calculation code
                - you may want to override this method for a custom implementation
            :param damage: the damage to apply
            :param reason: the reason for the damage, as a DamageSource-instance, or None


        function on_interact(self, player, button: int, modifiers: int, itemstack) -> bool
            
            Called when the player tries to interact with the entity by clicking on it
            Damage should not be calculated here
            :param player: the player doing so, WARNING: only type-hinted for entity, not world/player.py:Player
            :param button: the button used
            :param modifiers: the modifiers used
            :param itemstack: the itemstack held in hand
            :return: if the normal behaviour should be canceled or not
            todo: make called


        function get_inventories(self) -> typing.Iterable
            
            Will return an list of all currently arrival inventories for this entity


        function on_inventory_cleared(self)
            
            Called when the entity inventory should be cleared
            Defaults to clearing all inventories from get_inventories()


        function draw(self)
            
            Called to draw the entity in the world
            Invoked in the correct rendering phase

            
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
                you CAN include a version entry to make sure you can fix the data version
            :param data: the data to load from
            The nbt data is auto-loaded before this event is called
            WARNING: data may be None when dump() was at some point not implemented
