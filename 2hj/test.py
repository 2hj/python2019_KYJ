import pygame
import pygame.gfxdraw


pygame.init()

FONT = pygame.font.SysFont('Arial', 20)
FONT_COLOR = pygame.Color('black')

ATOM_IMG = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.gfxdraw.aacircle(ATOM_IMG, 15, 15, 14, (0, 255, 0))
pygame.gfxdraw.filled_circle(ATOM_IMG, 15, 15, 14, (0, 255, 0))


class Atom(pygame.sprite.Sprite):

    def __init__(self, pos, element):
        pygame.sprite.Sprite.__init__(self)
        # We have to make a copy of the image now, because
        # we're modifying it by blitting the text onto it.
        self.image = ATOM_IMG.copy()
        textsurface = FONT.render(element, True, FONT_COLOR)
        # To center the text, set the center of the textrect to
        # the center of the image rect.
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect) 
        self.rect = self.image.get_rect(center=pos)


def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group(
        Atom((150, 200), 'Ne'), Atom((300, 100), 'C'))

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        all_sprites.update()
        screen.fill((40, 50, 60))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()