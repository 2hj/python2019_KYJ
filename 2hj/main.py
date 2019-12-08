import sys
from sprites import *

"""
<요구사항>
  - 플레이어가 npc와 충돌 => npc머리 위에 말풍선 표시 (o)
  ==> 그 상태에서 스페이스바 누르면 대사 창이 뜸 (o)
  - 플레이어가 npc와 떨어지게 되면 다시 말풍선 사라짐 (o)
  - npc와 관련한 퀘스트가 있으면 npc머리 위에 느낌표 표시 

  - 퀘스트 목록: 퀘스트 하나씩 공개될 때마다 목록에 퀘스트가 보이게 됨. 깨지 못한 퀘스트는 ??? 로 표시되어 있음
  
  ** npc의 질문에 대한 플레이어의 대답 선택 **
  - 백그라운드 이미지 하나 깔기 (대답 갯수 상관없이 크기 고정)
  - 선택대답을 담을 작은 박스이미지 
  - => 하나의 스프라이트 객체로 묶기, 즉 해당 스프라이트 객체는 특정 질문에 대한 대답목록 스프라이트 객체

  ** 게임방식 **
  - 스테이지 (시나리오 만드려니 너무 어렵다~)
  - 목표 : 10 스테이지
  - 대답 잘못하면 게임오버 시키기~
  - 한 스테이지마다 플레이어가 상대하는 npc들을 정해두고 그 npc들과의 대화를 모두 공략해야 한 스테이지를 통과.
    한 스테이지 도중에 게임오버되면 그 스테이지부터 리스타트
  - 엔딩은 어떻게 두지? 마지막 1-2스테이지에 따라 엔딩이 갈리게 할까?
  - 게임오버 스토리를 몇개 둬야함

"""
pg.init()



## 파이게임 화면 생성 ##
screen = pg.display.set_mode(screen_size) 

## 스프라이트 그룹 ##
npc_group = pg.sprite.Group()
dialog_group = pg.sprite.Group()
answer_group = pg.sprite.Group()

## 플레이어 생성 ##
player_file = mon_file
player = Player(player_file, [100, 100], [80, 80], [choice([-10, 10]), choice([-10, 10])]) 

## npc 생성 ##
# 교수
prof_file = prof_file
prof = Npc(prof_file, [200, 200], [80, 80], '교수님')
npc_group.add(prof)

## 말풍선 생성 ##
word_bubble = WordBubble(word_bubble_file, [50, 50])

Clock = pg.time.Clock()

## 충돌 감지 ##
# 플레이어와 npc 충돌 시=> 플레이어가 더 갈 수 없고, npc머리 위에 말풍선 나타남
# 플레이어와 건물 충돌 시=> 플레이어가 더 갈 수 없음
state = False
def collision():
  global state
  screen.fill(WHITE)
  player.move_key()
  
  for npc in npc_group:
    if pg.sprite.spritecollide(player, npc_group, False):
      # 플레이어 움직임 stop하기 어캐함??

      # 플레이어와 npc 충돌 => npc머리 위에 말풍선이 뜨게 함
      word_bubble.pos = [npc.rect.left + 15, npc.rect.top - 50]
      word_bubble.rect.left, word_bubble.rect.top = word_bubble.pos
      screen.blit(word_bubble.img, word_bubble.rect)
      key_event = pg.key.get_pressed()
      if key_event[pg.K_SPACE]:
        state = True
      if key_event[pg.K_ESCAPE]:
        state = False
      
      if state: 
        blit_dialog(npc)
        
      # 그 자리에서 스페이스바 누르면 npc와 대화 창 뜨게 하기

# 메인루프에서 blit 했을 때 스프라이트가 화면 상 계속 존재하는 이유: 프레임이 루프되기 때문
# 스프라이트는 루프되어야 계속 존재하고 있음

def blit_dialog(npc):
  global state
  dialog = DialogBox(dialogbox_file, [35, 400], [132*7, 32*7])
  dialog_group.add(dialog)
  
  dialog.img.blit(npc.name, npc.name_rect)
  dialog.img.blit(talk, talk_rect)
  screen.blit(dialog.img, dialog.rect)
  key_event = pg.key.get_pressed()
  if key_event[pg.K_SPACE]:
    state = True
  if key_event[pg.K_ESCAPE]:
    state = False
  if state: 
    blit_answerbox(npc)

def blit_answerbox(npc):
  global state
  answer = Answer( answer_pos, len(level1['a']['a1']) )
  screen.blit(answer.answer_bg, answer.answer_rect)

  answer_num = -1
  key_event = pg.key.get_pressed()
  if key_event[pg.K_d]:
    answer_num += 1
    state = True

  if key_event[pg.K_s]:
    pass

  if state:  
    pg.transform.scale(answer.answer_box[answer_num], answer_box_bigsize)
    answer.answer_bg.blit(answer.answer_box[answer_num], answer.answer_box[answer_num].get_rect())
    screen.blit(answer.answer_bg, answer.answer_rect)

    

##---- 메인루프 ----##
running = True
while running:
  Clock.tick(60)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
  # screen.fill(WHITE)
  pg.time.delay(20)
  # player.move_self()
  # player.move_key()
  collision() 
  screen.blit(player.img, player.rect)
  screen.blit(prof.img, prof.rect)

  pg.display.update()

pg.quit() # 얘가 왜 메인루프 밖일까 -> running이 False 됐으니까...