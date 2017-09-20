from PIL import Image,ImageDraw
import random

##creation d'une image avec un pavage truchet.

def createImg(colorback,colorfront,colorborder,taille,mode):
  #antialiasing taille *10 et resize 10 fois + petit avec antialiasing
  ntaille = taille*10
  epaisseur = 2*10
  imres = Image.new('RGB', (ntaille,ntaille),colorback)
  draw = ImageDraw.Draw(imres)
  #premier quart de cercle avec bordure
  draw.ellipse((-ntaille/2, -ntaille/2, ntaille/2+epaisseur, ntaille/2+epaisseur), fill=(colorborder))
  draw.ellipse((-ntaille/2+epaisseur, -ntaille/2+epaisseur, (ntaille/2)-epaisseur, (ntaille/2)-epaisseur), fill=(colorfront))
  #deuxieme quart de cercle  avec bordure  
  draw.ellipse((ntaille/2-epaisseur, ntaille/2-epaisseur, ntaille+ntaille/2, ntaille+ntaille/2), fill=(colorborder))
  draw.ellipse((ntaille/2+epaisseur, ntaille/2+epaisseur, (ntaille+ntaille/2)-epaisseur, (ntaille+ntaille/2)-epaisseur), fill=(colorfront))
  #Si mode = 2 on fait un flip de l'image
  if mode==2:
    imres=imres.transpose(Image.FLIP_LEFT_RIGHT)
  #resize 10fois plus petit pour l'antialiasing
  imres = imres.resize((taille,taille), Image.ANTIALIAS)
  return imres

#image carre avec Nbre carre truchet  en ligne et en colonne
Nbre=11
#taille du carre truchet  en pixel
taille=65
#changer de seed pour une autre image 
seed=10
# les couleurs du pavage  RGBA
colorborder =  (255,255,255,255)
colorfront = (255,221,221,255)
colorback = (221,221,255,255)
random.seed(seed)
tailleImage=taille*Nbre
new_im = Image.new('RGB', (tailleImage,tailleImage))
# on cree les 4 briques du pavage truchet
im1=createImg(colorfront,colorback,colorborder,taille,1);
im2 =createImg(colorback,colorfront,colorborder,taille,1);
im3 =createImg(colorfront,colorback,colorborder,taille,2);
im4 =createImg(colorback,colorfront,colorborder,taille,2);
#on fait le pavage les briques 1 et 4 sont sur les case impaire les briques 2,3 sur les paires
for y in range(0,Nbre):
  for x in range(0,Nbre):
    if (x+y)%2==1:
      if random.randint(0,100)>=50:
        im=im1
      else:
        im=im4
    else:
      if random.randint(0,100)>=50:
        im=im2
      else:
        im=im3
    new_im.paste(im, (x*taille,y*taille,x*taille+taille,y*taille+taille))
new_im.save("truchet.png", "PNG")
raw_input('Appuyer une touche pour quitter')


  
  