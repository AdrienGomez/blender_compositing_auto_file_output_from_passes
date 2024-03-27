import bpy

filename=bpy.path.display_name_from_filepath(bpy.data.filepath)

#Activate Use Nodes for compositing
if bpy.context.scene.use_nodes == False:
    bpy.context.scene.use_nodes = True

#Define context
compositor = bpy.context.scene.node_tree
#Add Output Node
outputnode = compositor.nodes.new(type="CompositorNodeOutputFile")
#Delete all inputs
outputnode.inputs.clear()
#Set file format to exr multilayer and set parameters
outputnode.format.file_format = 'OPEN_EXR_MULTILAYER'
outputnode.format.color_depth = '32'
outputnode.format.exr_codec = 'DWAA'
#Set Output
outputnode.base_path="//renders/compositing/"+filename+"_comp_"

#Define Render Layers Node
rendernode=compositor.nodes['Render Layers']

#function to connect outputs and inputs sockets
def socketlink(socket):
    compositor.links.new(rendernode.outputs[socket],outputnode.inputs[socket])

#Define view layer
currentlayer= bpy.context.view_layer

#Loop through Render Layers node add an input node in File Output with the same name 
for out in rendernode.outputs:
    if not out.is_unavailable:
        outputnode.file_slots.new(out.name)
        socketlink(out.name)
    
 
    
