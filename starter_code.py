import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
#Define Classes
class Game():
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        #Set game values
        # TODO: assign 1 to self.round_number
        self.round_number = 1
        # TODO: assign 0 to self.score
        self.score = 0

        # TODO: assign player to self.player
        self.player = player
        # TODO: assign alien_group to self.alien_group
        self.alien_group = alien_group
        # TODO: assign player_bullet_group to self.player_bullet_group
        self.player_bullet_group = player_bullet_group
        # TODO: assign alien_bullet_group to self.alien_bullet_group
        self.alien_bullet_group = alien_bullet_group

        #Set sounds and music
        # TODO: assign pygame.mixer.Sound("new_round.wav") to self.new_round_sound
        self.new_round_sound = pygame.mixer.Sound('sounds/new_round.wav')
        # TODO: assign pygame.mixer.Sound("breach.wav") to self.breach_sound
        self.breach_sound = pygame.mixer.Sound('sounds/breach.wav')
        # TODO: assign pygame.mixer.Sound("alien_hit.wav") to self.alien_hit_sound
        self.alien_hit_sound = pygame.mixer.Sound('sounds/alien_hit.wav')
        # TODO: assign pygame.mixer.Sound("player_hit.wav") to self.player_hit_sound
        self.player_hit_sound = pygame.mixer.Sound('sounds/player_hit.wav')

        #Set font
        # TODO: assign pygame.font.Font("Facon.ttf", 32) to self.font
        self.font = pygame.font.Font("Facon.ttf", 32)

    def update(self):
        """Update the game"""
        # TODO: call self.shift_aliens() with no args
        self.shift_aliens()
        # TODO: call self.check_collisions() with no args
        self.check_collisions()
        # TODO: call self.check_round_completion() with no args
        self.check_round_completion()

    def draw(self):
        """Draw the HUD and other information to display"""
        WHITE = (255, 255, 255)

        # Set text
        # TODO: assign self.font.render() to score_text with f"Score: {self.score}, True, and WHITE as args
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        # TODO: assign score_text.get_rect() to score_rect
        score_rect = score_text.get_rect()
        # TODO: assign WINDOW_WIDTH // 2 to self_rect.centerx
        self_rect.centerx = WINDOW_WIDTH // 2

        # TODO: assign 10 to score_rect.top
        score_rect.top = 10


        # TODO: assign self.font.render() to round_text with f"Round: {self.round_number}, True, and WHITE as args
        round_text = self.font.render(f"Round: {self.round_number}", True, WHITE)
        # TODO: assign round_text.get_rect() to round_rect
        round_rect = round_text.get_rect()
        # TODO: assign (20, 10) to round_rect.topleft
        round_rect.topleft = (20, 10)

        # TODO: assign self.font.render() to lives_text with f"Lives: {self.player.lives}, True, and WHITE as args
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        # TODO: assign lives_text.get_rect() to lives_rect
        lives_rect = lives_text.get_rect()
        # TODO: assign (20, 10) to lives_rect.topleft
        lives_rect.topleft = (20, 10)

        #Blit the HUD to the display
        # TODO: call display_surface.blit() with score_text, score_rect as the args
        # TODO: call display_surface.blit() with round_text, round_rect as the args
        # TODO: call display_surface.blit() with lives_text, lives_rect as the args
        # TODO: call pygame.draw.line() with display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4 as its args
        # TODO: repeat the last function call but with display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4 as its args
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        pass

    def check_collisions(self):
        """Check for collisions"""
        #See if any bullet in the player bullet group hits an alien in the alien group
        # TODO: if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            # TODO: call self.alien_hit_sound.play()
            self.alien_hit_sound.play()
            # TODO: add 100 to self.score
            self.score += 100


        #See if the player has collided with any bullet in the alien bullet group
        # TODO: if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            # TODO: call self.player_hit_sound.play()
            # TODO: subtract 1 from self.player.lives

            # TODO: call self.check_game_status() with "You've been hit!", "Press 'Enter' to continue" as its 2 args
        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.alien_hit_sound.play()
            self.score -= 1
            self.check_game_status("You've been hit!", "Press 'Enter' to continue")

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        # TODO: if not (self.alien_group):
            # TODO: add 1000 * self.round_number to self.score (don't forget it's += when I say add to)
            # TODO: add 1 to self.round_number
            # TODO: call self.start_new_round() with no args
        if not (self.alien_group):
            self.score = 1000 * self.round_number
            self.start_new_round()

    def start_new_round(self):
        """Start a new round"""
        # Create a grid of Aliens 11 columns and 5 rows.
        # TODO: for col in range(11):
        for col in range(11):
            # TODO: for row in range(5):
            for row in range(5):
                # TODO: assign Alien() to alien with the following args for Alien()
                alien = Alien(64 + col * 64,64 + row * 64, self.round_number,self.alien_bullet_group)
                # first arg (x) is going to be 64 + col * 64
                # second arg (y) is going to be 64 + row * 64
                # third arg (velocity) is going to be self.round_number
                # fourth arg is self.alien_bullet_group
                # TODO: call self.alien_bullet_group.add() with alien as its argument
                self.alien_bullet_group.add(alien)
        # Pause the game and prompt user to start
        # TODO: call self.new_round_sound.play() with no args
        self.new_round_sound.play()
        # TODO: call self.pause_game() with the following args for self.pause_game()
        self.pause_game(f"Space Invaders Round {self.round_number}","Press 'Enter' to being")
        # first arg (main_text) f"Space Invaders Round {self.round_number}"
        # second arg (sub_text) "Press 'Enter' to being"

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        # TODO: call self.alien_bullet_group.empty() with no args
        # TODO: same for self.player_bullet_group.empty()
        # TODO: call self.player.reset()
        # TODO: for alien in self.alien_group:
            # TODO: call alien.reset()
        self.alien_bullet_group()
        self.player_bullet_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien,reset()

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        global running

        # Set Colors
        # TODO: assign (255, 255, 255) to WHITE
        WHITE = (255, 255, 255)
        # TODO: repeat using (0, 0, 0) for BLACK
        BLACK = (0, 0, 0)

        # Create main pause text
        # TODO: assign self.font.render(main_text, True, WHITE) to main_text
        main_text = self.font.render(main_text, True, WHITE)
        # TODO: assign main_text.get_rect() to main_rect
        main_rect = main_text.get_rect()
        # TODO: assign (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2) to main_rect.center
        main_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        #Create sub pause text
        # TODO: assign self.font.render(sub_text, True, WHITE) to sub_text
        sub_text = self.font.render(sub_text, True, WHITE)
        # TODO: assign sub_text.get_rect() to sub_rect
        sub_rect = sub_text.get_rect()
        # TODO: assign (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64) to sub_rect.center
        sub_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

        #Blit the pause text
        # TODO: call display_surface.fill() with BLACK as its argument
        # TODO: call display_surface.blit() with main_text, and main_rect as its args
        # TODO: call display_surface.blit() with sub_text, and sub_rect as its args
        # TODO: call pygame.display.update() with no args
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()
        #Pause the game until the user hits enter
        #TODO: assign True to is_paused
        is_paused = True
        #TODO: while is_paused:
        while is_paused:
            #TODO: for event in pygame.event.get():
            for event in pygame.event.get():
                # The user wants to play again
                # TODO: if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    # TODO: if event.key == pygame.K_RETURN:
                    if event.key == pygame.K_RETURN:
                        # TODO: assign False to is_paused
                        is_paused = False
                # The user wants to quit
                # TODO: if event.type == pygame.QUIT:
                    # TODO: assign False to is_paused
                    # TODO: assign False to running
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    def reset_game(self):
        """Reset the game"""
        # TODO: call self.pause_game() with the following args: f"Final Score: {self.score}", "Press 'Enter' to play again")
    self.pause_game( f"Final Score: {self.score}", "Press 'Enter' to play again")

    # Reset game values
        # TODO: assign 0 to self.score
        self.score = 0
        # TODO: assign 1 to self.round_number
        self.round_number = 1

        # TODO: assign 5 to self.player.lives
        self.player.lives = 5

        # Empty groups
        # TODO: call self.alien_group.empty()
        # TODO: repeat for alien_bullet_group
        # TODO: repeat for player_bullet_group
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        # Start a new game
        # TODO: call self.start_new_round()
        self.start_new_round()


class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        # TODO: assign pygame.image.load("player_ship.png") to self.image
        self.image = pygame.image.load("player_ship.png")
        # TODO: assign self.image.get_rect() to self.rect
        self.rect = self.image.get_rect()
        # TODO: assign WINDOW_WIDTH //2 to self.rect.centerx
        self.rect.centerx = WINDOW_WIDTH //2
        # TODO: assign WINDOW_HEIGHT to self.rect.bottom
        self.rect.bottom = WINDOW_HEIGHT

        # TODO: assign 5 to self.lives
        self.lives = 5
        # TODO: assign 8 to self.velocity
        self.velocity = 8
        # TODO: assign bullet_group to self.bullet_group
        self.bullet_group = bullet_group

        # TODO: assign pygame.mixer.Sound("player_fire.wav") to self.shoot_sound
        self.shoot_sound = pygame.mixer.Sound("player_fire.wav")

    def update(self):
        """Update the player"""
        # TODO: assign pygame.key.get_pressed() to keys
        pygame.key.get_pressed(keys)
        #Move the player within the bounds of the screen
        # TODO: if keys[pygame.K_LEFT] and self.rect.left > 0:
            # TODO: subtract self.velocity from self.rect.x
        # TODO: if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            # TODO: add self.velocity to self.rect.x
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.velocity -= self.rect.x
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.velocity += self.rect.x
    def fire(self):
        """Fire a bullet"""
        # Restrict the number of bullet on screen at a time
        # TODO: if len(self.bullet_group) <2:
            # TODO: call self.shoot_sound.play() with no arguments
            # TODO: call PlayerBullet() with self.rect.centerx, self.rect.top, and self.bullet_group as the arguments
        if len(self.bullet_group) <2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
    def reset(self):
        """Reset the players position"""
        # TODO: assign WINDOW_WIDTH // 2 to self.rect.centerx
        self.rect.centerx = WINDOW_WIDTH // 2


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        # TODO: assign pygame.image.load("alien.png") to self.image
        self.image = pygame.image.load("alien_ship.png")
        # TODO: assign self.image.get_rect() to self.rect
        self.rect = self.image.get_rect()
        # TODO: assign (x, y) to self.rect.topleft
        self.rect.topleft = (x, y)

        # TODO: assign x to self.starting_x
        self.starting_x = x
        # TODO: assign y to self.starting_y
        self.starting_y = y

        # TODO: assign 1 to self.direction
        self.direction = 1
        # TODO: assign velocity to self.velocity
        self.velocity = velocity
        # TODO: assign bullet_group to self.bullet_group
        self.bullet_group = bullet_group

        # TODO: assign pygame.mixer.Sound("alien_fire.wav") to self.shoot_sound
        self.shoot_sound = pygame.mixer.Sound("alien_fire.wav")

    def update(self):
        """Update the alien"""
        # TODO: add self.direction * self.velocity to self.rect.x
        self.rect.x = self.direction * self.velocity

        #Randomly fire a bullet
        # TODO: if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            #TODO: call self.shoot.sound.play() with no arguments
            self.shoot.sound.play()
            #TODO: call self.fire() with no arguments
            self.fire()

    def fire(self):
        """Fire a bullet"""
        # TODO: call AlienBullet() with self.rect.centerx, self.rect.bottom, self.bullet_group as the arguments
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        """Reset the alien position"""
        # TODO: assign (self.starting_x, self.starting_y) to self.rect.topleft
        self.rect.topleft = (self.starting_x, self.starting_y)
        # TODO: assign 1 to self.direction
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        # TODO: assign pygame.image.load("green_laser.png") to self.image
        self.image = pygame.image.load("green_laser.png")
        # TODO: assign self.image.get_rect() to self.rect
        self.rect = self.image.get_rect()
        # TODO: assign x to self.rect.centerx
        self.rect.centerx = x
        # TODO: assign y to self.rect.centery
        self.rect.centery = y

        # TODO: assign 10 to self.velocity
        self.velocity = 10
        # TODO: call bullet_group.add() passing in self as the only argument
        bullet_group.add()

    def update(self):
        """Update the bullet"""
        # TODO: subtract self.velocity from self.rect.y
        self.rect.y - self.velocity
        #If the bullet is off the screen, kill it
        # TODO: if self.rect.bottom < 0:
        if self.rect.bottom < 0:
            # TODO: call self.kill()
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        # TODO: assign pygame.image.load("red_laser.png") to self.image
        # TODO: assign self.image.get_rect() to self.image
        # TODO: assign x to self.rect.centerx
        # TODO: assign y to self.rect.centery

        # TODO: assign 10 to self.velocity
        # TODO: call bullet_group.add() passing in self
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.starting_x = x
        self.starting_y = y
        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group
        self.shoot_sound.pygame.mixer.Sound("alien_fire.wav")
    def update(self):
        """Update the bullet"""
        # TODO: add self.velocity to self.rect.y
        self.rect.y += self.velocity
        #If the bullet is off the screen, kill it
        # TODO: if self.rect.top > WINDOW_HEIGHT:
        if self.rect.top > WINDOW_HEIGHT:
            # TODO: call self.kill()
            self.kill()




#Create bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()
#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)

#Create an alien group.  Will add Alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()
#Create a Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
# TODO: call the my_game.start_new_round() function with no arguments.
my_game.start_new_round()

#The main game loop
running = True
while running:
    # TODO: not really a todo here just a note to WATCH YOUR INDENTING.
    # TODO: for event in pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check to see if the user wants to quit
        # TODO: if event.type == pygame.QUIT
        if event.type == pygame.QUIT:
            running = False
            # TODO: assign False to running
        #The player wants to fire
        # TODO: if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            # TODO: if event.key == pygame.K_SPACE:
         if event.key == pygame.K_SPACE:
            my_player.fire()
                # TODO: call my_player.fire() function with no arguments.


    #Fill the display
    # TODO: call display_surface.fill() function and pass in (0, 0, 0) for the argument.
    display_surface.fill((0, 0, 0))

    #Update and display all sprite groups
    # TODO: call my_player_group.update() with no arguments.
    my_player_group.update()
    # TODO: call my_player_group.draw() passing in display_surface as its argument
    my_player_group.draw(display_surface)
    # TODO: repeat the last 2 todo's with my_alien_group instead of my_player_group
    my_alien_group.update()
    my_alien_group.draw(display_surface)
    # TODO: repeat the last 2 todo's with my_player_bullet_group
    my_player_bullet_group.draw(display_surface)
    my_player_bullet_group.update()
    # TODO: repeat the last 2 todo's with my_alien_bullet_group
    my_alien_bullet_group.draw(display_surface)
    my_alien_bullet_group.update()
    #Update and draw Game object
    # TODO: call my_game.update() with no arguments
    my_game.update()
    # TODO: call my_game.draw() with no arguments
    my_game.draw()
    #Update the display and tick clock
    # TODO: call pygame.display.update() with no arguments
    pygame.display.update()
    # TODO: call clock.tick() with FPS as its only argument
    clock.tick(FPS)

#End the game
pygame.quit()