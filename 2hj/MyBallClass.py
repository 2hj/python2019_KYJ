import pygame as pg
import sys
from random import *

# 스프라이트 : 특성=> 스프라이트 이미지(image), 스프라이트 담는 사각영역(rect)

class MyBallClass(pg.sprite.Sprite):
  def __init__(self, img, pos, speed):
    pg.sprite.Sprite.__init__(self) # 초기화
    # self.img = pg.image.load(img) # 이미지불러오기
    self.img = pg.transform.scale(pg.image.load(img), (80,80))
    self.rect = self.img.get_rect() # 이미지 경계
    # Surface.get_rect()
    # image.load()는 Surface객체 리턴
    # transform.scale()도 Surface객체 리턴
    self.rect.left, self.rect.top = pos # 공의 초기 위치
    self.speed = speed
 
  # 스프라이트를 움직임 (업데이트 되는 거니까 rect 다시 정의)
  def move(self):
    self.rect = self.rect.move(self.speed)
    if self.rect.left < 0 or self.rect.right > width:
      self.speed[0] = -self.speed[0]

    if self.rect.top < 0 or self.rect.bottom > height:
      self.speed[1] = -self.speed[1]

##---- 충돌 감지 (collision detection) ----##
def animate(group):
  screen.fill([0,0,0])

  for ball in group:
    ball.move()

  for ball in group:
    group.remove(ball) # 스프라이트 그룹에서 해당 스프라이트를 제거 (스프라이트를 화면에서 지워버림..? => ball들은 이미 group에 소속되어 있으므로)
    # 그럼 sprite.spritecollide(sprite, spriteGroup, dokill) 은 해당 스프라이트그룹의 그룹원이 아닌 스프라이트랑만 비교할수있는 함수인가?
    if pg.sprite.spritecollide(ball, group, False):
      ball.speed[0] = -ball.speed[0]
      ball.speed[1] = -ball.speed[1]

    group.add(ball)
    # screen.blit(ball.img, ball.rect)
    # ball.move()
    # screen.blit(pg.transform.scale(ball.img, (80,80)), ball.rect)
    screen.blit(ball.img, ball.rect)
    # ball.move() 뒤에 screen.blit()이 와야 하는 이유:
    # 

  pg.display.flip()
  pg.time.delay(20)

size = width, height = 640, 480
screen = pg.display.set_mode(size)
# screen.fill([255,255,255])

# 공 여러개 생성
img_file = 'mon.png'
group = pg.sprite.Group()
# balls = []  # 여러 개의 공을 담는 리스트
for row in range(0, 3):
  for col in range(0, 3):
    pos = [col * 180 + 10, row * 180 + 10]
    speed = [choice([-2, 2]), choice([-2, 2])]
    ball = MyBallClass(img_file, pos, speed)
    # balls.append(ball) # 생성한 볼을 balls에 담기
    group.add(ball)

# 공을 화면에 블릿
# for ball in balls:
#   screen.blit(pg.transform.scale(ball.img, (80, 80)), ball.rect)

# pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
  # screen.fill([0,0,0])
  # rect.move()는 결국 객체 자체가 다른 좌표로 이동하는게 아니고, 그려진 건 그냥 그대로 두고 그냥 계속 그린다는 뜻이네
  # 그래서 fill()을 안해주면 이동하는 좌표마다 그려져서 이미지를 드래그한 것처럼 보이게 됨.

  # pg.time.delay(20)
  # for ball in balls:
  #   ball.move()
  #   # screen.blit(pg.transform.scale(ball.img, (80, 80)), ball.rect)
  #   screen.blit(ball.img, ball.rect)
  # pg.display.flip()
  animate(group)
pg.quit()


