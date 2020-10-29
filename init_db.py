from sqlalchemy import MetaData, create_engine

from polls.db import choice, question
from polls.settings import config

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(
        question.insert(),
        [
            {
                "question_text": "The Ultimate Answer?",
                "pub_date": "2015-12-15 17:17:49.629+02",
            }
        ],
    )

    conn.execute(
        choice.insert(),
        [
            {
                "choice_text": "Serenity now! Serenity now! SERENITY NOW!",
                "votes": 3,
                "question_id": 1,
            },
            {"choice_text": "Inner peace.", "votes": 2, "question_id": 1},
            {"choice_text": "42", "votes": 42, "question_id": 1},
            {"choice_text": "Randomness", "votes": 9, "question_id": 1},
        ],
    )

    conn.close()


if __name__ == "__main__":
    db_url = DSN.format(**config["postgres"])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
