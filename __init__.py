bl_info = {
    "name": "FS Tools Public Demo",
    "description": "FSTools is a collection of pie menus to accomodate a fast and efficient workflow in fullscreen",
    "author": "Mark C | Antony Riakiotakis, Sebastian Koenig - Motion Tracking Pie",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "location": "ALT + Q",
    "warning": "Public demo. Bugs might still exist, please use the appropriate thread for reporting bugs.",
    "wiki_url": "https://github.com/MarkC-b3d/FSTools/issues",
    "category": "User Interface" }

import bpy
import os
import subprocess
from bpy.types import Menu

class PIE_MT_init(Menu):

    bl_idname = "PIE_MT_init"
    bl_label = "FS Tools"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()

        pie.operator("wm.call_menu_pie", text="Snap Tools", icon='SNAP_ON').name = "PIE_MT_snap"
        pie.operator("wm.call_menu_pie", text="Shading Tools", icon='MATSHADERBALL').name = "PIE_MT_shading"
        pie.operator("wm.call_menu_pie", text="FS Ops", icon='SCRIPT').name = "PIE_MT_fsops"
        pie.operator("wm.call_menu", text="Editor Tools", icon='PRESET').name = "LAYOUT_MT_editor"
        pie.operator("wm.call_menu_pie", text="Render Tools", icon='BLENDER').name = "PIE_MT_render"
        pie.operator("wm.call_menu_pie", text="View Tools", icon='RESTRICT_VIEW_OFF').name = "PIE_MT_view"
        pie.operator("wm.call_menu_pie", text="File Tools", icon='FILEBROWSER').name = "PIE_MT_topbar"

#################################################################################################

class PIE_MT_topbar(Menu):

    bl_idname = "PIE_MT_topbar"
    bl_label = "Topbar Tools"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()

        pie.operator("wm.call_menu", text="File", icon='PRESET').name = "TOPBAR_MT_file"
        pie.operator("wm.call_menu", text="Edit", icon='EDITMODE_HLT').name = "TOPBAR_MT_edit"
        pie.operator("wm.call_menu", text="Render", icon='RESTRICT_RENDER_OFF').name = "TOPBAR_MT_render"
        pie.operator("wm.call_menu", text="Window", icon='WINDOW').name = "TOPBAR_MT_window"
        pie.operator("wm.call_menu", text="Help", icon='HELP').name = "TOPBAR_MT_help"


#################################################################################################

class PIE_MT_track(Menu):

    bl_idname = "PIE_MT_track"
    bl_label = "Tracking Pies"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()

        pie.operator("wm.call_menu_pie", text="Markers", icon='OUTLINER_OB_EMPTY').name = "PIE_MT_tracking_marker"
        pie.operator("wm.call_menu_pie", text="Tracking", icon='DECORATE_LINKED').name = "PIE_MT_tracking_track"
        pie.operator("wm.call_menu_pie", text="Clip Setup", icon='CAMERA_DATA').name = "PIE_MT_clipsetup_pie"
        pie.operator("wm.call_menu_pie", text="Solver", icon='FILE_SCRIPT').name = "PIE_MT_solver_pie"
        pie.operator("wm.call_menu_pie", text="Reconstruction", icon='MOD_BUILD').name = "PIE_MT_reconstruction_pie"

####################################################################################################

class PIE_MT_render(Menu):

    bl_idname = "PIE_MT_render"
    bl_label = "Render Engine"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

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
        #pie.operator("wm.call_menu", text="Pipeline Menu", icon='MESH_CYLINDER').name = "LAYOUT_MT_pipeline"
        pie.operator("quick.cycles", text="Quick Cycles", icon='FF')
        pie.operator("add.dof", text="Add Empty as DOF", icon='EMPTY_AXIS')
        pie.operator('wm.url_open', text='Order food', icon='MESH_TORUS').url='https://www.google.com/search?q=order+food+online'
        pie.operator('wm.url_open', text='FSTools Github', icon='SCRIPTPLUGINS').url='https://github.com/MarkC-b3d/FSTools'


# class LAYOUT_MT_pipeline(bpy.types.Menu):
#     bl_label = "Pipeline Menu"
#     bl_idname = "LAYOUT_MT_pipeline"
#
#     def draw(self, context):
#         layout = self.layout
#
#         layout.operator("substance.painter", icon='BRUSH_DATA')
#         layout.operator("substance.designer", icon='NODETREE')
#         layout.row().separator()
#         layout.operator("autodesk.maya", icon='ORPHAN_DATA')
#         layout.operator("autodesk.3ds", icon='ORPHAN_DATA')
#          layout.row().separator()
#          layout.operator("unreal.engine", icon='FUND')
#          layout.operator("vfx.natron", icon='OUTLINER_OB_CAMERA')
#
#
# class SubstancePainter(bpy.types.Operator):
#     bl_idname = "substance.painter"
#     bl_label = "Substance Painter"
#     def execute(self, context):
#         subprocess.Popen(["E:\\Substance Painter\\Substance Painter"])
#         return {'FINISHED'}
#
# class SubstanceDesigner(bpy.types.Operator):
#     bl_idname = "substance.designer"
#     bl_label = "Substance Designer"
#     def execute(self, context):
#         subprocess.Popen(["E:\\Substance Designer\\Substance Designer"])
#         return {'FINISHED'}
#
# class Autodesk3DS(bpy.types.Operator):
#     bl_idname = "autodesk.3ds"
#     bl_label = "3DS Max"
#     def execute(self, context):
#         subprocess.Popen(["E:\\3DS_Max\\3ds Max 2018\\3dsmax"])
#         return {'FINISHED'}
#
# class AutodeskMaya(bpy.types.Operator):
#     bl_idname = "autodesk.maya"
#     bl_label = "Autodesk Maya"
#     def execute(self, context):
#         subprocess.Popen(["E:\\Maya\\Maya2018\\bin\\maya"])
#         return {'FINISHED'}
#
# class UnrealEngine(bpy.types.Operator):
#     bl_idname = "unreal.engine"
#     bl_label = "Unreal Engine"
#     def execute(self, context):
#         subprocess.Popen(["D:\\Programs\\UnrealEngine\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher"])
#         return {'FINISHED'}
#
# class VFXNatron(bpy.types.Operator):
#     bl_idname = "vfx.natron"
#     bl_label = "Natron"
#     def execute(self, context):
#         subprocess.Popen(["E:\\Natron\\Natron-2.3.14-Windows-x86_64bit-no-installer\\bin\\Natron"])
#         return {'FINISHED'}

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
        '''Speed up cycles rendering by lowering light path bounces'''
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
        pie.operator("mesh.select_similar", text="(A) Select Similar", icon='COPY_ID')
        pie.operator("mesh.select_random",  text="(D) Select Random", icon='MOD_NOISE')
        pie.operator("wm.call_menu", text="(S) Select", icon='RESTRICT_SELECT_OFF').name = "VIEW3D_MT_select_edit_mesh"
        pie.operator("mesh.select_mode", text="(W) Vertex", icon='VERTEXSEL').type = 'VERT'
        pie.operator("mesh.select_mode", text="(Q) Edge", icon='EDGESEL').type = 'EDGE'
        pie.operator("mesh.select_mode", text="(E) Face", icon='FACESEL').type = 'FACE'
        pie.operator("wm.call_menu_pie", text="(Z) Snap Tools", icon='SNAP_ON').name = "PIE_MT_snap"
        pie.operator("wm.call_menu_pie", text="(C) VEF Tools", icon='FILE_SCRIPT').name = "PIE_MT_vef"

class PIE_MT_vef(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Select Tools"
    bl_idname = "PIE_MT_vef"

    def draw(self, context):
        layout = self.layout


        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator("wm.call_menu", text="Verts", icon='VERTEXSEL').name = "VIEW3D_MT_edit_mesh_vertices"
        pie.operator("wm.call_menu", text="Edges", icon='EDGESEL').name = "VIEW3D_MT_edit_mesh_edges"
        pie.operator("wm.call_menu", text="Faces", icon='VERTEXSEL').name = "VIEW3D_MT_edit_mesh_faces"
        pie.operator("wm.call_menu", text="UV", icon='UV').name = "VIEW3D_MT_uv_map"


##################################################################################################
#Clip Pie

class PIE_MT_tracking_marker(Menu):
    # Settings for the individual markers
    bl_label = "Marker Settings"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.mode == 'TRACKING'

    def draw(self, context):
        clip = context.space_data.clip
        tracks = getattr(getattr(clip, "tracking", None), "tracks", None)
        track_active = tracks.active if tracks else None

        layout = self.layout
        pie = layout.menu_pie()
        # Use Location Tracking
        prop = pie.operator("wm.context_set_enum", text="Loc", icon='OUTLINER_DATA_EMPTY')
        prop.data_path = "space_data.clip.tracking.tracks.active.motion_model"
        prop.value = "Loc"
        # Use Affine Tracking
        prop = pie.operator("wm.context_set_enum", text="Affine", icon='OUTLINER_DATA_LATTICE')
        prop.data_path = "space_data.clip.tracking.tracks.active.motion_model"
        prop.value = "Affine"
        # Copy Settings From Active To Selected
        pie.operator("clip.track_settings_to_track", icon='COPYDOWN')
        # Make Settings Default
        pie.operator("clip.track_settings_as_default", icon='SETTINGS')
        if track_active:
        # Use Normalization
            pie.prop(track_active, "use_normalization", text="Normalization")
        # Use Brute Force
            pie.prop(track_active, "use_brute", text="Use Brute Force")
            # Match Keyframe
            prop = pie.operator("wm.context_set_enum", text="Match Previous", icon='KEYFRAME_HLT')
            prop.data_path = "space_data.clip.tracking.tracks.active.pattern_match"
            prop.value = 'KEYFRAME'
            # Match Previous Frame
            prop = pie.operator("wm.context_set_enum", text="Match Keyframe", icon='KEYFRAME')
            prop.data_path = "space_data.clip.tracking.tracks.active.pattern_match"
            prop.value = 'PREV_FRAME'


##################################################################################################
#Tracking

class PIE_MT_tracking_track(Menu):
    # Tracking Operators
    bl_label = "Tracking"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.mode == 'TRACKING'

    def draw(self, context):
        space = context.space_data

        layout = self.layout
        pie = layout.menu_pie()
        # Track Backwards
        prop = pie.operator("clip.track_markers", icon='TRACKING_BACKWARDS')
        prop.backwards = True
        prop.sequence = True
        # Track Forwards
        prop = pie.operator("clip.track_markers", icon='TRACKING_FORWARDS')
        prop.backwards = False
        prop.sequence = True
        # Detect Features
        pie.operator("clip.detect_features", icon='ZOOM_SELECTED')



##################################################################################################
#Clip Setup

class PIE_MT_clipsetup_pie(Menu):
    # Setup the clip display options
    bl_label = "Clip and Display Setup"

    def draw(self, context):
        space = context.space_data

        layout = self.layout
        pie = layout.menu_pie()
        # Reload Footage
        pie.operator("clip.reload", text="Reload Footage", icon='FILE_REFRESH')
        # Prefetch Footage
        pie.operator("clip.prefetch", text="Prefetch Footage", icon='LOOP_FORWARDS')
        # Lock Selection
        pie.prop(space, "lock_selection", icon='LOCKED')
        # Set Scene Frames
        pie.operator("clip.set_scene_frames", text="Set Scene Frames", icon='SCENE_DATA')
        # Render Undistorted
        pie.prop(space.clip_user, "use_render_undistorted", text="Render Undistorted")
        # PIE: Marker Display
        icon = 'VISIBLE_IPO_ON' if space.show_disabled else 'VISIBLE_IPO_OFF'
        pie.prop(space, "show_disabled", text="Show Disabled", icon=icon)
        # Set Active Clip
        pie.operator("clip.set_active_clip", icon='CLIP')
        # Mute Footage
        pie.prop(space, "use_mute_footage", text="Mute Footage", icon='MUTE_IPO_ON')

##################################################################################################
#Registering

class PIE_MT_solver_pie(Menu):
    # Operators to solve the scene
    bl_label = "Solving"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.mode == 'TRACKING'

    def draw(self, context):
        clip = context.space_data.clip
        settings = getattr(getattr(clip, "tracking", None), "settings", None)

        layout = self.layout
        pie = layout.menu_pie()
        # Clear Solution
        pie.operator("clip.clear_solution", icon='FILE_REFRESH')
        # Solve Camera
        pie.operator("clip.solve_camera", text="Solve Camera", icon='OUTLINER_OB_CAMERA')
        # Use Tripod Solver
        if settings:
            pie.prop(settings, "use_tripod_solver", text="Tripod Solver")
        # create Plane Track
        pie.operator("clip.create_plane_track", icon='MATPLANE')
        # Set Keyframe A
        pie.operator("clip.set_solver_keyframe", text="Set Keyframe A",
                    icon='KEYFRAME').keyframe = 'KEYFRAME_A'
        # Set Keyframe B
        pie.operator("clip.set_solver_keyframe", text="Set Keyframe B",
                    icon='KEYFRAME').keyframe = 'KEYFRAME_B'
        # Clean Tracks
        prop = pie.operator("clip.clean_tracks", icon='X')
        # Filter Tracks
        pie.operator("clip.filter_tracks", icon='FILTER')
        prop.frames = 15
        prop.error = 2


#################################################################################################
#Registering

class PIE_MT_reconstruction_pie(Menu):
    # Scene Reconstruction
    bl_label = "Reconstruction"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.mode == 'TRACKING'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # Set Active Clip As Viewport Background
        pie.operator("clip.set_viewport_background", text="Set Viewport Background", icon='FILE_IMAGE')
        # Setup Tracking Scene
        pie.operator("clip.setup_tracking_scene", text="Setup Tracking Scene", icon='SCENE_DATA')
        # Setup Floor
        pie.operator("clip.set_plane", text="Setup Floor", icon='MESH_PLANE')
        # Set Origin
        pie.operator("clip.set_origin", text="Set Origin", icon='OBJECT_ORIGIN')
        # Set X Axis
        pie.operator("clip.set_axis", text="Set X Axis", icon='AXIS_FRONT').axis = 'X'
        # Set Y Axis
        pie.operator("clip.set_axis", text="Set Y Axis", icon='AXIS_SIDE').axis = 'Y'
        # Set Scale
        pie.operator("clip.set_scale", text="Set Scale", icon='ARROW_LEFTRIGHT')
        # Apply Solution Scale
        pie.operator("clip.apply_solution_scale", icon='ARROW_LEFTRIGHT')

#################################################################################################
#Registering

classes = (
    PIE_MT_init,
    PIE_MT_render,
    LAYOUT_MT_editor,
    PIE_MT_fsops,
    LAYOUT_MT_community,
    LAYOUT_MT_pipeline,
    PIE_MT_view,
    PIE_MT_shading,
    PIE_MT_snap,
    PIE_MT_select,
    PIE_MT_track,
    PIE_MT_tracking_marker,
    PIE_MT_tracking_track,
    PIE_MT_clipsetup_pie,
    PIE_MT_solver_pie,
    PIE_MT_reconstruction_pie,
    PIE_MT_topbar,
    PIE_MT_vef,
    # SubstancePainter,
    # SubstanceDesigner,
    # UnrealEngine,
    # VFXNatron,
    # Autodesk3DS,
    # AutodeskMaya,
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

        km = wm.keyconfigs.addon.keymaps.new(name="Clip", space_type='CLIP_EDITOR')

        kmi = km.keymap_items.new("wm.call_menu_pie", 'Q', 'PRESS', alt=True)
        kmi.properties.name = "PIE_MT_track"
        addon_keymaps.append((km, kmi))

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
