// LF-P1-R02. Parametric conceptual CAD. Dimensions mirror parameters.json.
$fn=36; W=560; D=430; H=520; plinth=105; railX=300; trayPitch=26;
module box(x,y,z,c=[.15,.17,.19],a=1){ color(concat(c,[a])) cube([x,y,z],center=true); }
module rounded(x,y,z,r,c){ color(c) minkowski(){cube([x-2*r,y-2*r,z],center=true);cylinder(r=r,h=.1,center=true);} }
module support(side){color([.83,.84,.82]) translate([side*238,35,290]) rotate([0,side*8,0]) polyhedron(points=[[-28,-155,-185],[28,-155,-185],[28,140,-185],[-28,140,-185],[-20,-115,185],[20,-115,185],[20,105,185],[-20,105,185]],faces=[[0,1,2,3],[4,7,6,5],[0,4,5,1],[1,5,6,2],[2,6,7,3],[3,7,4,0]]);}
rounded(W,D,plinth,18,[.12,.14,.16]); translate([0,-145,61]) box(470,120,16,[.78,.79,.77]);
for(x=[-220,220])for(y=[-155,155])translate([x,y,-5])color([.08,.09,.1])cylinder(h=22,r=18);
support(-1);support(1);translate([0,156,300])box(370,38,355,[.12,.14,.16]);
translate([0,118,405])box(railX,16,12,[.22,.25,.27]);translate([0,88,405])box(railX,16,12,[.22,.25,.27]);
translate([0,102,360])box(72,62,28,[.25,.31,.33]);translate([0,92,300])box(56,56,118,[.20,.24,.26]);translate([0,92,235])box(45,45,16,[.55,.55,.56]);translate([0,92,205])box(38,38,40,[.55,.58,.57]);
for(x=[-130:20:0])translate([x,128,432])box(16,22,12,[.08,.09,.1]);
translate([0,-92,151])box(82,70,30,[.15,.45,.52]);translate([0,-56,152])box(48,24,32,[.68,.62,.22]);
translate([0,-174,133])box(390,82,30,[.18,.24,.27]);for(x=[-143:trayPitch:143]){translate([x,-174,158])box(14,42,16,[.28,.32,.34]);translate([x,-142,160])box(4,10,28,[.14,.65,.67]);}
translate([0,20,478])box(260,25,18,[.14,.16,.18]);translate([0,3,455])color([.08,.09,.1])cylinder(h=38,r=25);translate([-145,5,445])box(120,10,8,[.95,.95,.88]);translate([145,5,445])box(120,10,8,[.95,.95,.88]);translate([0,38,440])box(80,10,8,[.90,.94,.94]);
translate([0,-218,163])rotate([25,0,0])box(250,55,85,[.75,.77,.75]);translate([0,-240,183])rotate([25,0,0])box(138,8,58,[.08,.12,.14]);translate([175,-240,180])color([.8,.08,.06])cylinder(h=18,r=20);
color([.45,.75,.78,.22])translate([0,-42,315])box(398,6,265,[.45,.75,.78],.22);translate([0,125,495])box(220,10,8,[.08,.62,.64]);
