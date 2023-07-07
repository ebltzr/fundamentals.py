# practice file main for modules
import modules

# give an alias/nickname to shorten module name to imported module
import modules as mod

# import functions/classes at top of file -- no longer need to call module modules.py
from modules import hello,bye

# import all -- no reccomended to use in large programs or many modules as you can run into a naming conflict
from modules import *

# python has prewritten modules
help('modules') # run code 

# name of module . name of function -- will call the hello() function found in module modules.py\
modules.hello()
    # Hey
modules.bye()
    # Goodbye

# use alias/nickname to call function
mod.hello()
    # Hey
mod.bye()
    # Goodbye

# import classes/functions already an don't need to call module
hello()
    # Hey
bye()
    # Goodbye