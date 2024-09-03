import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person['email'].duplicated()][['email']].drop_duplicates()


data = [[1, 'a@b.com'], [2, 'a@b.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

print(duplicate_emails(person))
