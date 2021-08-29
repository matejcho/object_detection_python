import tensorflow as tf
import coremltools as ct

if __name__ == '__main__':
    h5model = tf.keras.models.load_model(filepath='./data/models/yolov4-tiny.h5')
    classes = ct.ClassifierConfig('./data/classes/cocolabels.txt')
    model = ct.convert(h5model, inputs=[ct.ImageType(1/255.0)], classifier_config=classes)
    model.save('./yolov4-tiny.mlmodel')
