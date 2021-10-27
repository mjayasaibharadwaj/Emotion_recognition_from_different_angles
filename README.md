# Emotion_recognition_from_different_angles


### Project Description
1. This project uses OpenCV's Face Detection Neural Network to detect faces in images.
2. Uses DeIT(Data efficient Image transformer) model to train the KDEF,JAFFE and CK+ datasets to effectively recognize emotion from different angles.


### File Description

1. "Emotion_recognition_different_angles.ipynb" jupyter notebook file contains the whole implementation of training the model
2. "KDEF_preprocessing.py" - preprocessing of the KDEF dataset
3. "jaffe_proprocessing.py" - preprocesing of the Jaffe dataset
4. "face_detection.py" - Extract faces from the set of images

### Dependencies required

1. Timm(Pytorch image models) Library --- pip install timm
2. Pytorch version 1.8.1 --- pip install torch==1.8.1
