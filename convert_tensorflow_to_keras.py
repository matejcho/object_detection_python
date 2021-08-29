import tensorflow as tf

if __name__ == '__main__':
    pb_model_dir = './checkpoints/yolov4-416'
    h5_model = './data/models/yolov4.h5'
    model = tf.keras.models.load_model(pb_model_dir)
    print(model.summary())

    # Saving the Model in H5 Format
    tf.keras.models.save_model(model, h5_model)

    # Loading the H5 Saved Model
    loaded_model_from_h5 = tf.keras.models.load_model(h5_model)
    print(loaded_model_from_h5.summary())
