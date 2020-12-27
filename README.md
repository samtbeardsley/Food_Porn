# From Jello Molds to Surf & Turf: Culinary Deep Learning

In the modern digital world images are everywhere and play a central role in our communications. We share experiences and ideas with all from friends and family to customers and followers in image format. Within this communication, one of the things we photograph most is food. The hashtags #food, #foodporn, #instafood, #yummy and #foodie are 5 of the top 100 hashtags on Instagram and, combined, have been used over 1 billion times. In spite of all of this sharing and the rise of the food blog, we also see cookbooks continue to be a medium in which we explore food. Undeniably, food is a necessary part of our everyday lives, but something that also ties us culturally and emotionally. 

As such, we have a long history of photographing our food with the first example attributed to scientist Joseph Nicéphore Niépce in 1832. In the 70s the term “food porn” was used as “unhealthy for human consumption,” but was later reframed to comment on the aesthetically appealing qualities of the food. On the topic of pornography Justice Potter Stewart said “I know it when I see it,” but whether you’re sharing your newest kitchen creation with your followers, or are a professional chef enticing bookstore browsers to pick up your newest cookbook (yes, we’re absolutely judging this book by its cover), we ask: What is it that makes our photos worthy of being #foodporn?

Image datasets of food exist, such as Food-101, however there are none, that I’m aware of, that attempt to capture the quality of the food. Fortunately, Reddit has the longstanding FoodPorn (FP) and ShittyFoodPorn (SFP) communities whose images I used in a classification task with convolutional neural networks. Professional food photographers and content creators such as bloggers or influencers can use the developed model to quickly judge the quality of their food photos.

Exploring the data set and model performance shows that good food images have color contrast, a point of focus that is front and center, and proper lighting and the misclassifications validate that the model has learned this. However, we see that it can still be tricked when using proper photography techniques on monstrous food creations.

The final developed model utilized the ResNet50 architecture pre-trained on the ImageNet data set. It achieved a 93.70% test accuracy after training the final convolution layer and conducting a second fine-tuning training on the top 150 layers (out of 214).


## Table Of Contents

### Documentation
 * [Project Report](https://github.com/samtbeardsley/Food_Porn/blob/master/Project%20Report.pdf)
 * [Presentation](https://github.com/samtbeardsley/Food_Porn/blob/master/Presentation.pdf)

### Notebooks
* [Data Wrangling](https://github.com/samtbeardsley/Food_Porn/blob/master/01_Data_Wrangling.ipynb)
* [Exploratory Data Analysis](https://github.com/samtbeardsley/Food_Porn/blob/master/02_Exploratory_Data_Analysis_Colab.ipynb)
* [Modeling](https://github.com/samtbeardsley/Food_Porn/blob/master/03_Modeling.ipynb)

