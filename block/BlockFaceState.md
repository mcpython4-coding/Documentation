----

**block/BlockFaceState.py - Documentation - Last updated on 16.04.2020 by uuk**

----

This file contains the class for the status of the faces of every block in-game

    class BlockFaceState
        
        attribute block: block.Block.Block - the block based on
        
        attribute faces: dict<util.enums.EnumSide -> bool> - which faces are currently shown
        
        attribute face_data: dict<util.enums.EnumSide -> list<vertices>> - the vertex data for each face
        
        attribute custom_renderer: rendering.ICustomBlockRenderer - an custom renderer describing the block
        
        attribute subscribed_renderer: bool - True when custom_renderer is draw-function and it was added
            to the correct event bus
            
        function __init__ block: block.Block.Block
            will set up the system for an block instance
            
        function show_face face: util.enums.EnumSide
            will show an face. If already shown, northing happens. Will
            handle custom block renderers as needed.
            
        function hide_face face: util.enums.EnumSide
            will hide an face. If not shown, nothing happens. Will handle
            custom block renderers as needed
            
        function _draw_custom_renderer
            internally used to draw an custom block renderer. Used to send the correct interfaces
            to the custom block renderers
            
        function update [redraw_complete: bool = False]
            Updates all faces. When redraw_complete is True, firstly, all faces are hidden.
            
        function hide_all
            will hide all shown faces. Will handle custom block renderers as needed.
            
        function __str__ -> str
            transforms the BlockFaceState into an attribute-based object-str
    
