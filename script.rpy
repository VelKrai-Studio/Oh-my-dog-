# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# DEFINE: Characters
# =======================================
define m = Character("Mochi")
define fi = Character("Fionna")
define fr = Character("Fred")
define p = Character("Pilar")
define j = Character("José")

# DEFINE: Character images
# =======================================
image Pilar_neutral = "images/Characters/Pilar/ph_Pilar_neutral.png"
image Jose_think = "images/Characters/Jose/ph_Jose_think.png"

# DEFINE: Background images
# =======================================
image bg magicShop = "images/Backgrounds/ph_magicShop.jpg"

# DEFINE: Image movements
# =======================================
transform moveRight:
    linear 0.5 xpos 0.85

transform moveLeft:
    linear 0.5 xpos 0.15

transform jumpUpDown:
    linear 0.2 ypos 0.85
    linear 0.2 ypos 1.0
    linear 0.2 ypos 0.85
    linear 0.2 ypos 1.0

transform shake (rate = 0.09):
    linear rate xoffset 2 yoffset -6
    linear rate xoffset -2.8 yoffset -2
    linear rate xoffset 2.8 yoffset -2
    linear rate xoffset -2 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg magicShop
    play music "audio/BGM/ph_GhostNGhost - Lazy Sunday.ogg"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Pilar_neutral
    # These display lines of dialogue.

    p "Oh boy, espero que no aparezca otro personaje y me obligue desplazarme a la izquerda."
    show Pilar_neutral at moveLeft
    show Jose_think

    j "HEY HEY PILAR, mira como me voy a la derecha wooooooooooooo!"

    show Jose_think at moveRight
    j "Y AHORA VOY A SALTAR DE FELICIDAD"

    show Jose_think at jumpUpDown
    j "hell yeah"

    p "Pues yo se intensify, observa:"

    show Pilar_neutral at shake
    p "RR RR RR RR RR RR"

    # This ends the game.

    return
