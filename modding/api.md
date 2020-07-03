# Mod API's

Modding can be made easier by providing an (more) stable mod API for other mods
to depend on. API's should be code which is for interaction between mods. The implementation
itself with the needed functional parts should be implemented not in the final API (for performance reasons).

If your mod provides such an API, make sure that it does depend on as less other mods as possible.
API's should be either stored in an api.py file or in an api directory.

If your mod needs another mod's API, you should include the API into your own mod.
As these API is part of the other mod, an licence header MUST be added stating a) the mod
b) the author and c) the version of the API (and d) the licence licensed under).

Feel free to include such header as an API provider to make life of others easier.