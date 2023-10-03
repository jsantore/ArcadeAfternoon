import arcade

our_window = arcade.open_window(1000, 1000, "Jack-o-lantern")

arcade.set_background_color(arcade.color.GREEN)
message = arcade.Text("We did this in class",400, 900,
                      arcade.color.AMAZON, 24)
arcade.start_render()
message.draw()
arcade.draw_circle_filled(500,500, 400, arcade.color.PUMPKIN)
arcade.draw_lrtb_rectangle_filled(450, 550, 550, 450,
                                  arcade.color.BLACK)
arcade.draw_triangle_filled(250,650, 350, 650, 300, 800,
                            arcade.color.JET)
arcade.draw_triangle_filled(550, 650, 600, 700, 650, 650,
                            arcade.color.YANKEES_BLUE)
arcade.draw_arc_filled(500, 350, 600, 200,
                       arcade.color.BLACK, -180, 0)

arcade.finish_render()

arcade.run()