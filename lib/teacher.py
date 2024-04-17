#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        
        random_index = random.randint(0, len(self.knowledge) - 1)
        random_knowledge = self.knowledge[random_index]
        return random_knowledge   