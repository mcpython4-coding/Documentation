You may notice that these is no file in the program itself?
Yes, you are right, but I would like to write some words about
what these system does.

Firstly, it was developed for reduced loading time.
It creates simply some form of cache for various things in the gameä
normally generated during loading. The parts created are various and are
described were they are generated.

You can say to the program to redo the caches with the "--rebuild" flag.
This will also be triggered when an mod(version) was changed.

files in which the prebuild system is located:

- globals.py as flag holder
- setup.py as main class holder
- item/ItemHandler.py for item atlases
- state/StateBlockItemGenerator.py for storing the item files
- texture/factory.py for storing the results