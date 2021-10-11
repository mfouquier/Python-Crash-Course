#All the different import calls
import sandwiches

sandwiches.sandwich_order('white', 'ham', 'pickles')

from sandwiches import sandwich_order

sandwich_order('rye', 'beef', 'onion', 'kraut')

from sandwiches import sandwich_order as so 

so('french', 'tuna', 'olive')

import sandwiches as sw 

sw.sandwich_order('moldy', 'sour', 'cabbage')

from sandwiches import *

sandwiches.sandwich_order('white', 'lamb', 'curry')