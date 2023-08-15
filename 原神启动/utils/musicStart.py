import pygame #要安装环境


def musicStart(audio_file, start_position):  # 播放音频
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(start=start_position)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()
