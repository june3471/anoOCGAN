import tensorflow as tf
import numpy as np


class AnoOCGAN:
    
    def __init__(self, noise_size):
        self.inputs_size = noise_size
        
    def generative(self):
        inputs = tf.keras.Input(self.noise_size, name="g_input")
        dense1 = tf.keras.layers.Dense(14,kernel_initializer=tf.keras.initializers.RandomNormal(stddev=0.02))(inputs)
        lrelu1 = tf.keras.layers.LeakyReLU(0.2)(dense1)
        dense2 = tf.keras.layers.Dense(7, kernel_initializer=tf.keras.initializers.)

    def descriminative(self):
        
    #def gan_modeling(self):
        
    #def gan_train(self):
        
    
        
    
    