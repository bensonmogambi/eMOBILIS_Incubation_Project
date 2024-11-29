#echo "from .base import *
from nis import cat

import EOL
from wheel.wheelfile.WheelFile import __init__

#from .production import *

try:
   from .local import *
#except:
  # pass
#" > __init__.py

cat <<EOL > __init__.py
from .base import *

from .production import *

try:
    from .local import *
except ImportError:
    pass
EOL
