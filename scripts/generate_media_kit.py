"""Create clearly labelled simulated-demo media for Product Hunt/GitHub Pages."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).parents[1]; out=ROOT/'site/media'; out.mkdir(parents=True,exist_ok=True)
try: font=lambda n,b=False:ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf' if b else 'C:/Windows/Fonts/arial.ttf',n)
except OSError: font=lambda n,b=False:ImageFont.load_default()
def frame(step, caption, fault=False, size=(1200,630)):
 im=Image.new('RGB',size,'#0e171b');d=ImageDraw.Draw(im); w,h=size
 d.text((54,42),'LOOM',font=font(25,True),fill='#eff9f6');d.text((138,42),'FORGE',font=font(25,True),fill='#51c7c1');d.text((54,82),'INTERACTIVE DEMO  /  SIMULATED',font=font(15,True),fill='#51c7c1')
 d.rounded_rectangle((60,145,w-60,h-72),18,fill='#18262b',outline='#3f6767',width=2)
 # machine
 d.rounded_rectangle((390,435,920,510),15,fill='#202a2e');d.polygon([(430,435),(430,225),(480,185),(510,435)],fill='#e0e3df');d.polygon([(875,435),(875,185),(920,225),(920,435)],fill='#e0e3df');d.rectangle((770,160,820,435),fill='#202a2e');d.rectangle((480,390,720,420),fill='#334248');
 for i,c in enumerate(['#ef705b','#333333','#e8c34a','#4a9eff']):d.rounded_rectangle((500+i*38,396,522+i*38,415),3,fill=c)
 d.rounded_rectangle((630,350,720,390),4,fill='#177f88');x=520+step*35;y=220+min(step,4)*22;d.rounded_rectangle((x,y,x+64,y+95),5,fill='#3b4d53');d.rounded_rectangle((x+14,y+95,x+50,y+142),5,fill='#4fc6c1');
 d.text((90,185),['LOAD & VALIDATE','PICKUP','CAVITY APPROACH','GUIDED INSERTION','GUIDE RELEASE','ELECTRICAL TEST','COMPLETE'][min(step,6)],font=font(25,True),fill='#ef705b' if fault else '#ffffff')
 d.text((90,230),caption,font=font(18),fill='#b8c9c7');d.text((90,275),'LF-P1-R02  •  4-circuit Mini-Fit Jr.  •  synthetic force trace',font=font(14),fill='#8da6a6')
 for i in range(7):d.rectangle((90+i*48,530,126+i*48,540),fill='#ef705b' if fault and i==step else ('#4fc6c1' if i<=step else '#31454a'))
 d.text((w-390,h-40),'DEVELOPMENT DESIGN — NOT HARDWARE EVIDENCE',font=font(12,True),fill='#9bb0ae')
 return im
hero=frame(3,'Try a guided insertion sequence, inspect synthetic force data, and introduce a fault.',False);hero.save(out/'product-hunt-cover.png',optimize=True)
frames=[frame(i,['Operator presents a labelled pre-crimped lead.','Head captures insulation behind the terminal.','Recipe-bound cavity approach.','Bounded force/travel insertion.','Split guide releases the inserted lead.','Mating test checks the expected map.','Operator removes completed assembly.'][i]) for i in range(7)]
frames[0].save(out/'loomforge-simulated-walkthrough.gif',save_all=True,append_images=frames[1:],duration=950,loop=0,optimize=True)
fault=[frame(0,'Operator loads an indexed lead.'),frame(2,'Door opening is introduced during the simulated cycle.',True),frame(2,'Protective stop; recovery is required. No automatic restart.',True)]
fault[0].save(out/'loomforge-fault-recovery.gif',save_all=True,append_images=fault[1:],duration=1200,loop=0,optimize=True)
print('Generated Product Hunt cover and two simulated walkthrough GIFs in',out)
