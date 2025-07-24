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

    '''
    ゲーム内の動き
    '''
    while True:
        screen.fill((0, 0, 0))  # 画面を塗りつぶし((R, G, B))
        pygame.display.update()  # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
