import arcade

first_window = arcade.open_window(1000, 1000, "Hello Comp151")
arcade.set_background_color(arcade.color.DEEP_SAFFRON)
arcade.start_render()
arcade.draw_line(200,500,800, 500, arcade.color.AFRICAN_VIOLET, 5)
arcade.draw_line(200, 100, 200, 650, arcade.color.CADMIUM_RED, 4)
arcade.finish_render()
arcade.run()