import unittest
import os
from utils.config import TEST_PATH

Suite=unittest.TestLoader().discover(start_dir=os.path.join(TEST_PATH,"case"),
                                     pattern='test*.py',
                                     top_level_dir=None)
print(Suite)
