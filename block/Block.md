----

**block/Block.py - Documentation - Last updated on 02.03.2020 by uuk**

----

This file contains the base class for every block in the game. Every block MUST inherit from this in order to work.

You are allowed to use other classes beside this class in your code as super classes, but you should be aware of that
this might lead into unwanted behaviour.

If you want an simpler solution for creating new blocks, see factory/BlockFactory.md, this adds an class-generator for blocks.

    class Block extends event.Registry.IRegistryContent
    
        static attribute CUSTOM_WALING_SPEED_MULTIPLIER: float - describes an factor which is used when standing on the block.
            When None, it is not used
            
        overriding static attribute TYPE: str - used internally to identify it as an Block-subclass
        
        static attribute BLOCK_ITEM_GENERATOR_STATE: dict - used by BlockItemFactory to generate the block-item, defines the
            model state the block is shown in as an item. Uses Block.set_model_state(BLOCK_ITEM_GENERATOR_STATE) when
            creating the block-item
            
        attribute position: tuple - the position the block is at
        
        attribute set_to: tuple - the block the block was set to
        
        attribute real_hit: tuple - the hit position as float tuple
        
        attribute face_state: block.BlockFaceState.BlockFaceState - the object representing the face data of the block
        
        attribute block_state: int - internal identifier storing which model id to use
        
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
            
        function is_breakable -> bool
            Used to determine if the block can be broken by player
            WARNING: may be merged with get_hardness in the future
            
        function on_random_update
            Called when the block recieves an random update
        
        function on_block_update
            Called when the block recives an block-update by e.g. adding/removing an near-by block
            
        function is_solid_side face: util.enums.EnumSide -> bool
            Should return if the given face is solid or not
            WARNING: may be moved to an attribute in the future
            
        function get_model_state -> dict
            Used to get the state of the block in terms of rendering
            Used to select in BlockState to find the correct state to render
            
        function set_model_state state: dict
            Used to set an model-state from data
            Used in debug world for block rendering
            
        static function get_all_model_states -> dict
            Used in debug world for finding all possible states of an block
        
        function on_player_interact itemstack: gui.ItemStack.ItemStack button: int modifiers: int exact_hit: tuple -> bool
            Called when the player presses the button [an entry in pyglet.window.mouse] when over the block during 
            holding modifiers [an entry in pyglet.window.key.MOD_[...]] during having itemstack in hand. 
            The position the block was hit is handed over in exact_hit
            The function MUST return if the default logic should stop on or not (e.g. brake the block)
            
            WARNING: this is called when the item of the itemstack does not trigger an event
            WARNING: when you change some things in the world and return False, bad things might happen
            
            WARNING: in the future, maybe an IPlayerLikeEntity object might be added as an parameter to use as the sender
            
        function get_hardness -> int/float
            Used to get the hardness of the block
            WARNING: may be changed to attribute in the future
            
        function get_minimum_tool_level -> int/float
            Used to compare with the tool level of the tool braking the block. See the tools for the values
            
            WARNING: may be chaned to attribute in the future
            WARNING: return type may change in the future
        
        function get_best_tools -> list<util.enums.ToolType>
            Used to compare with the tool type braking the block
            
            WARNING: may change to attribute in th future
            
        function get_provided_slots side: util.enums.EnumSide
            Should return the slots for the given side
            
        function get_view_bbox -> block.BoundingBox.BoundingBox / block.BoundingBox.BoundingArea
            Used to get the bounding box of the block
            WARNING: is called every draw of the world when viewed at. Store the BoundingBox somewhere
            
        function get_custom_block_renderer -> object
            Used to get an custom block renderer
            Unused at the moment
            WARNING: may be removed or moved to an attribute in the future
         
        function on_request_item_for_block itemstack: gui.ItemStack.ItemStack
            Used to modify an itemstack for the block
            Used in picking the block with middle-click
            
        static function modify_block_item item: factory.ItemFactory.ItemFactory
            Used to modify data of the item factory when needed when creating the block-item
