"""
움직임 구현하기 : 픽셀의 색을 바꾸어 움직이는 것처럼 보이게 함
백그라운드 맵과 디스플레이(스크린) 맵을 하나 둔다
스크린맵에서 플레이어가 움직일 때 = 근접한 픽셀이 칠해질 때,
스크린맵에 플레이어가 원래 존재하던 자리(움직이기 이전 플레이어)를 삭제한다
=> 삭제하는 법 = 백그라운드맵에서 같은 위치의 픽셀을 가져옴

<blit>
블릿 : 한 이미지에서 다른 이미지로 그래픽을 복사하는 것

"""

import pygame

# screen = [1, 1, 2, 2, 2, 1]
# playerpos = 3
# screen[playerpos] = 8

# playerpos = playerpos-1
# screen[playerpos] = 8

background = [1, 1, 2, 2, 2, 1]
screen = [0]*6
for i in range(6):
  screen[i] = background[i]

playerpos = 3
screen[playerpos] = 8

screen[playerpos] = background[playerpos]
playerpos -= 1
screen[playerpos] = 8

screen[playerpos] = background[playerpos]
playerpos += 2
screen[playerpos] = 8
print(screen)