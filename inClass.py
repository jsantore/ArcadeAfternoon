import arcade

demo_window = arcade.open_window(1000, 900, "Graph Paper Demo")
arcade.set_background_color(arcade.color.ARSENIC)
arcade.start_render()
for xpos in range(100, 1000, 100):
    arcade.draw_line(xpos,0,xpos,900, arcade.color.LIGHT_CYAN, 4)
for ypos in range(100, 900, 100):
    arcade.draw_line(0, ypos,1000,ypos, arcade.color.LIGHT_CYAN, 4)
arcade.finish_render()
arcade.run()