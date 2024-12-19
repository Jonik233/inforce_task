import os
import string
import random
import pandas as pd
from faker import Faker

def generate_data(num_samples:int=1500, corruption_rate:float=0.2) -> pd.DataFrame:
    f = Faker()
    
    # Generating diverse emails (with different domains and validity)
    domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    emails = [f.email(domain=random.choice(domains)) for _ in range(num_samples)]
    
    # Artificial corruption
    n_invalid = int(corruption_rate * num_samples)
    strs_to_remove = ["@", "com", ".", ".com"]
    
    for _ in range(n_invalid):
        indx = random.randint(0, num_samples)
        char = random.choice(string.ascii_letters + string.digits)
        str_to_remove = random.choice(strs_to_remove)
        emails[indx] = emails[indx].replace(str_to_remove, char)
    
    
    # Generating the rest of data
    ids = [i for i in range(1, num_samples + 1)]
    names = [f.name() for _ in range(num_samples)]
    dates = [f.date_time() for _ in range(num_samples)]
    
    data = {
            "user_id": ids,
            "name": names,
            "email": emails,
            "signup_date": dates
        }
    
    return pd.DataFrame(data)



if __name__ == '__main__':
    
    data_path = os.environ['DATA_PATH']

    try:
        num_samples_input = input("Enter the number of samples to generate (default 1500): ")
        corruption_rate_input = input("Enter the corruption rate (default 0.2, between 0 and 1): ")

        num_samples = int(num_samples_input) if num_samples_input.strip() else 1500
        corruption_rate = float(corruption_rate_input) if corruption_rate_input.strip() else 0.2

        if not (0 <= corruption_rate <= 1):
            raise ValueError("Corruption rate must be between 0 and 1.")

        df = generate_data(num_samples=num_samples, corruption_rate=corruption_rate)
        
        if not data_path:
            print("DATA_PATH is not set in the .env file. Saving to 'output.csv' instead.")
            data_path = "output.csv"

        df.to_csv(data_path, index=False)
        print(f"Data successfully saved to {data_path}")

    except ValueError as e:
        print(f"Error: {e}")