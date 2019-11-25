***block/ISlab.py - documentation***
___

This file is used as base class for slab-like blocks.
It contains the code for creating an slab block & working with it.
It contains also an enum representing the three states of an slab:
upper, downer & double


1. class SlabModes(enum.Enum)
    
    as mentioned above, these contains the three states of an slab:
    - top
    - bottom
    - double

2. variable dict<block.ISlab.SlabModes -> block.BoundingBox.BoundingBox>
BBOX_DICT: an map representing the bounding boxes of an slab in every 
state

3. class ISlab(block.Block.Block)

    base class for every slab, overwrites the block.Block.Block 
    functions to to its job
    
    1. def on_create(self)
    
        overwrites super method. Will setup slab data like state.
        
    2. def get_model_state(self)
    
        overwrites super method, returns the state of the slab, an name 
        of the block.ISlab.SlabModes-enum, as dict {"type": <name>}
        
    3. def set_model_state(self, state: dict)
    
        overwrites super method. when "type"-key is in state data, it 
        will be decoded to the state of the slab.
        
    4. def get_all_model_states() -> list
    
        overwrites super method. returns an list of all slab state data's
        
    5. def on_player_interact(self, itemstack, button, modifiers, exact_hit) -> bool
    
        overwrites super method. empty function body, planed 
        implementation place for the single -> double transform of an 
        slab
        
    6. def is_solid_side(self, side) -> bool
    
        overwrites super method. returns if the side is solid.
        Returns only True if state is double
        
    7. def get_view_bbox(self)
    
        returns the bounding box of the block read from (2)