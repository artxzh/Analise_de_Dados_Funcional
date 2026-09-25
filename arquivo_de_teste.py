from validations import *
from files_creator import *

df = load_csv("dados")
if check_parameter(df, "categoria", "Beleza"):
  print("Deu certo")