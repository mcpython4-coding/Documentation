***Inventory.py - documentation - last updated on 14.5.2020 by uuk***
___

    improvements for the future:
    - add option to store under an special directory the data and output the binary data
    


    @G.registry class Inventory extends storage.serializer.IDataSerializer.IDataSerializer

        variable PART

        static function load(cls, savefile, inventory: gui.Inventory.Inventory, path: str, file=None)
        static function save(cls, data, savefile, inventory: gui.Inventory.Inventory, path: str, file=None, override=False)