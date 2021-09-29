import numpy as np
import pandas as pd
from gspread_pandas import Spread


#creates an example dataframe
df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

# Open (if exist) or creates a worksheet with strg='name','url', or 'id'
spread = Spread('Test_gspread',create_spread=True)
# This will ask to authenticate if you haven't done so before

#Paste dataframe to Sheet1
spread.df_to_sheet(df, index=False, sheet='Sheet1', start='A1', replace=True)

#Change individual entry
spread.update_cells('A1', 'A1', ['Test de celda'])
