import numpy as np


class AvgMeter(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def adjust_learning_rate(optimizer, start_lr, epoch):
    """Sets the learning rate to the initial LR decayed by 10 every x epochs"""

    decay_iters = 40
    lr = start_lr * (0.1 ** (epoch // decay_iters))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr
