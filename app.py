import os
import sys

# Ensure the current directory is in the path so 'app' module can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.ui import main

if __name__ == "__main__":
    main()
