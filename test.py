import pandas
import matplotlib.pyplot as plt
from torchvision.transforms import ToTensor, Lambda
from torchvision import datasets
from torch.utils.data import Dataset
import torch
import sys
import pprint

pprint.pprint(sys.path)

print(torch.cuda.is_available())
print(torch.cuda.get_device_name())

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
