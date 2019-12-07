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

1. variable bool prebuilding: if prebuilding

2. variable bool debugevents: if events should be debugged

3. variable str local: path the globals-file is in, normally should be
base directory

4. variable rendering.Window.Window window: window instance

5. variable world.World.World world: the active world

6. variable world.player.Player player: the active player instance

7. variable chat.Chat.Chat chat: the active chat instance

8. variable event.EventHandler.EventHandler eventhandler: the active
event handler

9. variable event.TickHandler.TickHandler tickhandler: the active
tickhandler

10. variable event.Registry.RegistryHandler registry: the main registry

11. variable chat.command.CommandParser.CommandParser commandparser:
instance of the command parser

12. variable state.StateHandler.StateHandler statehandler: the main
statehandler

13. variable texture.factory.TextureFactoryHandler 
texturefactoryhandler: texturefactory instance

14. variable gui.InventoryHandler.InventoryHandler inventoryhandler: 
main inventory handler instance

15. variable world.gen.WorldGenerationHandler.WorldGenerationHandler 
worldgenerationhandler: main world generation handler

16. variable world.gen.biome.BiomeHandler.BiomeHandler biomehandler:
main biome handler

17. variable crafting.CraftingHandler.CraftingHandler craftinghandler:
main crafting handelr

18. variable tags.TagHandler.TagHandler taghandler: main tag handler

19. variable world.Dimension.DimensionHandler dimensionhandler: main 
dimension handler

20. variable texture.model.ModelHandler.ModelHandler modelhandler: 
main modelhandler instance

21. variable mod.ModLoader.ModLoader modloader: modloader instance

22. variable int NEXT_EVENT_BUS_ID: counter for event bus id's