import sys
import warnings

# Not impressed psycopg2
if not sys.warnoptions:
    warnings.filterwarnings("ignore", module='psycopg2')
