
# Resources
- [Classic Generative Adversarial Networks Paper](https://arxiv.org/abs/1406.2661)
- [(Classic) Generative Adversarial Networks (Paper Explained)](https://www.youtube.com/watch?v=eyxmSmjmNS0&ab_channel=YannicKilcher) 
- [Generative Adversarial Networks (GANs) - Computerphile](https://www.youtube.com/watch?v=Sw9r8CL98N0&ab_channel=Computerphile)
- [Introduction to GANs, NIPS 2016 | Ian Goodfellow, OpenAI](https://www.youtube.com/watch?v=9JpdAg6uMXs&ab_channel=PreserveKnowledge)
- [Generative Adversarial Networks - FUTURISTIC & FUN AI !](https://www.youtube.com/watch?v=O8LAi6ksC80&ab_channel=CodeEmporium)
- [Zebras, Horses & CycleGAN Computerphile](https://www.youtube.com/watch?v=T-lBMrjZ3_0&ab_channel=Computerphile)
- [DC-GAN Explained!](https://www.youtube.com/watch?v=EYrt7fGyA08&ab_channel=HenryAILabs)
- [The applications and implementation of Generative Adversarial Networks - Thomas Derksen](https://www.youtube.com/watch?v=FZIZCRJbAAs&ab_channel=PyGrunnUseraccount)
- [A Friendly Introduction to Generative Adversarial Networks (GANs)](https://www.youtube.com/watch?v=8L11aMN5KY8&ab_channel=Serrano.Academy)
- [An Introduction to Generative Adversarial Networks (GANs)](https://www.youtube.com/watch?v=OXWvrRLzEaU&ab_channel=AladdinPersson)
- [Building our first simple GAN](https://www.youtube.com/watch?v=OljTVUVzPpM&ab_channel=AladdinPersson)
- [DCGAN implementation from scratch](https://www.youtube.com/watch?v=IZtv9s_Wx9I&ab_channel=AladdinPersson)
- [AI generated faces - StyleGAN explained!](https://www.youtube.com/watch?v=4LNO8nLxF4Y&list=PLcp6ZnH4WYlbra9TYePMD1vht6ScbQFB4&ab_channel=AIBites)
- [StyleGAN2 explained - AI generated faces, cars and cats!](https://www.youtube.com/watch?v=841UAo7Ax5w&list=PLcp6ZnH4WYlbra9TYePMD1vht6ScbQFB4&index=2&ab_channel=AIBites)
- [Progressive Growing of GANs for Improved Quality | PGGAN (paper illustrated)](https://www.youtube.com/watch?v=bXffGPbu2Qc&list=PLcp6ZnH4WYlbra9TYePMD1vht6ScbQFB4&index=3&ab_channel=AIBites)
<!-- # Table Of Contents
-  [In a Nutshell](#in-a-nutshell)
-  [In Details](#in-details)
-  [Future Work](#future-work)
-  [Contributing](#contributing)
-  [Acknowledgments](#acknowledgments)

# In a Nutshell   
In a nutshell here's how to use this template, so **for example** assume you want to implement ResNet-18 to train mnist, so you should do the following:
- In `modeling`  folder create a python file named whatever you like, here we named it `example_model.py` . In `modeling/__init__.py` file, you can build a function named `build_model` to call your model

```python
from .example_model import ResNet18

def build_model(cfg):
    model = ResNet18(cfg.MODEL.NUM_CLASSES)
    return model
``` 

   
- In `engine`  folder create a model trainer function and inference function. In trainer function, you need to write the logic of the training process, you can use some third-party library to decrease the repeated stuff.

```python
# trainer
def do_train(cfg, model, train_loader, val_loader, optimizer, scheduler, loss_fn):
 """
 implement the logic of epoch:
 -loop on the number of iterations in the config and call the train step
 -add any summaries you want using the summary
 """
pass

# inference
def inference(cfg, model, val_loader):
"""
implement the logic of the train step
- run the tensorflow session
- return any metrics you need to summarize
 """
pass
```

- In `tools`  folder, you create the `train.py` .  In this file, you need to get the instances of the following objects "Model",  "DataLoader”, “Optimizer”, and config
```python
# create instance of the model you want
model = build_model(cfg)

# create your data generator
train_loader = make_data_loader(cfg, is_train=True)
val_loader = make_data_loader(cfg, is_train=False)

# create your model optimizer
optimizer = make_optimizer(cfg, model)
```

- Pass the all these objects to the function `do_train` , and start your training
```python
# here you train your model
do_train(cfg, model, train_loader, val_loader, optimizer, None, F.cross_entropy)
```

**You will find a template file and a simple example in the model and trainer folder that shows you how to try your first model simply.**


# In Details
```
├──  config
│    └── defaults.py  - here's the default config file.
│
│
├──  configs  
│    └── train_mnist_softmax.yml  - here's the specific config file for specific model or dataset.
│ 
│
├──  data  
│    └── datasets  - here's the datasets folder that is responsible for all data handling.
│    └── transforms  - here's the data preprocess folder that is responsible for all data augmentation.
│    └── build.py  		   - here's the file to make dataloader.
│    └── collate_batch.py   - here's the file that is responsible for merges a list of samples to form a mini-batch.
│
│
├──  engine
│   ├── trainer.py     - this file contains the train loops.
│   └── inference.py   - this file contains the inference process.
│
│
├── layers              - this folder contains any customed layers of your project.
│   └── conv_layer.py
│
│
├── modeling            - this folder contains any model of your project.
│   └── example_model.py
│
│
├── solver             - this folder contains optimizer of your project.
│   └── build.py
│   └── lr_scheduler.py
│   
│ 
├──  tools                - here's the train/test model of your project.
│    └── train_net.py  - here's an example of train model that is responsible for the whole pipeline.
│ 
│ 
└── utils
│    ├── logger.py
│    └── any_other_utils_you_need
│ 
│ 
└── tests					- this foler contains unit test of your project.
     ├── test_data_sampler.py
```


# Future Work

# Contributing
Any kind of enhancement or contribution is welcomed.


# Acknowledgments -->

