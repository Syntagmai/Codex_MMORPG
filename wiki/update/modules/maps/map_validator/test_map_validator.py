#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo map_validator

Módulo: map_validator
Descrição: Validação de integridade de mapas
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from map_validator import MapvalidatorModule

class TestMapvalidatorModule(unittest.TestCase):
    """Testes para o módulo map_validator"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = MapvalidatorModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "map_validator")
        self.assertEqual(self.module.description, "Validação de integridade de mapas")
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
