import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION

# Inicializa o Pygame
pygame.init()

# Define a resolução desejada para a janela do jogo (1280x720)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Cria a janela no tamanho correto (1280x720) em modo janela redimensionável
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Define o título da janela
pygame.display.set_caption("Meu Jogo - Menu")

# Classe Menu
class Menu:
    def __init__(self, window):
        self.window = window
        self.window_width, self.window_height = self.window.get_size()

        # Carrega e redimensiona a imagem para caber na tela do jogo (1280x720)
        self.surf = pygame.image.load('./assets/Menu.png')
        self.surf = pygame.transform.scale(self.surf, (self.window_width, self.window_height))

        self.rect = self.surf.get_rect(topleft=(0, 0))

        # Carrega a música do menu e toca em loop (-1)
        pygame.mixer.music.load('./assets/Menu.wav')
        pygame.mixer.music.play(-1)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, border_color: tuple,
                  border_width: int):
        """Renderiza texto com borda (contorno preto)."""
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Cria o texto principal (cor do texto vinho)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Criar borda ao redor do texto, desenhando o texto com borda maior (em uma cor clara de vinho)
        if border_width > 0:
            # Desenha a borda (contorno claro) desenhando o texto em várias direções
            for dx in range(-border_width, border_width + 1):
                for dy in range(-border_width, border_width + 1):
                    if dx != 0 or dy != 0:  # Não desenhar a borda no centro do texto
                        border_surf: Surface = text_font.render(text, True, border_color).convert_alpha()
                        border_rect: Rect = border_surf.get_rect(center=text_center_pos)
                        self.window.blit(border_surf, border_rect.move(dx, dy))

        # Desenha o texto principal (cor vinho) sobre a borda
        self.window.blit(text_surf, text_rect)

    def run(self):
        self.window.blit(self.surf, self.rect)

        # Centralizar o título "Vampire Hunter"
        title_y_pos = SCREEN_HEIGHT // 3  # Posição Y centralizada na parte superior da tela
        self.menu_text(80, "Vampire Hunter", (128, 0, 32), (SCREEN_WIDTH // 2, title_y_pos), (255, 255, 255), 3)  # Borda branca

        # Posição das opções do menu (com espaçamento entre elas)
        option_y_pos = title_y_pos + 150  # Espaçamento médio entre o título e as opções do menu
        option_spacing = 50  # Espaçamento entre as opções do menu

        for i, option in enumerate(MENU_OPTION):
            self.menu_text(50, option, (128, 0, 32), (SCREEN_WIDTH // 2, option_y_pos + option_spacing * i), (255, 255, 255), 2)  # Borda branca

        pygame.display.flip()

# Instancia o menu
menu = Menu(window)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se clicar no "X", fecha o jogo
            running = False

    # Executa o menu
    menu.run()

# Sai do Pygame corretamente
pygame.quit()
sys.exit()
