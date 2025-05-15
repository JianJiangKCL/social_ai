the password is SEUAIPL
has audio but it too short so that no use normally sound is truncated.
# README
## Dynamic Facial Expression in-the-Wild (DFEW) Database
* For more information about the dataset, please visit [the project website](https://dfew-dataset.github.io/).
* If your use the dataset in a publication, please cite the paper below:
```
@inproceedings{jiang2020dfew,
  title={DFEW: A Large-Scale Database for Recognizing Dynamic Facial Expressions in the Wild},
  author={Xingxun, Jiang and Yuan, Zong and Wenming, Zheng and Chuangao, Tang and Wanchuang, Xia and Cheng, Lu and Jiateng, Liu},
  booktitle={Proceedings of the 28th ACM International Conference on Multimedia},
  pages={xxxx-xxxx},
  year={2020}
}
```
* Please note that we do not own the copyrights to these clips. Their use is RESTRICTED to non-commercial research and educational purposes.

## Change Log
Version 1.0, released on 10/17/2020

## File Information
### Overview
- Clips (Clip)
  - Original Clips (./CLip/original): Totally 16372 dynamic facial expression video clips. See "CLIP" section below for more information. 
    - data_part_1-2-3.zip :  4800 clips.
    - data_part_4-5-6.zip :  4800 clips. 
    - data_part_7-8-9.zip :  4800 clips.
    - data_part_10-11.zip :  1972 clips.
  - Preprocessed with Time Interpolation Method(TIM) (./Clip/clip_224x224_16f.zip)
  - Preprocessed without Time Interpolation Method(TIM) (./Clip/clip_224x224)
    - clip_224x224_part_1.zip
    - clip_224x224_part_2.zip
    - clip_224x224_part_3.zip
    - clip_224x224_part_4.zip
    - clip_224x224_part_5.zip
    - clip_224x224_part_6.zip
    - clip_224x224_part_7.zip
    - clip_224x224_part_8.zip
    - clip_224x224_part_9.zip
    - clip_224x224_part_10.zip
    - clip_224x224_part_11.zip
- Emotion Labels with data split (EmoLabel_DataSplit): Data split with single-labeled emotion for 5-fold cross-validation mentioned in the paper. 
  - train(single_labeled).zip (./EmoLabel_DataSplit/train(single_labeled).zip):
    - set_1.csv : training data of the fd1 cross-validation
    - set_2.csv : training data of the fd2 cross-validation
    - set_3.csv : training data of the fd3 cross-validation
    - set_4.csv : training data of the fd4 cross-validation
    - set_5.csv : training data of the fd5 cross-validation
  - test(single_labeled).zip  (./EmoLabel_DataSplit/test(single_labeled).zip):
    - set_1.csv : test data of the fd1 cross-validation
    - set_2.csv : test data of the fd2 cross-validation
    - set_3.csv : test data of the fd3 cross-validation
    - set_4.csv : test data of the fd4 cross-validation
    - set_5.csv : test data of the fd5 cross-validation
- Annotations (./Annotation) : 
  - annotation.zip (./Annotation/annotation.zip) : the 7-dimensional expression distribution vector for each video clip

### CLIP
--------------------"./Clip/original"----------------------
Containing 16372 annotated video clip with 7-dimensional emotions distribution vector.

Notes:
1. Clips are named in the format of "XXXXX.mp4"

-----------------"./Clip/clip_224x224"-----------------
Containing 15906 annotated video clip with 7-dimensional emotions distribution vector. These clips are acquired by picking out the useless frames undetected human faces, discarding the clips which useful frames greater than 50% and face normailzation(alignment and affine). Totally 466 face undetected clips are dropped from 16372 clips, here 362 clips belongs to the single labeled DFEW.


-----------------"./Clip/clip_224x224_16f"-----------------
Containing 15906 annotated video clip with 7-dimensional emotions distribution vector. These clips are acquired by picking out the useless frames undetected human faces, discarding the clips which useful frames greater than 50%, face normailzation(alignment and affine) and time interpolation method(TIM). Totally 466 face undetected clips are dropped from 16372 clips, here 362 clips belongs to the single labeled DFEW.

Notes:
1. The y th frame of clip "x.mp4" is named in the format of "x_y.jpg"


### EMOTION_LABELS & Data Split
------------------"./EmoLabel_DataSplit"-------------------
Containing 11697 (drop 362 clips undetected face from totally 12059 single-labled clips) annotated video clip with single-labeled discrete emotion. We used 5 fold cross-validation for evaluation methods performed on these 12059 video clips.
fd1: 9356 clips for training, 2341 clips for test
fd2: 9356 clips for training, 2341 clips for test
fd3: 9357 clips for training, 2340 clips for test
fd4: 9358 clips for training, 2339 clips for test
fd5: 9361 clips for training, 2336 clips for test

Notes:
1: Happy
2: Sad
3: Neutral
4: Angry
5: Surprise
6: Disgust
7: Fear


### Annotations
---------------"./Annotation/annotation.xlsx"---------------

each row: (vote_happy) (vote_sad) (vote_neutral) (vote_angry) (vote_surprise) (vote_disgust) (vote_fear) (clip_name) (annotation)

Notes:
0: Non single-labeled
1: Happy 
2: Sad 
3: Neutral 
4: Angry 
5: Surprise
6: Disgust
7: Fear


## Contact
Please contact Xingxun Jiang (jiangxingxun@seu.edu.cn) for questions about the dataset.












