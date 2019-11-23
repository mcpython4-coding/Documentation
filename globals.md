***globals.py - documentation***
___

This file is used for storing global stuff like handlers and runtime 
flags.
It contains a wide range of instances of handlers & registries

Additions of new handlers are welcome.
A mod could exchange handlers, but please make sure that all functions
are implemented.

WARNING: everything is very changeable, including the changes done in
the near future found in version.info

1. variable str VERSION: The version of the game

2. variable bool prebuilding: if prebuilding

3. variable bool debugevents: if events should be debugged

4. variable str local: path the globals-file is in, normally should be
base directory

5. variable rendering.Window.Window window: window instance

6. variable world.World.World world: the active world

7. variable world.player.Player player: the active player instance

8. variable chat.Chat.Chat chat: the active chat instance

9. variable event.EventHandler.EventHandler eventhandler: the active
event handler

10. variable event.TickHandler.TickHandler tickhandler: the active
tickhandler

11. variable event.Registry.RegistryHandler registry: the main registry

12. variable chat.command.CommandParser.CommandParser commandparser:
instance of the command parser

13. variable state.StateHandler.StateHandler statehandler: the main
statehandler

14. variable texture.factory.TextureFactoryHandler 
texturefactoryhandler: texturefactory instance

15. variable gui.InventoryHandler.InventoryHandler inventoryhandler: 
main inventory handler instance

16. variable world.gen.WorldGenerationHandler.WorldGenerationHandler 
worldgenerationhandler: main world generation handler

17. variable world.gen.biome.BiomeHandler.BiomeHandler biomehandler:
main biome handler

18. variable crafting.CraftingHandler.CraftingHandler craftinghandler:
main crafting handelr

19. variable tags.TagHandler.TagHandler taghandler: main tag handler

20. variable world.Dimension.DimensionHandler dimensionhandler: main 
dimension handler

21. variable texture.model.ModelHandler.ModelHandler modelhandler: 
main modelhandler instance

22. variable mod.ModLoader.ModLoader modloader: modloader instance

23. variable int NEXT_EVENT_BUS_ID: counter for event bus id's