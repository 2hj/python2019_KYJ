import pygame as pg
from random import *
from settings import *
from dialoglist import *

# 플레이어. NPC. 빌딩
# ==> 스프라이트 구현. 스프라이트 충돌 구현. 부드러운 움직임 구현.
# rect: 스프라이트 담는 사각 영역 

## 게임 텍스트 ##
pg.font.init()
dialogfont = pg.font.Font(font_file, 30)
answerfont = pg.font.Font(font_file, 18)
# font = pg.font.SysFont('arial', 30)
# name = font.render('교수님', True, WHITE)
# name_rect = name.get_rect()
# name_rect.center = name_pos

talk = dialogfont.render(level1['q']['q1'], True, WHITE)
talk_rect = talk.get_rect()
talk_rect.left, talk_rect.top = talk_pos


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
        self.rect.left -= 2
    if key_event[pg.K_RIGHT]:
        self.rect.left += 2
    if key_event[pg.K_UP]:
        self.rect.top -= 2
    if key_event[pg.K_DOWN]:
        self.rect.top += 2
    
  # 충돌했을 때 더는 그쪽 방향으로 이동 못하게 하기  
  def stop(self):
    pass

# display.flip()이랑 display.update()의 차이가 뭐지..?

##---- npc ----##
class Npc(pg.sprite.Sprite):
  def __init__(self, img, pos, size, name):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect()
    self.rect.left, self.rect.top = pos

    self.name = dialogfont.render('교수님', True, WHITE)
    self.name_rect = self.name.get_rect()
    self.name_rect.center = name_pos
    
    self.level = 0
  def npctalk(self, level):
    pass

##---- 말풍선 ----##
class WordBubble(pg.sprite.Sprite):
  def __init__(self, img, size):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect()
    self.pos = [0, 0]
    self.rect.left, self.rect.top = self.pos
    
##---- 대화박스 ----##
class DialogBox(pg.sprite.Sprite):
  def __init__(self, img, pos, size):
    pg.sprite.Sprite.__init__(self)
    self.img = pg.transform.scale(pg.image.load(img), size)
    self.rect = self.img.get_rect()
    self.rect.left, self.rect.top = pos

  def dialog(self):
    pass

##---- 대답 선택목록 ----##
class Answer(pg.sprite.Sprite):
  def __init__(self, pos, loop_box):
    pg.sprite.Sprite.__init__(self)
    self.answer_bg = pg.transform.scale(pg.image.load(answer_bg_file), answer_bg_size)
    self.answer_box = []
    self.answer_txt = []
    # 대답 선택지 수 만큼 대답박스 이미지 생성
    boxpos = [16, 22]
    for i in range(loop_box):
      self.answer_box.append( pg.transform.scale(pg.image.load(answer_box_file), answer_box_size) )
      self.answer_txt.append( answerfont.render(level1['a']['a1'][i], True, WHITE) )
      textrect = self.answer_txt[i].get_rect(center = self.answer_box[i].get_rect().center)
      self.answer_box[i].blit(self.answer_txt[i], textrect)
      self.boxrect = self.answer_box[i].get_rect()
      self.boxrect.left, self.boxrect.top = boxpos
      self.answer_bg.blit(self.answer_box[i], self.boxrect)
      boxpos[1] += 60
    
    self.answer_rect = self.answer_bg.get_rect(center=pos)

    

"""
하나의 Answer 스프라이트객체 : 질문 하나에 대한 대답 목록
-> 질문마다 Answer객체를 따로 만드는게 좋을까? => 객체 생성 시 answer box를 몇개 생성시킬지 loop box 변수가 전해지므로 편함
-> 아니면 Answer객체는 고정해두고 db에서 대답만 땡겨와서 answer box에 적용시킬까?

- Answer객체를 따로 만들면, 대답 선택에 따른 시나리오를 이어나가기에 쉬울까?
- 두번째 방법을 쓰면 
self.answer_box[n] =

"""