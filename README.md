# Symmetry Fix
A modo kit by @csprance to fix the issues that arise from using the mirror instance tool in modo. When you convert to a mesh from an instance by default in modo the faces will all be flipped. The only way I know how to fix that issues (or to even get it to show up in modo for that matter) is to copy and paste the polygons in a new mesh item and flip the faces and update the surface normals on the mesh. This is a pain in the ass if you have a lot of meshes so I just decided to turn it into a modo command and call it done.

## Installation
This is a modo kit so install it like normal. I've only tested this on Modo 10, but I don't think it's doing anything
fancy. Let me know if you run into any issues and if it works on other versions of modo!
* Extract/Clone into `%appdata%/Luxology/Kits`
* Restart modo

## How to use
* `Click` the Sym Fix button with a group or individual instances selected to convert them to meshes and fix issues.

## Video Guide
Coming Soon......


## Whats going on
* using a single instance or instances for each instance:
    * convert it to a mesh
    * copy all polygons
    * create a new mesh item
    * paste the new polygons
    * delete the old mesh item
    * rename the new mesh item 
    * flip the polygons
    * update surface normals

it will do that for each instance selected and then provide an undo context to go back to the beggining if something went wrong.


## Uninstallation process
* Delete `csprance_symmetry_fix` from `%appdata%/Luxology/Kits`

## Credits
* Chris Sprance - All the Things

