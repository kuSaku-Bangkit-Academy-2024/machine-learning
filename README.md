# KusaKu 

The project includes datasets and trained models for advisory and categorization purposes. Below is a detailed description of the contents of this repository.

## Folder Structure

This repository consists of several main folders, each of which has a specific function:

- **Folder `advice`**: Contains datasets used for advisory purposes. These datasets can be used to train or test models that provide advice based on the given inputs.

- **Folder `categorize`**: Contains two trained models used to categorize the data. Each model is placed in a separate folder:

## Usage

### Dataset (`advice`)

The dataset used to provide advice is located within folder `advice`. This dataset can be used to train models or evaluate existing models so that they can provide monthly recommendations based on existing data analysis

### Model Kategorisasi (`categorize`)

In a folder `categorize`, You will find two sub-folders each containing one trained model. Each model can be used as needed to categorize data based on criteria determined during training.

### Large Files

Due to GitHub's limitations in storing large files (above 100MB), some dataset and model files are stored in Google Drive. You can download these files via the following link:

- categorize/distilbert/results/best_models/variables/variables.data-00000-of-00001 (771,073 KB) -> https://drive.google.com/file/d/10x20CcHm4zRoLvLn68a2YNB6xqU9o4YN/view?usp=sharing
- categorize/distilbert/saved_model/tf_model.h5 (257,115 KB) -> https://drive.google.com/file/d/1sligIkOxYl8W7dBz3zNJP6_sB4Bfk2dZ/view?usp=sharing
- categorize/Roberta/results/best_models/variables/variables.data-00000-of-00001 (1,461,016 KB) -> https://drive.google.com/file/d/1fZj-r_FNp9uJx2sxlyz6YFF8eh3_gg6T/view?usp=sharing
- categorize/RoBERTa/saved_model/tf_model.h5 (487,207 KB) -> https://drive.google.com/file/d/1QoK4U7lQjVt40xMxysL3ld2xZevwKqf2/view?usp=sharing
- categorize/Model Comparison/distilbert/results/best_models/variables/variables.data-00000-of-00001 (771,073 KB)  -> https://drive.google.com/file/d/1lM2bsyro4BCGcZ9zz-2NLbYDTEwNKanN/view?usp=sharing
- categorize/Model Comparison/distilbert/saved_model/tf_model.h5 (257,115 KB) -> https://drive.google.com/file/d/1cF5ojsIu3uwYfX_dvCXIycYBZLwnfzlG/view?usp=sharing
- categorize/Model Comparison/Roberta/results/best_models/variables/variables.data-00000-of-00001 (1,461,016 KB) -> https://drive.google.com/file/d/1D2-MOHzPRERuKYIE6XNyp05oxC4wW5Pw/view?usp=sharing
- categorize/Model Comparison/RoBERTa/saved_model/tf_model.h5 (487,207 KB) ->  https://drive.google.com/file/d/1D_1KBZXGB0ib9pfrwXu394djEtNwXF6b/view?usp=sharing 

Here is the Google Drive that contain all machine learning file -> https://drive.google.com/drive/folders/1FcvG3yji6gH33OTQm1lgKfavPWCVoF-o?usp=sharing

After downloading these files, you can place them in the appropriate folder within your local repository.
