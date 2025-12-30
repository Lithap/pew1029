#!/usr/bin/env python3
"""
Tests for pew CLI tool
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
import pew


class TestPewStop(unittest.TestCase):
    """Test cases for pew stop command"""
    
    def test_stop_now(self):
        """Test 'pew stop now' command"""
        with patch('sys.argv', ['pew', 'stop', 'now']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = pew.main()
                self.assertEqual(result, 0)
                self.assertIn('Stopping pew now', mock_stdout.getvalue())
    
    def test_stop_without_args(self):
        """Test 'pew stop' command without arguments"""
        with patch('sys.argv', ['pew', 'stop']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = pew.main()
                self.assertEqual(result, 0)
                self.assertIn('Stopping pew', mock_stdout.getvalue())
    
    def test_no_command(self):
        """Test pew without any command shows help"""
        with patch('sys.argv', ['pew']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = pew.main()
                self.assertEqual(result, 1)
                self.assertIn('usage:', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
