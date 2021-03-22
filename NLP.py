from transformers import CamembertForSequenceClassification, CamembertTokenizer, pipeline
import torch
import numpy
import time


TOKENIZER = CamembertTokenizer.from_pretrained('camembert-base', do_lower_case=True)
model = CamembertForSequenceClassification.from_pretrained('camembert-base', num_labels=6)
model.load_state_dict(torch.load("sentiment.pt", map_location=torch.device('cpu')))

pipe = pipeline("sentiment-analysis", tokenizer=TOKENIZER, model=model)


def predict(dataset):
    start_time = time.time()
    df = dataset
    df['pred'] = numpy.NaN

    for index, row in df.iterrows():
        text = row['review']
        note = pipe(text)[0]["label"][-1]
        df.at[index, 'pred'] = note
    df["pred"] = df["pred"].astype(int)

    print(f"Scraping exec time = {time.time() - start_time}")
    return df
