# CAD regeneration

`loomforge.scad` is native parametric source for a conceptual envelope: base, simplified motion/head stack, fixture cartridge, 12-slot tray, guard, and feet. Regenerate with `openscad -o hardware/mechanical/exports/loomforge-assembly.stl hardware/mechanical/source/loomforge.scad` and inspect it before use.

OpenSCAD/FreeCAD/CadQuery were unavailable in this environment. STEP, DXF, dimensioned drawings, section/exploded views, and renders are deliberately incomplete—not fake exports. Controlled connector/rail dimensions and a CAD workstation are required next.

Part IDs: LF-100 base, LF-110 gantry, LF-200 head, LF-210 guide, LF-220 gripper, LF-300 fixture plate, LF-310 fixture, LF-400 tray, LF-500 guard, LF-600 electronics enclosure.
