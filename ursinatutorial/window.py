from ursina import window                    # Import the ursina engine
from ursina import *                    # Import the ursina engine

app = Ursina()                          # Initialise your Ursina app

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

app.run()                                 # Run the app
