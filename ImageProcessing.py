class ImageProcessing:
    def ImageNormalization(self, img=[], mode='norm'):
        if mode == 'norm':
            img = (img-np.min(img).astype(np.float32)/(np.max(img)-np.min(img)).astype(np.float32))
        elif mode == 'std':
            img = (img-np.mean(img)) / np.std(img)

        return img
