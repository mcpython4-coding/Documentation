----

**block/Block.py - Documentation - Last updated on 16.04.2020 by uuk**

----

This file contains the base class for every block in the game. Every block MUST inherit from this in order to work.

You are allowed to use other classes beside this class in your code as super classes, but you should be aware of that
this might lead into unwanted behaviour.

If you want an simpler solution for creating new blocks, see factory/BlockFactory.md, this adds an class-generator for blocks.

    class Block extends event.Registry.IRegistryContent
    
        overriding static attribute TYPE: str - The registry to register to
        
        static attribute CUSTOM_WALING_SPEED_MULTIPLIER: float - How fast to walk on the block
        
        static attribute BLOCK_ITEM_GENERATOR_STATE: dict - The state to use in the BlockItemGenerator
        
        static attribute BREAKABLE: bool - If the block can be broken in gamemode 0
        
        static attribute HARDNESS: int - How "hard" the block is, used to deterim block break time
        
        static attribute MINIMUM_TOOL_LEVEL: int - An integer representing the tool level to break the block
        
        static attribute BEST_TOOLS_TO_BREAK: list<util.enums.ToolType> - An list of the tool(s) assigned
            to break the block
            
        static attribute EXPLOSION_RESISTANCE: float - An float representing the blast resistance
        
        static attribute RANDOM_TICK_USING: bool - If random ticks are used
        
        static attribute CONDUCTS_REDSTONE: bool - If the block can hold redstone power
        
        static attribute CAN_BE_PUSHED_BY_PISTON: bool - If the block can be pushed by an piston
        
        static attribute CAN_BE_PULLED_BY_PISTON: bool - Id the block can be pulled by an piston
        
        static attribute COLLISION_BOX - An bounding-box similar instance for usage in collision
        
        static attribute FULL_BLOCK: bool - If the block is full or not
        
        static attribute CAN_PLAYER_SPAWN_IN: bool - If the player can spawn in the block
        
        attribute position: tuple - where the block is in the world
        
        attribute set_to: tuple - the block to which the block was set to
        
        attribute real_hit: tuple: where set_to was hit by the ray from player
    
        attribute face_state: block.BlockFaceState.BlockFaceState - an instance representing the status of the faces of
            the block
        
        attribute block_state: int - internally used to determin which model state to select 
        
        attribute face_solid: dict<util.enums.EnumSide -> bool> - represents which faces are solid
        
        attribute injected_redstone_values: list<int[0-15]> - An list representing injected redstone values
            can be used for other blocks to store their injected value
            WARNING: may be changed to dict<util.enums.EnumSide -> int[0-15]>
        
        attribute uuid: uuid.UUID - an unique identifier for these block for this game-instance
        
        static function modify_block_item itemconstructor: factory.ItemFactory.ItemFactory
            called by BlockItemGenerator or its loaders from the dumped files to modify
            an constructed BlockItem.       
        
        function __init__ position: tuple [set_to: tuple] [real_hit: tuple] [state: dict]
            creates an new Block-object from this class. "position" must be an valid position in the world
            defining where the block is located. set_to is optional and defines the coordinates of the block the block 
            was set to. real_hit defines the exact position the other block was hit at. state defines in which model 
            state the block should be created in. When you sub-class Block and would like to do stuff on creation, you
            MUST call the the method of Block to make sure that everything is set up correctly.
            
        function on_remove
            called when the block is removed. Called BEFORE removed from world. Can be used to drop items out of
            inventories or do other (funny) stuff. Please notice: Block drops may NOT be calculated yet.
            
        function get_inventories -> list
            Used to get the inventories from an block. Used by /replaceitem-command and /iteminfo command,
            WARNING: will be removed in future. Use get_provided_slots
            
        function get_redstone_value side: util.enums.EnumSide -> int
        
        function get_provided_slots side: util.enums.EnumSide -> tuple<list<gui.Slot.Slot>,list<gui.Slot.Slot>>
            Should return the slots for the given side. First entry: in, second: out
            
        function get_model_state -> dict
            Used to get the state of the block in terms of rendering
            Used to select in BlockState to find the correct state to render
                    
        function set_model_state state: dict
            Used to set an model-state from data
            Used in debug world for block rendering
            
        static function get_all_model_states -> dict
            Used in debug world for finding all possible states of an block

        function get_view_bbox -> block.BoundingBox.BoundingBox / block.BoundingBox.BoundingArea
            Used to get the bounding box of the block
            WARNING: is called every draw of the world when viewed at. Store the BoundingBox somewhere

        function on_random_update
            Called when the block recieves an random update
        
        function on_block_update
            Called when the block recives an block-update by e.g. adding/removing an near-by block
            
        function on_player_interact itemstack: gui.ItemStack.ItemStack button: int modifiers: int exact_hit: tuple -> bool
            Called when the player presses the button [an entry in pyglet.window.mouse] when over the block during 
            holding modifiers [an entry in pyglet.window.key.MOD_[...]] during having itemstack in hand. 
            The position the block was hit is handed over in exact_hit
            The function MUST return if the default logic should stop on or not (e.g. brake the block)
            
            WARNING: this is called when the item of the itemstack does not trigger an event
            WARNING: when you change some things in the world and return False, bad things might happen
            
            WARNING: in the future, maybe an IPlayerLikeEntity object might be added as an parameter to use as the sender
            
        function on_request_item_for_block itemstack: gui.ItemStack.ItemStack
            Used to modify an itemstack for the block
            Used in picking the block with middle-click
            
        function can_be_replaced_by_block blockname_or_instance: str or block.Block.Block ä
                itemstack: gui.ItemStack.ItemStack position: tuple -> bool
            could be called in the future when placing block to check if an block can be
            replaced by another one
         
        function save -> object<pickleable,compareable>
            used to dump data from the block for save
            WARNING: model state should be included in this data
            
        function load data: object<pickleable,compareable>
            used to load previous dumped data into the block
            same as the previous dumped
            WARNING: stored in saves, please include checks for past versions
            
        function __str__ -> str
            an str-representative of the default attributes of the block
