import pygame
import random

def main():
	width, height = screen_size = (640, 480)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("PyGame is working! :D")

	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					done = True

		colors = [[139, 69, 19],
					[34, 139, 34]]
		#screen.fill((0, 0, 0))
		x_pos = random.randint(0, width) // 10
		y_pos = random.randint(0, height) // 10
		c_choice = random.choice(colors)
		t = random.uniform(0.5, 1.0)
		new_c = (c_choice[0] * t,
				c_choice[1] * t,
				c_choice[2] * t)

		rekt = (x_pos * 10, y_pos * 10, 10, 10)
		pygame.draw.rect(screen, new_c, rekt)

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()
