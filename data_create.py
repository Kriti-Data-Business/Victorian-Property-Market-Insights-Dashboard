import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Create 250 property records across Victoria
regions = ['Melbourne CBD', 'Eastern Suburbs', 'Western Suburbs', 'Northern Suburbs', 
           'Southern Suburbs', 'Outer East', 'Outer West']
property_types = ['Apartment', 'House', 'Townhouse', 'Land']
sentiments = ['bullish', 'optimistic', 'positive', 'stable', 'cautious', 'bearish']

# Generate data
n_records = 250
df = pd.DataFrame({
    'property_id': range(1, n_records + 1),
    'region': np.random.choice(regions, n_records),
    'property_type': np.random.choice(property_types, n_records),
    'price_aud': np.random.normal(700000, 300000, n_records).astype(int),
    'price_per_sqm': np.random.normal(8000, 2000, n_records).astype(int),
    'date_recorded': [datetime.now() - timedelta(days=int(x)) for x in np.random.randint(0, 90, n_records)],
    'stakeholder_sentiment': np.random.choice(sentiments, n_records),
    'market_activity': np.random.choice(['High', 'Medium', 'Low'], n_records),
    'investment_readiness': np.random.choice(['Ready', 'Developing', 'Emerging'], n_records),
    'development_potential': np.random.choice(['High', 'Medium', 'Low'], n_records),
})

# Data validation
df['price_valid'] = (df['price_aud'] > 0) & (df['price_aud'] < 3000000)

# Save
df.to_csv('victorian_property_data.csv', index=False)
print(f"Dataset created: {len(df)} records")
