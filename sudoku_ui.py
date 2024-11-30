import pygame

width = 640
height = 700

def draw_game_start(screen):
    # initializes the two fonts that will be used
    title_font = pygame.font.Font(None,100)
    button_font = pygame.font.Font(None,50)
    diff_font = pygame.font.Font(None,70)

    screen.fill("light blue")

    title = title_font.render("Let's Play Sudoku!", 0, "black")
    title_rectangle = title.get_rect(
        center = (width//2, height//2 - 150))
    screen.blit(title, title_rectangle)
    diff_message = diff_font.render("Select Difficulty:", 0, "black")
    diff_rectangle = diff_message.get_rect(
        center = (width//2, height//2))
    screen.blit(diff_message, diff_rectangle)

    easy_text = button_font.render("Easy", 0, (0,0,0))
    med_text = button_font.render("Medium", 0, (0, 0, 0))
    hard_text = button_font.render("Hard", 0, (0, 0, 0))

    easy_surface = pygame.Surface((easy_text.get_size()[0]+20, easy_text.get_size()[1]+20))
    easy_surface.fill("green")
    easy_surface.blit(easy_text, (10,10))

    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1]+20))
    med_surface.fill("yellow")
    med_surface.blit(med_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill("red")
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center = (width//2 - 150,height//2 + 100))

    med_rectangle = med_surface.get_rect(
        center=(width//2, height//2 + 100))

    hard_rectangle = hard_surface.get_rect(
        center=(width // 2 + 150 , height//2 + 100))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    diff = "easy"
                    return
                if med_rectangle.collidepoint(event.pos):
                    diff = "med"
                    return
                if hard_rectangle.collidepoint(event.pos):
                    diff = "hard"
                    return
        pygame.display.update()


def load_game_over(screen):
    screen.fill("light blue")

    lose_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    lose = lose_font.render("You Lost", 0, "black")

    lose_rectangle = lose.get_rect(
        center=(width // 2, height // 2 - 150))
    screen.blit(lose, lose_rectangle)

    restart_text = button_font.render("Restart", 0, (0, 0, 0))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("red")
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(width // 2, height // 2 + 100))
    screen.blit(restart_surface, restart_rectangle)

def load_win(screen):
    screen.fill("light blue")

    win_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    win = win_font.render("You Lost", 0, "black")

    win_rectangle = win.get_rect(
        center=(width // 2, height // 2 - 150))
    screen.blit(win, win_rectangle)

    quit_text = button_font.render("Exit", 0, (0, 0, 0))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill("red")
    quit_surface.blit(quit_text, (10, 10))

    quit_rectangle = quit_surface.get_rect(
        center=(width // 2, height // 2 + 100))
    screen.blit(quit_surface, quit_rectangle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")

    draw_game_start(screen)

    screen.fill("light blue")


if __name__ == "__main__":
    main()
