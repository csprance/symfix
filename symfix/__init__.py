#!/usr/bin/env python
################################################################################
#
# SymFix.py
# Description: The class used for fixing instance mirror bug in modo
# Usage: run main() this script is called from lxserv/SymFixCmd.py
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command
import modo

class SymFix(object):
    def __init__(self):
        self.selection = list()
        self.scene = modo.Scene()
        self.user_selection = list()
        self.instance = None
        self.delete_list = list()

    def store_selection(self):
        '''
        Takes the user selection and stores all the selected
        meshes into a list for later use in self.selection
        '''
        # store the user_selection so we can restore it later
        self.user_selection = self.scene.selected
        # grab all the instances in the selection and duplicates them returning the duplicates
        # self.selection = [self.scene.duplicateItem(inst) for inst in self.scene.selectedByType('meshInst')]
        self.selection = self.scene.selectedByType('meshInst')


    def start(self):
        '''Starts the whole thing off'''
        # store the selection
        self.store_selection()
        # loop through all the selected meshes
        for instance in self.selection:

            name = instance.name
            ids = instance.id
            parent = instance.parent
            index = instance.parentIndex


            # rename it
            instance.name = 'old_mesh_to_delete'

            # select the object
            self.scene.select(instance.id)

            # convert it to a mesh
            lx.eval("item.setType Mesh")

            # add the item to the delete list but wait to do the deleting last
            self.delete_list.append(self.scene.selected[0])


            # copy all polygons
            lx.eval("select.typeFrom polygon;edge;vertex;item;pivot;center;ptag true")
            lx.eval("select.all")
            lx.eval("copy")


            # create a new mesh item
            new_mesh = self.scene.addItem('mesh')

            # rename the new mesh item
            new_mesh.name = name

            # move that mesh item to the correct position
            new_mesh.setParent(newParent=parent, index=index)



            # select the new mesh and paste the new polygons
            self.scene.select(new_mesh)
            lx.eval("paste")


            # flip the polygons
            lx.eval("select.all")
            lx.eval("poly.flip")

            # update surface normals
            lx.eval("edgesmooth.update")

            # deselect everything
            self.scene.deselect(None)

        # # delete the old mesh items as a final step
        for itm in self.delete_list:
            self.scene.select(itm, add=True)
            lx.eval("item.delete")


def main():
    # call it
    sf = SymFix()
    sf.start()


if __name__ == '__main__':
    main()

