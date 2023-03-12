#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Unittest for base model module.
"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""
    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
