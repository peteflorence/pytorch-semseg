# This script reads all of the files in ./train
# and resizes all .png files to be 480 x 360
#
###  Input:  .png files in ./images
###  Output: creates .png files 480 x 360 in ./resized_images

###  Warning: don't have `images` be a part of the name of your path except the last directory, or rework the pathing! 

import os
from PIL import Image

def cropImage(filename_full_path, output_full_path):
  # adjust width and height to your needs
  width = 480
  height = 320
  
  try: 
    im_out = Image.open(output_full_path)
    if (im_out.size[0] == 480 and im_out.size[1] == 320):
          print "output already 480 x 320"
          return
  except(KeyboardInterrupt):
      quit()
  except:
    print "resizing..."

  print filename_full_path
  print output_full_path

  try:
      im_in = Image.open(filename_full_path)
      if (im_in.size[0] == 480 and im_in.size[1] == 320):
          print "input already 480 x 320"
          return
      im_out = im_in.crop((0,0,width, height))    # best down-sizing filter
      print "in try loop to crop"
      im_out.save(output_full_path)
      print im_in.size, " --> ", im_out.size
  except(KeyboardInterrupt):
      quit()
  except:
      print "FAILED resizing"
      #os.system("mv " + filename_full_path + " " + filename_full_path + "failed_resize")

def resizeDirectory(dir_name):
  cwd = os.getcwd()
  path_to_dir = cwd + "/" + dir_name
  for root, dirs, files in os.walk(path_to_dir):
      for filename in sorted(files):
          filename_full_path = os.path.join(root, filename)
          if filename_full_path.endswith(".png"):
              print "found .png match: " + filename_full_path
              output_full_path = filename_full_path.replace("trainannot", "resized_trainannot")
              cropImage(filename_full_path, output_full_path)

os.system("mkdir resized_trainannot")
resizeDirectory("trainannot")