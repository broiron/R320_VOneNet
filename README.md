# FGSM_MNIST

We're trying to make model better which is robust against to adversarial images, especially made by FGSM.
Yann LeCun's MNIST datasets are used.

We're inspired by this [tutorial](https://www.pyimagesearch.com/2021/03/08/defending-against-adversarial-image-attacks-with-keras-and-tensorflow/).

## 2023 ICIIT conference paper

Paper "A Study on the Optimization of the CNNs for Adversarial Attacks" got accepted to ICIIT 2023 conference wrote by Hyeongcheol Park, Jongweon Kim.

Conference proceeding is not now available(still publishing) but you can see the original paper down below.

<object data="https://github.com/broiron/R320_VOneNet/blob/main/report/ICIIT_A_Study_on_the_Optimization_of_the_CNNs_for_Adversarial_Attacks.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/broiron/R320_VOneNet/blob/main/report/ICIIT_A_Study_on_the_Optimization_of_the_CNNs_for_Adversarial_Attacks.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/broiron/R320_VOneNet/blob/main/report/ICIIT_A_Study_on_the_Optimization_of_the_CNNs_for_Adversarial_Attacks.pdf">Download PDF</a>.</p>
    </embed>
</object>


## Fine-tune modeling
1. train model with original MNIST datasets (learning rate == 0.001)<br>
2. get adversarial images of MNIST from trained model<br>
3. fine-tune model with adversarial images. learning rate is 0.0001 (it may be modified)<br>
4. validate with validation set 100 epochs each models<br>
5. results saved as a plot <br>

A function named<br>
  generate_image_adversarial(args) is just interpretation of tensorflow code to pytorch code<br>

## Results

red line  : accuracy of original MNIST imagess of fine-tuned model<br>
blue line : accuracy of adversarial MNIST images of fine-tuned model <br>

1. Result of none VOneNet finetuned<br>
<br><img src="https://github.com/comeeasy/VOneNet_FGSM_MNIST/blob/main/report/None-vonenet-finetuned.png" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br>

2. Result of VOneNet finetuned<br>
<br><img src="https://github.com/comeeasy/VOneNet_FGSM_MNIST/blob/main/report/vonenet-finetuned.png" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br>

### fine-tunning harms None-VOneNet models's prediction of original data. 
### But VOnetNet models are robust to fine-tunning 

## Requirements

- python 3.8+
- pytorch 0.4.1+
- numpy
- tqdm

## License

MIT License

## trained model

| Name     | Description                                                              |
| -------- | ------------------------------------------------------------------------ |
| 1-layer-linear-classifier | really simple model                                     |
| 3-layer-linear-classifier | add two layer to 1-layer simple model                   |
| Convnet                   | simple convolutional model                              |



## Report
<object data="https://github.com/comeeasy/FGSM_MNIST/blob/main/VOneNet-FGSM-report.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/comeeasy/FGSM_MNIST/blob/main/VOneNet-FGSM-report.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/comeeasy/VOneNet_FGSM_MNIST/blob/main/report/VOneNet-FGSM-report.pdf">Download PDF</a>.</p>
    </embed>
</object>

## Longer Motivation

1. VOneNet maybe boosts performance. So we're considering how apply this model to
[VOneNet](https://github.com/dicarlolab/vonenet)
