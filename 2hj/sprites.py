import pygame as pg
from random import *
from settings import *

# 플레이어. NPC. 빌딩
# ==> 스프라이트 구현. 스프라이트 충돌 구현. 부드러운 움직임 구현.
# rect: 스프라이트 담는 사각 영역 

##---- 플레이어 ----##
class Player(pg.sprite.Sprite):
  def __init__(self, img, pos, size, speed):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect() # Rect 객체 리턴. Rect객체가 스프라이트를 감싸는 공간 정보(위치좌표)를 가지고있는거임
    self.rect.left, self.rect.top = pos
    self.speed = speed

  def move_self(self):
    self.rect = self.rect.move(self.speed)
    if self.rect.left < 0 or self.rect.right > width:
      self.speed[0] = -self.speed[0]
    if self.rect.top < 0 or self.rect.bottom > height:
      self.speed[1] = -self.speed[1]

  # 키보드 조작으로 이동
  def move_key(self):
    key_event = pg.key.get_pressed()
    if key_event[pg.K_LEFT]:
        self.rect.left -= 1
    if key_event[pg.K_RIGHT]:
        self.rect.left += 1
    if key_event[pg.K_UP]:
        self.rect.top -= 1
    if key_event[pg.K_DOWN]:
        self.rect.top += 1
    
  # 충돌했을 때 더는 그쪽 방향으로 이동 못하게 하기  
  def stop(self):
    pass

# display.flip()이랑 display.update()의 차이가 뭐지..?

##---- npc ----##
class Npc(pg.sprite.Sprite):
  def __init__(self, img, pos, size):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect()
    self.rect.left, self.rect.top = pos

##---- 말풍선 ----##
class WordBubble(pg.sprite.Sprite):
  def __init__(self, img, size):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect()
    self.pos = [0, 0]
    self.rect.left, self.rect.top = self.pos
    


    
  