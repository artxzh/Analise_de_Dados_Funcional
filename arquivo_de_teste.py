from validations import *
from files_creator import *

df = load_csv("dados")
string = validate_parameter(df, "categoria")
