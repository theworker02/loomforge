"""Stage only public, reviewable LoomForge artifacts for static GitHub Pages."""
from pathlib import Path
from shutil import copy2
root=Path(__file__).parents[1]; site=root/'site'; assets=site/'assets'; downloads=site/'downloads'
assets.mkdir(exist_ok=True); downloads.mkdir(exist_ok=True)
for source,target in [
 (root/'hardware/mechanical/renders/cad-front-hero.png',assets/'cad-front-hero.png'),
 (root/'hardware/mechanical/renders/lighting-camera.svg',assets/'lighting-camera.svg'),
 (root/'reports/loomforge-r02-design-review.pdf',downloads/'loomforge-r02-design-review.pdf'),
 (root/'docs/manufacturing/unresolved-design-items.md',downloads/'unresolved-design-items.md'),
 (root/'hardware/mechanical/exports/loomforge-r02-assembly.stl',downloads/'loomforge-r02-assembly.stl')]:
 copy2(source,target)
print('Staged GitHub Pages assets:', ', '.join(p.name for p in [assets/'cad-front-hero.png',assets/'lighting-camera.svg',downloads/'loomforge-r02-design-review.pdf',downloads/'unresolved-design-items.md',downloads/'loomforge-r02-assembly.stl']))
