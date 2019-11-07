bl_info = {
    "name": "FS Tools Public Demo",
    "description": "FSTools is a collection of pie menus to accomodate a fast and efficient workflow in fullscreen",
    "author": "Mark C",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "ALT + Q",
    "warning": "Public demo. Bugs might still exist, please use the appropriate thread for reporting bugs.",
    "wiki_url": "http://example.com",
    "category": "User Interface" }

import bpy
import os
import subprocess
from bpy.types import Menu

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)

class PIE_MT_init(Menu):
    # label is displayed at the center of the pie menu.
    bl_idname = "PIE_MT_init"
    bl_label = "FS Tools"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("wm.call_menu_pie", text="Snap Tools", icon='SNAP_ON').name = "PIE_MT_snap"
        pie.operator("wm.call_menu_pie", text="Shading Tools", icon='MATSHADERBALL').name = "PIE_MT_shading"
        pie.operator("wm.call_menu_pie", text="FS Ops", icon='SCRIPT').name = "PIE_MT_fsops"
        pie.operator("wm.call_menu", text="Editor Tools", icon='PRESET').name = "LAYOUT_MT_editor"
        pie.operator("wm.call_menu_pie", text="Render Tools", icon='BLENDER').name = "PIE_MT_render"
        pie.operator("wm.call_menu_pie", text="View Tools", icon='RESTRICT_VIEW_OFF').name = "PIE_MT_view"

#################################################################################################

class PIE_MT_render(Menu):
    # label is displayed at the center of the pie menu.
    bl_idname = "PIE_MT_render"
    bl_label = "Render Engine"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("render.engine_eevee")
        pie.operator("render.engine_cycles")
        pie.operator("render.engine_workbench")

class EeveeRenOp(bpy.types.Operator):
    bl_idname = "render.engine_eevee"
    bl_label = "Eevee"
    def execute(self, context):
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'

        return {'FINISHED'}

class CyclesRenOp(bpy.types.Operator):
    bl_idname = "render.engine_cycles"
    bl_label = "Cycles Renderer"
    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'

        return {'FINISHED'}

class WorkBenchRenOp(bpy.types.Operator):
    bl_idname = "render.engine_workbench"
    bl_label = "Workbench"
    def execute(self, context):
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'

        return {'FINISHED'}

###################################################################################################
#Editor

class LAYOUT_MT_editor(bpy.types.Menu):
    bl_label = "Editor Menu"
    bl_idname = "LAYOUT_MT_editor"

    def draw(self, context):
        layout = self.layout


        layout.operator("view.editor", icon='VIEW3D')
        layout.operator("uvw.editor", icon='GROUP_UVS')
        layout.operator("shader.editor", icon='SHADING_RENDERED')
        layout.row().separator()
        layout.operator("sequence.editor", icon='SEQ_SEQUENCER')
        layout.operator("clip.editor", icon='RENDER_ANIMATION')
        layout.operator("dope.editor", icon='ACTION')
        layout.operator("graph.editor", icon='GRAPH')
        layout.operator("nla.editor", icon='NLA')
        layout.row().separator()
        layout.operator("text.editor", icon='FILE_TEXT')
        layout.operator("console.editor", icon='CONSOLE')


class ShaderSwitch(bpy.types.Operator):
    bl_idname = "shader.editor"
    bl_label = "Shader Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NODE_EDITOR')

        return {'FINISHED'}

class ViewSwitch(bpy.types.Operator):
    bl_idname = "view.editor"
    bl_label = "3D Viewport"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='VIEW_3D')

        return {'FINISHED'}

class UVSwitch(bpy.types.Operator):
    bl_idname = "uvw.editor"
    bl_label = "UV Image Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='IMAGE_EDITOR')

        return {'FINISHED'}

class SequenceSwitch(bpy.types.Operator):
    bl_idname = "sequence.editor"
    bl_label = "Sequence Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='SEQUENCE_EDITOR')

        return {'FINISHED'}

class ClipSwitch(bpy.types.Operator):
    bl_idname = "clip.editor"
    bl_label = "Clip Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='CLIP_EDITOR')

        return {'FINISHED'}

class DopeSwitch(bpy.types.Operator):
    bl_idname = "dope.editor"
    bl_label = "Dopesheet Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='DOPESHEET_EDITOR')

        return {'FINISHED'}

class GraphSwitch(bpy.types.Operator):
    bl_idname = "graph.editor"
    bl_label = "Graph Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='GRAPH_EDITOR')

        return {'FINISHED'}

class NLASwitch(bpy.types.Operator):
    bl_idname = "nla.editor"
    bl_label = "NLA Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NLA_EDITOR')

        return {'FINISHED'}

class TextSwitch(bpy.types.Operator):
    bl_idname = "text.editor"
    bl_label = "Text Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='TEXT_EDITOR')

        return {'FINISHED'}

class ConsoleSwitch(bpy.types.Operator):
    bl_idname = "console.editor"
    bl_label = "Console Editor"
    def execute(self, context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='CONSOLE')

        return {'FINISHED'}


#################################################################################################
#fsops

class PIE_MT_fsops(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "FS Ops"
    bl_idname = "PIE_MT_fsops"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("wm.call_menu", text="Community Menu", icon='PRESET').name = "LAYOUT_MT_community"
        pie.operator("quick.cycles", text="Quick Cycles", icon='FF')
        pie.operator("add.dof", text="Add Empty as DOF", icon='EMPTY_AXIS')


#################################################################################################
#fsops_custom operators
#################################################################################################
class DOFAdd(bpy.types.Operator):
    bl_idname = "add.dof"
    bl_label = "Add an empty named as DOF"
    def execute(self, context):
        bpy.ops.object.empty_add(type='SPHERE', location=(0, 0, 0))
        bpy.context.object.name = "DOF"

        return {'FINISHED'}

#################################################################################################
#quickcycles

class QuickCycles(bpy.types.Operator):
    bl_idname = "quick.cycles"
    bl_label = "Speed up cycles rendering by lowering light path bounces"
    def execute(self, context):
        bpy.context.scene.cycles.diffuse_bounces = 1
        bpy.context.scene.cycles.glossy_bounces = 1
        bpy.context.scene.cycles.transparent_max_bounces = 1
        bpy.context.scene.cycles.transmission_bounces = 1
        bpy.context.scene.cycles.volume_bounces = 1
        bpy.context.scene.cycles.max_bounces = 1
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        return {'FINISHED'}

#################################################################################################
#communitymenu

class LAYOUT_MT_community(bpy.types.Menu):
    bl_label = "Community Menu"
    bl_idname = "LAYOUT_MT_community"

    def draw(self, context):
        layout = self.layout
        layout.operator('wm.url_open', text='Blender Homepage', icon='BLENDER').url='http://www.blender.org'
        layout.operator('wm.url_open', text='Blender Facebook').url='https://www.facebook.com/groups/2207257375/'
        layout.operator('wm.url_open', text='Blendernation').url='https://www.blendernation.com/'
        layout.operator('wm.url_open', text='Blender Artists').url='https://blenderartists.org//'
        layout.operator('wm.url_open', text='Blender Reddit').url='https://www.reddit.com/r/blender/'
        layout.operator('wm.url_open', text='Blender Today').url='https://blender.community/c/today'
        layout.operator('wm.url_open', text='Blender Stackexchange').url='https://blender.stackexchange.com/'
        layout.operator('wm.url_open', text='Blendswap').url='https://www.blendswap.com/'
        layout.operator('wm.url_open', text='Right Click Select').url='https://blender.community/c/rightclickselect/'
        layout.row().separator()
        layout.operator('wm.url_open', text='Artstation').url='https://www.artstation.com/'
        layout.operator('wm.url_open', text='Pinterest').url='https://www.pinterest.com/'

#################################################################################################
#viewtools

class PIE_MT_view(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "View Tools"
    bl_idname = "PIE_MT_view"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("wm.window_fullscreen_toggle", text="Toggle Fullscreen", icon='FULLSCREEN_ENTER')
        pie.operator("wm.context_toggle",text="Show Floor", icon='GRID').data_path = "space_data.overlay.show_floor"
        pie.operator("wm.context_toggle",text="Toggle Overlays", icon='OVERLAY').data_path = "space_data.overlay.show_overlays"
        pie.operator("wm.context_toggle",text="Show Gizmo", icon='OBJECT_ORIGIN').data_path = "space_data.show_gizmo"


#################################################################################################
#Shading

class PIE_MT_shading(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Shading Tools"
    bl_idname = "PIE_MT_shading"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        pie.operator("object.better_smooth", text="Smooth", icon='SHADING_SOLID')
        pie.operator("object.shade_flat", text="Flat", icon='SHADING_RENDERED')

class BetterSmooth(bpy.types.Operator):
    bl_idname = "object.better_smooth"
    bl_label = "Smooth shading with autosmooth"
    def execute(self, context):
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}

#################################################################################################
#Snapping


class PIE_MT_snap(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Snap Tools"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        pie.operator("snap.increment", text="Increment Snap", icon='SNAP_INCREMENT')
        pie.operator("snap.edge", text="Edge Snap", icon='SNAP_EDGE')
        pie.operator("snap.face", text="Face Snap", icon='SNAP_FACE')
        pie.operator("snap.vertex", text="Vertex Snap", icon='SNAP_VERTEX')

class SnapIncrement(bpy.types.Operator):
    bl_idname = "snap.increment"
    bl_label = "Snap to increment"
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}
        return {'FINISHED'}

class SnapEdge(bpy.types.Operator):
    bl_idname = "snap.edge"
    bl_label = "Snap to Edge"
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'EDGE'}
        return {'FINISHED'}

class SnapFace(bpy.types.Operator):
    bl_idname = "snap.face"
    bl_label = "Snap to Face"
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'FACE'}
        return {'FINISHED'}

class SnapVertex(bpy.types.Operator):
    bl_idname = "snap.vertex"
    bl_label = "Snap to Vertex"
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}
        return {'FINISHED'}


##################################################################################################
#Select

class PIE_MT_select(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Select Tools"
    bl_idname = "PIE_MT_select"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("mesh.select_similar", text="ASelect Similar", icon='COPY_ID')
        pie.operator("mesh.select_random",  text="DSelect Random", icon='MOD_NOISE')
        pie.operator("mesh.select_nth", text="SChecker Deselect", icon='IMAGE_ZDEPTH')
        pie.operator("mesh.select_mode", text="WVertex", icon='VERTEXSEL').type = 'VERT'
        pie.operator("mesh.select_mode", text="QEdge", icon='EDGESEL').type = 'EDGE'
        pie.operator("mesh.select_mode", text="EFace", icon='FACESEL').type = 'FACE'
        pie.operator("wm.call_menu_pie", text="ZSnap Tools", icon='SNAP_ON').name = "PIE_MT_snap"
        pie.operator("mesh.bevel", text="CBevel", icon='MOD_BEVEL')

##################################################################################################
#Registering

classes = (
    PIE_MT_init,
    PIE_MT_render,
    LAYOUT_MT_editor,
    PIE_MT_fsops,
    LAYOUT_MT_community,
    PIE_MT_view,
    PIE_MT_shading,
    PIE_MT_snap,
    PIE_MT_select,
    EeveeRenOp,
    CyclesRenOp,
    WorkBenchRenOp,
    DOFAdd,
    QuickCycles,
    ShaderSwitch,
    ViewSwitch,
    UVSwitch,
    SequenceSwitch,
    ClipSwitch,
    DopeSwitch,
    GraphSwitch,
    NLASwitch,
    TextSwitch,
    ConsoleSwitch,
    BetterSmooth,
    SnapVertex,
    SnapFace,
    SnapEdge,
    SnapIncrement,
    )

addon_keymaps = []


def register():

    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager
    kc = bpy.context.window_manager.keyconfigs.addon
    if wm.keyconfigs.addon:

        km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')

        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS' ,alt=True)
        kmi.properties.name = "PIE_MT_init"

        km = wm.keyconfigs.addon.keymaps.new(name="Mesh")

        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS' ,alt=True)
        kmi.properties.name = "PIE_MT_select"
        addon_keymaps.append((km,kmi))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

#@Mark C  btw you can shorten your method with: register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
	register()
