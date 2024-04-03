from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import pandas as pd

Base = declarative_base()

class Sentiment(Base):
    __tablename__ = 'sentiments'

    sentiment_id = Column(Integer, primary_key=True)
    sentiment_label = Column(String(255))

    def __repr__(self):
        return f"<Sentiment(sentiment_id={self.sentiment_id}, sentiment_label={self.sentiment_label})>"

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    text = Column(String(255))  
    sentiment_id = Column(Integer, ForeignKey('sentiments.sentiment_id'))
    sentiment = relationship("Sentiment", backref="tweets")

    def __repr__(self):
        return f"<Tweet(id={self.id}, text={self.text}, sentiment_id={self.sentiment_id})>"

class DatabaseManager:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.engine = self.create_engine()
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_engine(self):
        db_url = f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
        return create_engine(db_url)

    def create_tables(self):
        Base.metadata.create_all(self.engine)
        print("Tabel telah dibuat.")

    def insert_from_csv(self, csv_file, max_text_length=255):
        data = pd.read_csv(csv_file)

        sentiments = {}

        for _, row in data.iterrows():
            sentiment_label = row['sentiment']

            if sentiment_label not in sentiments:
                sentiment = self.session.query(Sentiment).filter_by(sentiment_label=sentiment_label).first()
                if not sentiment:
                    sentiment = Sentiment(sentiment_label=sentiment_label)
                    self.session.add(sentiment)
                    self.session.commit()
                sentiments[sentiment_label] = sentiment

            tweet = Tweet(text=row['tweets'][:max_text_length], sentiment_id=sentiments[sentiment_label].sentiment_id)
            self.session.add(tweet)

        self.session.commit()
        print("Data berhasil dimasukkan ke dalam database.")

if __name__ == "__main__":
    # Konfigurasi MySQL
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'dzikri123'
    db_name = 'manager'

    # Inisialisasi objek DatabaseManager
    db_manager = DatabaseManager(db_host, db_user, db_password, db_name)

    # Membuat tabel-tabel
    db_manager.create_tables()

    # Insert data dari CSV ke dalam database
    db_manager.insert_from_csv('sentiment_good.csv')
    db_manager.insert_from_csv('sentiment_bad.csv')
    db_manager.insert_from_csv('sentiment_neutral.csv')
