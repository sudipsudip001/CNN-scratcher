import matplotlib.pyplot as plt
import numpy as np
import os
import pickle

#train images
train_images = np.array([])
train_labels = []

#test images
test_images = np.array([])
test_labels = []

the_path = ".\\dataset\\cifar-10-batches-py\\"

class Preprocess:
    def __init__(self):
        pass

    def unpickle(self, file):
        with open(file, 'rb') as fo:
            dict = pickle.load(fo, encoding='bytes')
        return dict

    def unpickle_data(self):
        #for train images
        images = []
        for i in range(1, 6):
            batch = self.unpickle(os.path.join(the_path, f"data_batch_{i}"))
            images.append(batch[b'data'])
            train_labels.append(batch[b'labels'])

        train_images = np.vstack(images).reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

        #for test images
        images = []
        batch = self.unpickle(os.path.join(the_path, f"test_batch"))
        images.append(batch[b'data'])
        test_labels.append(batch[b'labels'])
        test_images = np.vstack(images).reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

        return train_images, test_images
    
def main():
    print("Hello world!")
    preprocess = Preprocess()
    train_images, test_images = preprocess.unpickle_data()
    print("The shape of train images: ", train_images.shape)
    print("The length of train image labels: ", len(train_labels))
    print("The shape of test images: ", test_images.shape)
    print("The length of test image labels: ", len(test_labels))

if __name__ == "__main__":
    main()