import sys
from sprites import *

"""
<요구사항>
- 플레이어가 npc와 충돌 => npc머리 위에 말풍선 표시 (o)
==> 그 상태에서 스페이스바 누르면 대사 창이 뜸 (x)
- 플레이어가 npc와 떨어지게 되면 다시 말풍선 사라짐 (o)
- npc와 관련한 퀘스트가 있으면 npc머리 위에 느낌표 표시

- 퀘스트 목록: 퀘스트 하나씩 공개될 때마다 목록에 퀘스트가 보이게 됨. 깨지 못한 퀘스트는 ??? 로 표시되어 있음
- 
"""

## 파이게임 화면 생성 ##
screen = pg.display.set_mode(screen_size) 

## 스프라이트 그룹 ##
npcs = pg.sprite.Group()

## 플레이어 생성 ##
player_file = mon_file
player = Player(player_file, [100, 100], [80, 80], [choice([-10, 10]), choice([-10, 10])]) 

## npc 생성 ##
# 교수
prof_file = prof_file
prof = Npc(prof_file, [200, 200], [80, 80])
npcs.add(prof)

## 말풍선 생성 ##
word_bubble = WordBubble(word_bubble_file, [50, 50])

Clock = pg.time.Clock()

## 충돌 감지 ##
# 플레이어와 npc 충돌 시=> 플레이어가 더 갈 수 없고, npc머리 위에 말풍선 나타남
# 플레이어와 건물 충돌 시=> 플레이어가 더 갈 수 없음
def collision():
  screen.fill(WHITE)
  player.move_key()
  
  for npc in npcs:
    if pg.sprite.spritecollide(player, npcs, False):
      # 플레이어 움직임 stop하기 어캐함??

      # 플레이어와 npc 충돌 => npc머리 위에 말풍선이 뜨게 함
      word_bubble.pos = [npc.rect.left + 15, npc.rect.top - 50]
      word_bubble.rect.left, word_bubble.rect.top = word_bubble.pos
      screen.blit(word_bubble.img, word_bubble.rect)

      # 그 자리에서 스페이스바 누르면 npc와 대화 창 뜨게 하기



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