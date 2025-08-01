#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo performance_monitor

Módulo: performance_monitor
Descrição: Monitoramento de performance
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from performance_monitor import PerformancemonitorModule

class TestPerformancemonitorModule(unittest.TestCase):
    """Testes para o módulo performance_monitor"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = PerformancemonitorModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "performance_monitor")
        self.assertEqual(self.module.description, "Monitoramento de performance")
        self.assertEqual(self.module.version, "1.0.0")
    
    def test_module_execution(self):
        """Testa execução do módulo"""
        result = self.module.execute()
        self.assertIsInstance(result, bool)
    
    def test_module_validation(self):
        """Testa validação do módulo"""
        result = self.module.validate()
        self.assertIsInstance(result, bool)

if __name__ == "__main__":
    unittest.main()
