import pygame
import sys


def main():
    '''
    ゲームの設定：
        画面の大きさ、タイトル、必要なファイルの用意など
    '''
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((1000, 700))  # 画面の大きさ（x方向, ｙ方向）
    pygame.display.set_caption('歴戦乱舞')  # 画面上部に表示するタイトルを設定
    x_axis = 0
    x_axis_speed = 0.1
    y_axis = 0
    y_axis_speed = 0.1
    '''
    ゲーム内の動き
    '''
    while True:
        screen.fill((0, 0, 0))  # 画面を塗りつぶし((R, G, B))

        x_axis += x_axis_speed
        y_axis += y_axis_speed
        pygame.draw.rect(screen, (255, 0, 0), (x_axis, y_axis, 100, 100))


        pygame.display.update()  # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
