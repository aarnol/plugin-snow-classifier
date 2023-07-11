import numpy as np
from waggle.plugin import Plugin
from waggle.data.vision import Camera

import torch
from torchvision import transforms
import argparse

#basically ripped from the surface water classifier at https://github.com/waggle-sensor/plugin-surfacewater
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', action = 'store', 
                        dest='model', default='model.pth', 
                        help='path to model')
    parser.add_argument('-stream', dest='stream',
                action='store', default="bottom",
                help='ID or name of a stream, e.g. sample')
    parser.add_argument(
        '-debug', dest='debug',
        action='store_true', default=False,
        help='Debug flag')
    parser.add_argument(
        '-continuous', dest='continuous',
        action='store_true', default=False,
        help='Continuous run flag')
    return parser.parse_args()





def run(model, sample, plugin):
    image =sample.data
    timestamp = sample.timestamp
    transformation = transforms.Compose([transforms.ToPILImage(),
                                         transforms.Resize((224,224)),
                                         transforms.ToTensor()])
    image = transformation(image)
    image = image.to(args.device).unsqueeze(0)
    pred = model(image)
    result = torch.argmax(pred).item()
    if result == 0:
        print('no snow')
    elif result == 1:
        print('snow')
    plugin.publish('env.binary.snow', result, timestamp=timestamp)






if __name__ == "__main__":
    args = get_args()
    if torch.cuda.is_available():
        args.device = 'cuda'
    else:
        args.device = 'cpu'
    model = torch.load(args.model, map_location=args.device)
    model.eval()
    while True:
        with Plugin() as plugin, Camera() as camera:
            sample = camera.snapshot()
            run(model,sample, plugin)
            if not args.continuous:
                break
    exit(0)
            
