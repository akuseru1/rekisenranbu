import pygame
import sys


def main():
    '''
    ゲームの設定：
        画面の大きさ、タイトル、必要なファイルの用意など
    '''
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((1000, 700))  # 画面の大きさ（x方向, ｙ方向）
    pygame.display.set_caption('練習')  # 画面上部に表示するタイトルを設定

    '''
    ゲーム内の動き
    '''
    while True:
        screen.fill((0, 0, 0))  # 画面を塗りつぶし((R, G, B))
        enemy = pygame.image.load("img/宮本武蔵.png")
        
        enemy_resize = pygame.transform.scale(enemy, (enemy.get_width() / 3.5, enemy.get_height() / 3.5))
        screen.blit(enemy_resize, (1000 / 2 - enemy_resize.get_width() / 2, 700 / 2 - 300))

        font = pygame.font.Font("./font/DragonQuestFC.ttf", 30)
        message = font.render("ムサシがあらわれた!", True, (255, 255, 255))
        attack_text = font.render("こうげき", True, (255, 255, 255))
        bloc_text = font.render("まもる", True, (255, 255, 255))
        magic_text = font.render("まほう", True, (255, 255, 255))
        screen.blit(message, (1000 / 2 - 80, 480))
        screen.blit(attack_text, (1000 / 2 - 80, 500))
        screen.blit(bloc_text, (1000 / 2 - 80, 520))
        screen.blit(magic_text, (1000 / 2 - 80, 540))

        pygame.display.update()  # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("前")
                if event.key == pygame.K_d:
                    print("右")
                if event.key == pygame.K_s:
                    print("後")
                if event.key == pygame.K_a:
                    print("左")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print("クリックするんなや!!")
                # print(event.dict)
                # print(event.dict["pos"][1])
                pos_x = event.dict["pos"][0]
                pos_y = event.dict["pos"][1]
                if pos_x > 500 and pos_x < 1000:
                    if pos_y > 350 and pos_y < 700:
                        print("正解")
                    else:
                        print("不正解")
                else:
                    print("不正解")


if __name__ == '__main__':
    main()
