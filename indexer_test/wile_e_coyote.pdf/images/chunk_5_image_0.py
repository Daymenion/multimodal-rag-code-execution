
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Revenues ($)": [500000, 450000, 470000, 480000, 490000, 500000, 470000, 460000, 450000, 440000, 430000, 420000],
    "Profits ($)": [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
    "Costs ($)": [400000, 350000, 370000, 380000, 390000, 400000, 370000, 360000, 350000, 340000, 330000, 320000]
}

df_year_2024_forecast_123456 = pd.DataFrame(data)
