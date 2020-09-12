import cv2
 
def video2frame(invideofilename, save_path):
    vidcap = cv2.VideoCapture(invideofilename)
    count = 0
    while True:
      success,image = vidcap.read()
      if not success:
          break
      print ('Read a new frame: ', success)
      fname = "video_6_{}.jpg".format("{0:05d}".format(count))
      cv2.imwrite(save_path + fname, image) # save frame as JPEG file
      count += 1
    print("{} images are extracted in {}.". format(count, save_path))


invideofilename="./video_6.mp4"
save="ds/ds_v4/img/"
video2frame(invideofilename,save)