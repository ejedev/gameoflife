import pygame
import random


def live_neighbours(position: list, cells: dict) -> int:
    posx = position[0]
    posy = position[1]
    alive = 0
    tocheck = [
        (posx - 10, posy),
        (posx + 10, posy),
        (posx, posy - 10),
        (posx - 10, posy - 10),
        (posx + 10, posy - 10),
        (posx, posy + 10),
        (posx - 10, posy + 10),
        (posx + 10, posy + 10),
    ]
    for cell in tocheck:
        try:
            if cells[cell] is True:
                alive += 1
        except:
            pass
    return alive


def populate(cells: dict) -> dict:
    for y in range(0, 101):
        for x in range(0, 101):
            if random.choice(range(1, 5)) == 1:
                cells[(x * 10, y * 10)] = True
            else:
                cells[(x * 10, y * 10)] = False
    return cells


def generation(cells: dict) -> dict:
    generation = {}
    for y in range(0, 101):
        for x in range(0, 101):
            posx = x * 10
            posy = y * 10
            is_alive = cells[(posx, posy)]
            neighours = live_neighbours([posx, posy], cells)
            if is_alive and neighours in [2, 3]:
                generation[(posx, posy)] = True
            elif not is_alive and neighours == 3:
                generation[(posx, posy)] = True
            else:
                generation[(posx, posy)] = False
    return generation


def main():
    pygame.init()
    gps = 1
    counter = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1000, 1000])
    cells = {}
    cells = populate(cells)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    counter = 0
                    cells = cells = populate(cells)
                if event.key == pygame.K_PERIOD:
                    gps += 1
                if event.key == pygame.K_COMMA:
                    gps -= 1
                    if gps == 0:
                        gps = 1
        screen.fill(pygame.Color(255, 255, 255, 255))
        for x in cells:
            if cells[x] is True:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x[0], x[1], 10, 10))
        pygame.display.flip()
        cells = generation(cells)
        clock.tick(gps)
        counter += 1
        pygame.display.set_caption(
            f"Conway's Game of Life - {gps} Generations Per Second - Generation {counter}"
        )
    pygame.quit()


if __name__ == "__main__":
    main()
