import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import keyboard
import math

class ParticlePlayer:
    def __init__(self):
        self.x = 5 * np.random.random_sample()
        self.y = 5 * np.random.random_sample()
        self.vx = 0.1
        self.vy = 0.1
        self.angle = np.angle(self.vy/self.vx)


    def move(self):
        vx = self.vx * math.cos(self.angle)
        vy = self.vy * math.sin(self.angle)
        
        if self.x < 0: self.x += self.vx
        if self.x >= 5: self.x -= self.vx
        if self.y < 0: self.y += self.vy
        if self.y >= 5: self.y -= self.vy
        
        if keyboard.is_pressed('up'):
            self.y += self.vy
        if keyboard.is_pressed('down'):
            self.y -= self.vy
        if keyboard.is_pressed('right'):
            self.x += self.vx
        if keyboard.is_pressed('left'):
            self.x -= self.vx
      
       
class ParticleEnemy:
    def __init__(self):
        self.x = 5 * np.random.random_sample()
        self.y = 5 * np.random.random_sample()
        self.vx = np.random.random_sample()/10 
        self.vy = np.random.random_sample()/10
        self.ax = 0
        self.ay = 0

    def move(self):
        if self.x < 0:
            self.x = 0
            self.vx = np.random.random_sample()/10
        if self.x >= 5:
            self.x = 5
            self.vx = np.random.random_sample()/10 * -1  
        if self.y < 0:
            self.y = 0
            self.vy = np.random.random_sample()/10
        if self.y >= 5:
            self.y = 5
            self.vy = np.random.random_sample()/10 * -1  
        self.x += self.vx
        self.y += self.vy
    
    def acceleration(self, p1):
        dist_x = self.x - p1.x
        dist_y = self.y - p1.y
        
        self.ax = 0.01 * dist_x
        self.ay = 0.01 * dist_y
        
        if self.vx < 0.1 or self.vx > -0.1:
            self.vx -= self.ax
        if self.vy < 0.1 or self.vy > -0.1:
            self.vy -= self.ay
        
        

# --- functions ---

######## main ########
def main():
    def animate(frame_number):
        global d  # need it to remove old plot
        # print('frame_number:', frame_number)

        # move all particles
        player.move()
        for particle in enemies:
            particle.acceleration(player)
            particle.move()

        # remove old plot
        #d.set_data([], [])
        d.remove()
        a.remove()


        # create new plot
        d,  = plt.plot(player.x, player.y, 'bo')
        a,  = plt.plot([particle.x for particle in enemies], [particle.y for particle in enemies], 'go')
        
        # pause if collide
        for particle in enemies:
            error_posy = player.y + 0.1
            error_negy = player.y - 0.1
            error_posx = player.x + 0.1
            error_negx = player.x - 0.1
            if (error_negx < particle.x < error_posx) and (error_negy < particle.y < error_posy):
                anim.pause()

    population = 5

    player = ParticlePlayer()
    enemies = [ParticleEnemy() for i in range(population)]

    fig = plt.gcf()
    # draw first plot
    d,  = plt.plot(player.x, player.y, 'bo')
    a,  = plt.plot([particle.x for particle in enemies], [particle.y for particle in enemies], 'go')
    anim = animation.FuncAnimation(fig, animate, frames=200, interval=45, repeat=False)
    plt.show()

if __name__ == '__main__':
    main()