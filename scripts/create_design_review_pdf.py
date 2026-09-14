"""Dependency-free design-review PDF builder for LF-P1-R02."""
from pathlib import Path
ROOT=Path(__file__).parents[1]; out=ROOT/'reports'/'loomforge-r02-design-review.pdf'; out.parent.mkdir(exist_ok=True)
pages=[
 ['LOOMFORGE LF-P1-R02','DESIGN REVIEW / DEVELOPMENT PACKAGE','Scope of supply: LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and complete the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use.','Selected configuration: compact benchtop, broad plinth, folded swept side supports, rear structural spine, transparent chamber, angled console and front loading deck.','Status: conceptual CAD and simulated software. Not production-ready or certified.'],
 ['SELECTED MECHANICAL ARRANGEMENT','Overall envelope: 560 W x 430 D x 520 H mm. Front deck carries 12-slot manual tray, Mini-Fit Jr cartridge and mating test plug.','Rear spine carries X/Y/Z head, rails, cable chain, camera, separate work/vision light zones and rear service routing.','Head: 210 mm X, 110 mm Y, 72 mm Z; proposed 32 mm controlled insertion; inline force mount; soft insulation gripper; split release guide.','The guide supports terminal to a proposed maximum 12 mm from cavity; this is an experimental constraint requiring bench trials.'],
 ['OPERATOR AND SAFETY FLOW','Open upward hinged guard; manually load terminal-forward wire and route slack through comb. Close guard, validate recipe/fixture/calibration, then start supervised sequence.','Head picks insulated lead, transfers under guide, inserts against bounded force/travel, opens split guide and releases. Mating/far-end test evaluates mapping; operator removes completed assembly.','Guard: proposed 6 mm polycarbonate, 105 degree opening, dual-channel interlock. Closing never restarts. E-stop remains on right console edge.','Lighting: 12 W diffuse work, 6 W vision zone with baffle/exposure control, 3 W status guide. Lighting is not a safety system.'],
 ['FIT REVIEW AND MANUFACTURING','Manual CAD-envelope review: home/extremes, pickup, approach, full insertion, guide release, door open, fixture removal and rear service. No automated collision, flexible-wire, human-factors or force validation performed.','Part register: hardware/mechanical/parts.csv. Concept CAD: hardware/mechanical/source/loomforge.scad. Central parameters: parameters.json.','Prototype path: folded/welded plinth, folded aluminum supports/console, machined spine/head/fixture, printed ESD tray, purchased motion/safety/light modules.','Critical release blockers: controlled connector drawings, tolerance stack, guide trials, purchased component selection, released electrical/safety design, CAD drawings and site validation.'],
 ['VISUAL AND MOTION DELIVERABLES','CAD-generated STL: hardware/mechanical/exports/loomforge-r02-assembly.stl. CAD render: hardware/mechanical/renders/cad-front-hero.png.','CAD-derived technical SVG set: front/rear/side/top/open-loading/cutaway/exploded/insertion/fixture/lighting/operator-sequence.','Simulated motion demonstrator: reports/motion-demonstration.html. It shares R02 layout parameters but establishes neither insertion success nor cycle time.','Next physical experiment: instrument guided insertion with 30+ housings and 120+ approved pre-crimped leads; compare force/travel signatures with approved inspection and retention evidence.']]
def esc(s): return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
objects=[]; page_ids=[]; font_id=3
for n, lines in enumerate(pages,1):
 stream=['BT /F1 24 Tf 1 0 0 1 54 720 Tm ('+esc(lines[0])+') Tj','/F1 12 Tf 1 0 0 1 54 690 Tm ('+esc(lines[1])+') Tj']
 y=650
 for line in lines[2:]:
  words=line.split(); rows=[]; cur=''
  for w in words:
   if len(cur)+len(w)>88: rows.append(cur);cur=w
   else: cur=(cur+' '+w).strip()
  rows.append(cur)
  for row in rows: stream.append(f'/F1 11 Tf 1 0 0 1 54 {y} Tm ('+esc(row)+') Tj'); y-=18
  y-=12
 stream+=['/F1 9 Tf 1 0 0 1 54 38 Tm (LoomForge LF-P1-R02 - development design - page '+str(n)+') Tj','ET']
 content='\n'.join(stream).encode(); objects.append((f'<< /Length {len(content)} >>\nstream\n'.encode()+content+b'\nendstream')); page_ids.append(None)
# objects: catalog, pages, font then contents/pages generated after ids known
base=[b'<< /Type /Catalog /Pages 2 0 R >>',None,b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>']
allobj=base+objects
for i in range(len(pages)):
 cid=4+i; pid=4+len(pages)+i; page_ids[i]=pid; allobj.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R >> >> /Contents {cid} 0 R >>'.encode())
kids=' '.join(f'{x} 0 R' for x in page_ids); allobj[1]=f'<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>'.encode()
data=b'%PDF-1.4\n'; offsets=[0]
for i,obj in enumerate(allobj,1): offsets.append(len(data));data+=f'{i} 0 obj\n'.encode()+obj+b'\nendobj\n'
xref=len(data);data+=f'xref\n0 {len(allobj)+1}\n0000000000 65535 f \n'.encode()+b''.join(f'{o:010d} 00000 n \n'.encode() for o in offsets[1:]);data+=f'trailer << /Size {len(allobj)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode();out.write_bytes(data);print(out)
