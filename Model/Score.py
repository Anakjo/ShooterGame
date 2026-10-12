import pygame
from datetime import datetime
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import KEYDOWN, K_RETURN
from Model.const import SCORE_POS, MENU_OPTION
from Model.DBProxy import DBProxy

#Manages player score input, database persistence, and the Top 10 leaderboard display
class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/score.png').convert()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        #Play score screen background music and initialize database connection
        pygame.mixer_music.load('./Asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')

        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(70, 'You Win!!!', (240, 248, 255), SCORE_POS['Title'])

            #Configure score and prompt message based on game mode (Singleplayer or Multiplayer)
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player 1 enter your name (4 characteres):'
                self.score_text(30, text, (240, 248, 255), SCORE_POS['EnterName'])
            if game_mode == MENU_OPTION[1]:
                score = player_score[0] + player_score[1]
                text = 'Enter your team name (4 characteres):'
                self.score_text(30, text, (240, 248, 255), SCORE_POS['EnterName'])

            #Handle user input events for name entry
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                        
                    exit()
                elif event.type == KEYDOWN:
                    #Save record to database when Enter is pressed and name length equals 4 characters
                    if event.key == K_RETURN and len (name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': datetime.now().strftime('%d/%m/%Y %H:%M')})
                        db_proxy.close()
                        return
                    #Handle backspace to delete characters from the input name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    #Append alphanumeric characters up to the 4-character limit
                    elif len(name) < 4 and event.unicode.isalnum():
                        name += event.unicode.upper()

            self.score_text(30, name, (240, 248, 255), SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        #Load audio and fetch top 10 records from the database
        pygame.mixer_music.load('./Asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        db_proxy = DBProxy('DBScore')
        top10 = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(70, 'TOP 10 SCORE', (240, 248, 255), SCORE_POS['Title'])

            #Render each entry in the Top 10 leaderboard list
            for idx, dados in enumerate(top10):
                score_str = f'{idx + 1}.  {dados[1]}     {dados[2]}     {dados[3]}'
                self.score_text(25, score_str, (240, 248, 255), SCORE_POS[idx])

            #Handle exit events to return to the previous menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                        return

            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            #Helper method to render centered score text and UI elements
            text_font: Font = pygame.font.SysFont(name="Agency FB", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)