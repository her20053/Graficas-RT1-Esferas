from Raytracer import Raytracer
import Figures


raycastObject = Raytracer(800, 800)

raycastObject.scene = Figures.snowman
raycastObject.render()
raycastObject.write('Snowman.bmp')
