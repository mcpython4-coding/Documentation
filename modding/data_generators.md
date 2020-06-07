# File about data generation

When to use
-

Data generators make it possible to generate stuff in python code and export it
for later usage into files. The files must be allocated into your normal mod system.

Generation happens only in dev-environments as data generators of mcpython-4
point towards dev-only folders.

For mod dev's you should manually override this flag in code and NOT run with --data-gen!

How to use
-

Data generators are powerful. You have to subscribe to the event "special:datagen:configure".
In this loading stage, you should create at least one mcpython.datagen.Configuration.DataGeneratorConfig
to configure where to output stuff. Than you can go ahead and create data-generator instances which will be
generated automatically after the stage is finished. 