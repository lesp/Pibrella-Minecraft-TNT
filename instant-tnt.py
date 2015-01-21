import pibrella
#Import the Pibrella module so that we can play with it
import time
#We are now masters of time, like Doctor Who, but with a far smaller budget
import mcpi.minecraft as minecraft
#We import the Minecraft module so that we can use it in Python

mc = minecraft.Minecraft.create()
#We create a connection between Python and the Minecraft game world.

#We define a function and call it button_changed
def button_changed(pin):
    pibrella.buzzer.success()
    #Plays a jaunty little tune using the Pibrella buzzer
    x,y,z = mc.player.getPos()
    #Create a cube of TNT
    tnt = 46
    mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, tnt, 1)
    
pibrella.button.changed(button_changed)
#This waits for a button press and when detected it runs the button_changed function.
