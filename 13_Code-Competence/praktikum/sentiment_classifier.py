import pandas as pd
import os

class SentimentClassifier:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset = None

    def load_data(self):
        try:
            self.dataset = pd.read_csv(self.dataset_path)
            print("Dataset berhasil dimuat.")
        except Exception as e:
            print("Error saat memuat dataset:", str(e))

    def preprocess_dataset(self):
        if self.dataset is not None:
            print("Pemrosesan dataset selesai.")
        else:
            print("Dataset belum dimuat.")

    def classify_sentiment(self):
        if self.dataset is not None:
            self.dataset['sentiment'] = self.dataset['tweets'].apply(lambda x: 'good' if 'great' in x.lower() else 'bad' if 'disappointed' in x.lower() else 'neutral')
            print("Klasifikasi sentimen selesai.")
        else:
            print("Dataset belum dimuat.")

    def save_to_csv(self):
        if self.dataset is not None:
            try:
                for sentiment in ['good', 'bad', 'neutral']:
                    subset = self.dataset[self.dataset['sentiment'] == sentiment]
                    subset.to_csv(os.path.join(os.path.dirname(self.dataset_path), f"sentiment_{sentiment}.csv"), index=False)
                print("Hasil klasifikasi disimpan ke file CSV.")
            except Exception as e:
                print("Error saat menyimpan hasil klasifikasi:", str(e))
        else:
            print("Dataset belum dimuat.")

    def summarize_counts(self):
        if self.dataset is not None:
            counts = self.dataset['sentiment'].value_counts().reset_index()
            counts.columns = ['sentiment', 'count']
            try:
                counts.to_csv(os.path.join(os.path.dirname(self.dataset_path), 'sentiment_counts.csv'), index=False)
                print("Jumlah sentimen disimpan ke sentiment_counts.csv")
            except Exception as e:
                print("Error saat menyimpan jumlah sentimen:", str(e))
        else:
            print("Dataset belum dimuat.")

dataset_path = "data_source/file.csv"
sentiment_classifier = SentimentClassifier(dataset_path)
sentiment_classifier.load_data()
sentiment_classifier.preprocess_dataset()
sentiment_classifier.classify_sentiment()
sentiment_classifier.save_to_csv()
sentiment_classifier.summarize_counts()