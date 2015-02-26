from apriori import apriori
import logging

logging.basicConfig(level=logging.INFO)

#Testing Apriori to mine frequent items
minimum_support = 2
apriori(minimum_support)