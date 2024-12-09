from PIL import Image, ImageDraw
import random

## Creation d'une image avec un pavage truchet.

def createImg(bg_color, fg_color, border_color, size, mode):
    # Antialiasing taille *10 et resize 10 fois + petit avec antialiasing
    nsize = size * 10
    thickness = 2 * 10
    imres = Image.new('RGB', (nsize, nsize), bg_color)
    draw = ImageDraw.Draw(imres)
    # Premier quart de cercle avec bordure
    draw.ellipse((-nsize / 2, -nsize / 2, nsize / 2 + thickness, nsize / 2 + thickness), fill=(border_color))
    draw.ellipse((-nsize / 2 + thickness, -nsize / 2 + thickness, (nsize / 2) - thickness, (nsize / 2) - thickness), fill=(fg_color))
    # Deuxieme quart de cercle avec bordure
    draw.ellipse((nsize / 2 - thickness, nsize / 2 - thickness, nsize + nsize / 2, nsize + nsize / 2), fill=(border_color))
    draw.ellipse((nsize / 2 + thickness, nsize / 2 + thickness, (nsize + nsize / 2) - thickness, (nsize + nsize / 2) - thickness), fill=(fg_color))
    # Si mode = 2 on fait un flip de l'image
    if mode == 2:
        imres = imres.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    # Resize 10 fois plus petit pour l'antialiasing
    imres = imres.resize((size, size), Image.Resampling.LANCZOS)

    return imres

# Image carre avec Nbre carre truchet en ligne et en colonne
Nbre = 11
# Taille du carre truchet en pixel
taille = 65
# Changer de seed pour une autre image
seed = 10
# Les couleurs du pavage RGBA
colorborder = (255, 255, 255, 255)
colorfront = (255, 221, 221, 255)
colorback = (221, 221, 255, 255)
random.seed(seed)
tailleImage = taille * Nbre
new_im = Image.new('RGB', (tailleImage, tailleImage))
# On cree les 4 briques du pavage truchet
im1 = createImg(colorfront, colorback, colorborder, taille, 1)
im2 = createImg(colorback, colorfront, colorborder, taille, 1)
im3 = createImg(colorfront, colorback, colorborder, taille, 2)
im4 = createImg(colorback, colorfront, colorborder, taille, 2)
# On fait le pavage les briques 1 et 4 sont sur les cases impaires les briques 2,3 sur les paires
for y in range(0, Nbre):
    for x in range(0, Nbre):
        if (x + y) % 2 == 1:
            if random.randint(0, 100) >= 50:
                im = im1
            else:
                im = im4
        else:
            if random.randint(0, 100) >= 50:
                im = im2
            else:
                im = im3
        new_im.paste(im, (x * taille, y * taille, x * taille + taille, y * taille + taille))
new_im.save("truchet.png", "PNG")
input('Appuyer une touche pour quitter')
