#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, subject):
        self.knowledge.append(subject)