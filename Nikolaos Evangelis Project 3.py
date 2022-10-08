import arcade

myWindow = arcade.open_window(800, 800, "map")
arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
#The sea.
arcade.start_render()

arcade.draw_line(200, 200, 800, 800, arcade.color.BROWN)
arcade.draw_line(100, 100, 400, 400, arcade.color.BROWN)
#Intended to be a brown Napoleonic era vessel
arcade.draw_circle_filled(250, 250, 300, arcade.color.BLACK_LEATHER_JACKET)
arcade.draw_triangle_filled(150, 150, 200, 100, 100, 100, arcade.color.BROWN)
arcade.draw_triangle_filled(650, 650, 600, 700, 700, 700, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(380, 380, 210, 210, arcade.color.GREEN)
#The great shore.
arcade.draw_arc_filled(550, 700, 400, 500, arcade.color.BROWN, 0, 100)
arcade.draw_line(330, 330, 660, 660, arcade.color. BLACK_LEATHER_JACKET)
arcade.draw_circle_filled(120, 120, 200, arcade.color.LIGHT_CORNFLOWER_BLUE)
#The inner harbor
arcade.draw_line(300, 300, 500, 500, arcade.color.BLUE)


arcade.run()