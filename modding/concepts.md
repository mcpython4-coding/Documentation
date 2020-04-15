

This file documents how to do certain things for modders


Registries

    Most of the content of the game is stored in so-called registries (instances
    of event.Registry.Registry). Every entry in such an registry must inherit from
    event.Registry.IRegistryContent and have the TYPE and NAME attribute set. You may
    want to use another class in between which sets the TYPE attribute and adds
    API-like functions. You can find examples of this e.g. at Block/Block.py
    
    Registry entries CAN be replaced by registering an entry with the same name.
    WARNING: if you run into errors when replacing, feel free to open an issue.
    If you searching for an cross-mod exception, please note that replaced registry
    content may give errors.
    
    How to send objects to the registry?
        The registry handler is stored at globals.registry. It has an function
        register() which gets the object to notate. But you can use also the annotation
        @globals.registry to do so.
        

Assets
    
    Stored with all executeable files in the mod folder/file/similar.
    Loaded dynamically for before-loaded namespaces. When an mod wants
    to register his own assets, <mod-instance>.add_load_default_resources()
    is the way to do so. This will register all default-locations to the system
    for assets. 


Blocks

    The concept of TileEntities does not exists. Please store your data direct in
    the block-instance and dump it manually. Use custom flags when your block
    should not be moveable by e.g. pistons.
    
    For creating an own block, you will need to create an sub-class of block/Block.py 
    or any of its sub-classes (like block/ISlab.py). This class must be registered,
    as every registry-content, with the @globals.registry notation to the system.
    As an item of the registry, the NAME attribute  M U S T  be set. For an list of
    all interfaces, see your super-classes.
    

Items
    
    Items are instances of sub-classes of item.Item.Item registered to the registry.
    They are stored in gui.ItemStack.ItemStack-instances. When they are stored in an
    gui, they are stored in an gui.Slot.Slot or similar class stored in an 
    gui.Inventory.Inventory-instance.
    
Recipes, Tags, Functions and Loot tables

    Stored the same way as in mc in data/{namespace}/{group}/{...}.
    <namespace> must be registered for asset loading
    
Commands
    
    Commands are sub-classes of chat.command.Command.Command. They are parsed
    with constructed chat.command.Command.ParseBridge-instances. For examples,
    see the existing commands in chat.command.Command[...]
    
Entities

    Entities are WIP as they were introduced not long ago. Types must be registered
    to the global registry as everything. Entities can be created with 
    globals.entityhandler.add_entity()
    
Events

    Events are called on so-called EventBuses which handle on the one side event calls
    and on the other side the registered functions. They can be activated/deactivated.
    They are used for e.g. states to handle fast-changes. For an complet list
    of all non-loading-events see events.list
    
Factories

    Helper classes for constructing new classes for registry. Make process simpler,
    but are not able to do much things. Usefull for deco items
    
Gui's

    Instances of gui.Inventory.Inventory, can be toggled on and off, can be always active,
    can contain slots for item handling.
    
Custom Block Renderers

    It is possible to replace the default block renderer with another one by sub-classing
    an rendering.ICustomBlockRenderer. Must be set in Block.face_state.custom_renderer to
    be active.
    
Entity Renderer

    mcpython supports model files for entities. These files  M U S T  be parsed in
    an rendering.EntityRenderer.EntityRenderer-instance (which will also handle the
    reload when needed). This model can also used in custom block renderers.
    
OpenGLSetupFiles

    An system for storing OpenGL-commands to exchange them simple during runtime.
    Used internally to setup OpenGL for rendering, can be used for any OpenGL command.
    
States

    The game is splitted up into so-called States which represent an state of the game.
    This system can be extended by creating own State-subclasses. For extending an 
    existing state, you can use an StatePart-subclass and inject it into the state to
    extend.
    
Save files

    The game can save your world. Some classes support storing extra information
    beside the information saved by default. You can also add own structures or replace
    the old ones by overriding registry side. Please make sure that you can load
    past-versions of your mod-data
    
World

    The world is stored in an world.World.World instance containing 
    world.Dimension.Dimension instances which then contain world.Chunk.Chunk instances.
    Chunks have an dict of blocks.

