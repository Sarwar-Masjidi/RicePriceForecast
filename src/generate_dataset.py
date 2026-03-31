import pandas as pd
import numpy as np

# Parameters
np.random.seed(42)
dates = pd.date_range(start='2015-01-01', end='2025-12-31', freq='W')  # weekly data
price = 200 + 2*np.arange(len(dates))/len(dates)  # upward trend
price += 10*np.sin(np.linspace(0, 20*np.pi, len(dates)))  # seasonality
price += np.random.normal(0, 5, len(dates))  # noise

# Introduce random spikes (simulate conflict or shocks)
num_spikes = 15
spike_indices = np.random.choice(len(dates), num_spikes, replace=False)
price[spike_indices] += np.random.uniform(20, 50, num_spikes)

# Create DataFrame
df = pd.DataFrame({'date': dates, 'price': price})

# Save CSV
df.to_csv('../data/raw/rice_prices.csv', index=False)
print("Dataset generated successfully at: data/raw/rice_prices.csv")