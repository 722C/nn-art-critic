import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

import numpy as np
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from skimage import filters

try:
    from scipy.misc import imread
except ImportError:
    from scipy.misc.pilutil import imread

from images.models import Image, BetterThan

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('train_test_split', type=float)
        parser.add_argument('test_split', type=float)

    def handle(self, *args, **options):
        better_thans = BetterThan.objects.all() #.filter(pk__lte=50)

        ds = SupervisedDataSet(204960, 1)
        for better_than in better_thans:
            bt = imread(better_than.better_than.image.file)
            wt = imread(better_than.worse_than.image.file)
            better_than.better_than.image.file.close()
            better_than.worse_than.image.file.close()

            bt = filters.sobel(bt)
            wt = filters.sobel(wt)

            bt_input_array = np.reshape(bt, (bt.shape[0] * bt.shape[1]))
            wt_input_array = np.reshape(wt, (wt.shape[0] * wt.shape[1]))
            input_1 = np.append(bt_input_array, wt_input_array)
            input_2 = np.append(wt_input_array, bt_input_array)
            ds.addSample(np.append(bt_input_array, wt_input_array), [-1])
            ds.addSample(np.append(wt_input_array, bt_input_array), [1])
        
        net = buildNetwork(204960, 2, 1)

        train_ds, test_ds = ds.splitWithProportion(options['train_test_split'])
        _, test_ds = ds.splitWithProportion(options['test_split'])

        trainer = BackpropTrainer(net, ds)

        avgerr = trainer.testOnData(dataset=test_ds)
        print 'untrained avgerr: {0}'.format(avgerr)

        trainer.train()

        avgerr = trainer.testOnData(dataset=test_ds)
        print 'trained avgerr: {0}'.format(avgerr)
