import pygame 
pygame.init()
white =(255, 250, 0)


clock = pygame.time.Clock()



display_surface = pygame.display.set_mode((500, 500))


pygame.display.set_caption('Image')

image = pygame.image.load('ggg.jpg')


DEFAULT_IMAGE_SIZE = (200, 200)


image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_POSITION = (0, 0)


while True:
    display_surface.fill(white)
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        pygame.quit()

    pygame.display.flip()
    clock.tick(60)
