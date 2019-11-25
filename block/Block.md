***block/Block.py - documentation***
___

This file is used for the base system for blocks.
It contains the base class for every block in game.

How are blocks internal handled?

For every block in the game an instance of the corresponding
Block-class is created storing the information about the block.

This object may be reused under certain circumstance for another block
in the world, when for example been moved or been copied to an location
from another. The block object can see it as an direct placed block in
the world and does not need to handle things for object references from
more than one position

1. class Block(object):
    
    Abstract base class for every block in the game.
    
    Every block which would like to use G.registry for registration
    needs to inherit from this class.
    
    There ARE some default-implementations for certain functions,
    feel free to overwrite all of them.
    
    attributes
    
    - position: the position add. May change on move, will get an
    block update when this happens
    - set_to: the position the block was set to, WARNING: may be None
    - real_hit: where the set_to block was hit at, WARNING: may be None
    
    1. def \_\_init__(self, position: tuple, set_to: tuple=None, state: dict=None, real_hit:tuple<3float>=None)
        Creates an new block instance. needs no overwrite.
        parameters:
        - position: the position created at
        - set_to: when set by player, this will be the block which
        was one block further the view-line
        - state: an dict representing the state the block should be in
        - real_hit: the float position the block setted_to was hit at
        
    2. def get_name() -> str
        
        returns the name of the block, must be implemented
        
    3. def on_register(registry)
        
        called by the block handling system when notated to G.registry.
        May be useful when creating an base class which has to perform
        some actions when registered
        
    4. def on_remove(self)
    
        called when the block is removed out of the world
        
    5. def get_inventories(self):
    
        should return an list of block inventories provided by this
        block. Default is an empty list
        
    6. def is_breakable(self) -> bool
    
        returns if the block can be broken in gamemode 0 or 2
        
    7. def on_random_update(self):
    
        default disabled function called when the block gets an random
        update
     
    8. def on_block_update(self)
    
        called when an block next to this gets updated
        
    9. def is_solid_side(self, side: util.enums.EnumSide) -> bool
    
        returns if the side is solid or not. This is used for 
        calculation of which block should be shown
    
    10. def get_model_state(self)
    
        returns the dict representing an valid entry in the blockstate
        file for this block
        
    11. def set_model_state(self, state: dict)
    
        set the model state of the block from the data
        
    12. def get_all_model_states()
    
        returns an list of block states these block supports. used by
        the debug world generator
        
    13. def on_player_interact(self, itemstack: gui.ItemStack.ItemStack, button: int, modifiers: int, exact_hit: tuple<3float>) -> bool
        
        called when the block is interacted by the player with itemstack
        in hand with button & modifiers at mouse and at hit exact_hit.
        returns if "normal" behaviour should go on or interrupted.
    
    14. def get_hardness(self) -> float
    
        returns the hardness of the block. Used to calculate brake time
        
    15. def get_minimum_tool_level(self) -> int
    
        every tool has an level. Here the minimum is defined. 
        
    16. def get_best_tools(self)
    
        returns an list of item.ItemTool.ToolType representing good 
        tools to brake this block. Used for brake time calculation
    
    17. def get_provided_slots(self, side: util.enums.EnumSide)
    
        returns an list of slots for the given side. Used for item 
        transfer (in the future).
        
        WARNING: The slots may not be only item holding. Please check 
        against gui.Slot.Slot before using.
    
    18. def get_view_bbox(self) -> block.BoundingBox.BoundingBox
    
        returns an bounding box used for these block
        
    19. def get_custom_block_renderer(self) -> block.ICustomBlockRenderer.ICustomBlockRenderer
    
        returns if needed an 
        block.ICustomBlockRenderer.ICustomBlockRenderer
        
    20. def on_request_item_for_block(self, itemstack: gui.ItemStack.ItemStack)
    
        called when an item specific for THESE block is needed. This 
        means for example for chests: with inventory data in item.
    
    21. def modify_block_item(cls, itemconstructor)
    
        called by the BlockItemFactory. Makes it possible to change the
        properties of the item for the block. Can fully replace it.
         
         
        