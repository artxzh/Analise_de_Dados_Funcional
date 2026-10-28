from validations import *
from files_creator import *
from filters import *

df = load_csv("dados")
print(filter_number_above(df, 2000, "valor_total"))
