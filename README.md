# Market-Study-NLP
## What is it?
It's an api that:
1. Scrape TrustPilot about a specified domain and a locality (like a city).
2. Use CamemBERT(a French NLP model) on the data gathered to predict notes and harmonise values.
3. Return a JSon containg the most used Pos/Neg/Old/Recent words, the number of reviews and companies.

## How to use it?
1. Run `bash dl.sh` to download the weight file for the model.
2. Launch the local server by executing api.py.
3. Go to the local adress http://127.0.0.1:5000/locality%3D*CITY_NAME*/domain%3D*DOMAIN*/ and replace the city name and domain by the informations you want.

## More info !
https://colab.research.google.com/drive/1aoKpy_6uSBQXSfWpMiyoF3XZFn0yc3xY?usp=sharing
This is the link of the colab where we trained our model.
