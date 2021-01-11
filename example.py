import time
from CombineModel_jt import CombineModel
import cv2
import numpy as np
import os
import glob
from tqdm import tqdm
import jittor as jt

jt.flags.use_cuda = 0

try:
    os.system ("bash -c 'mv ./heat/bg.jpg ./heat/.jpg'")
except:
    pass

#models for face/eye1/eye2/nose/mouth
combine_model = CombineModel()

print('start')
# This is where the model reads in test images
fileRoot = './test'
images_path = sorted(glob.glob(fileRoot+r"/*"))

for x,fileName in enumerate(images_path):
    print(fileName)
    mat_img = cv2.imread(fileName)
    mat_img = cv2.resize(mat_img, (512, 512), interpolation=cv2.INTER_CUBIC)
    mat_img = cv2.cvtColor(mat_img, cv2.COLOR_RGB2BGR)
    # Setting gender parameters, 0 means male while 1 means female
    combine_model.sex = 0
    # Setting refinement parameters, can be float between 0 and 1
    # the closer to 0, result will stick more to your sketch
    # the closer to 1, result will be more refined and smoothed
    combine_model.part_weight['eye1'] = 0.5
    combine_model.part_weight['eye2'] = 0.5
    combine_model.part_weight['nose'] = 0.5
    combine_model.part_weight['mouth'] = 0.5
    combine_model.part_weight[''] = 0.5
    combine_model.predict_shadow(mat_img)
    # This is where model writes result images
    cv2.imwrite('./results/' + 'res'+ str(x) +'_male.jpg',cv2.cvtColor(combine_model.generated, cv2.COLOR_BGR2RGB))
    jt.gc()
