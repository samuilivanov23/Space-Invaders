import turtle
import math

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("space_invaders_background.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Set up the border of the gme
border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.speed(0)
border_pen.pensize(3)

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.speed(0)
score_pen.color("white")
score_pen.setposition(-290, 280)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



#Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

#Create the enemies
#Choose the number of enemies
number_of_enemies = 5

enemy_y_decrement_offset = 35
enemy_x_offset = 40
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

index_of_current_enemy = 0
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    enemy_x_position = -200 + (index_of_current_enemy * enemy_x_offset)
    enemy_y_position = 250
    enemy.setposition(enemy_x_position, enemy_y_position)
    index_of_current_enemy += 1

enemy_speed = 5

#Create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.setheading(90)
bullet.hideturtle()
bullet.speed(0)

bullet_speed = 15 # to be way faster than the other objects

#Move player left and right
def move_left():
    player_x_position = player.xcor();
    player_x_position -= player_speed
    if player_x_position < -280:
        player_x_position = -280
    player.setx(player_x_position)

def move_right():
    player_x_position = player.xcor();
    player_x_position += player_speed
    if player_x_position > 280:
        player_x_position = 280
    player.setx(player_x_position)

#Fire a bullet
def fire_bullet():
    if not bullet.isvisible():
        x_pos = player.xcor()
        y_pos = player.ycor() + 10
        bullet.setposition(x_pos, y_pos)
        bullet.showturtle()

#Chek if there is collision between twp turtle objects
def isCollission(turtle1, turtle2):
    distance = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(), 2) + math.pow(turtle1.ycor() - turtle2.ycor(), 2))

    if distance < 15:
        return True
    else:
        return False

#main game loop
game_is_over = False
while not game_is_over:
    #Move the enemies
    for enemy in enemies:
        enemy_x_position = enemy.xcor()
        enemy_x_position += enemy_speed
        enemy.setx(enemy_x_position)

        #Check if the enemy touches the bounds of the border
        if enemy_x_position < -280:
            #Move all of the enemies down
            for enemy in enemies:
                enemy_y_position = enemy.ycor()
                enemy_y_position -= enemy_y_decrement_offset;
                enemy.sety(enemy_y_position)
            enemy_speed *= -1

        elif enemy_x_position > 280:
            #Move all of the enemies down
            for enemy in enemies:
                enemy_y_position = enemy.ycor()
                enemy_y_position -= enemy_y_decrement_offset;
                enemy.sety(enemy_y_position)
            enemy_speed *= -1

        #Check if there is a collision between the bullet and the enemy
        if isCollission(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400) # to be outside the board end not interrupt the game
            #Reset the enemy
            enemy.setposition(-200, 250)
            score += 10
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align = "left", font = ("Arial", 14, "normal"))

        #Check if there is a collision between the enemy and the player
        if isCollission(player, enemy):
            enemy.hideturtle()
            player.hideturtle()
            print("Game over")
            game_is_over = True

    #Chck if it is possible to fire a bullet
    if bullet.isvisible():
        bullet_y_position = bullet.ycor()
        bullet_y_position += bullet_speed
        bullet.sety(bullet_y_position)

    #Chek if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()

    #Set up the key bindings
    turtle.listen()
    turtle.onkeypress(move_left, "Left")
    turtle.onkeypress(move_right, "Right")
    turtle.onkeypress(fire_bullet, "space")

#Determine when to finish the program
turtle.done()
