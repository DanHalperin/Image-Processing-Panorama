import os
import sol4
import time
import shlom

def main():

  experiments = ['aqua2.mp4']

  for experiment in experiments:
    exp_no_ext = experiment.split('.')[0]
    os.system('mkdir dump')
    os.system('mkdir dump/%s' % exp_no_ext)
    os.system('ffmpeg -i videos/%s dump/%s/%s%%03d.jpg' % (experiment, exp_no_ext, exp_no_ext))

    s = time.time()
    panorama_generator = sol4.PanoramicVideoGenerator('dump/%s/' % exp_no_ext, exp_no_ext,  2100)
    panorama_generator.align_images(translation_only=False)
    panorama_generator.generate_panoramic_images(120, should_crop=False)
    print(' time for %s: %.1f' % (exp_no_ext, time.time() - s))

    panorama_generator.save_panoramas_to_video()


if __name__ == '__main__':
  main()
