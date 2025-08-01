#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o módulo file_mover

Módulo: file_mover
Descrição: Movimentação de arquivos
"""

import unittest
from pathlib import Path
import sys

# Adicionar diretório do módulo ao path
module_path = Path(__file__).parent
sys.path.insert(0, str(module_path))

from file_mover import FilemoverModule

class TestFilemoverModule(unittest.TestCase):
    """Testes para o módulo file_mover"""
    
    def setUp(self):
        """Configuração inicial dos testes"""
        self.module = FilemoverModule()
    
    def test_module_initialization(self):
        """Testa inicialização do módulo"""
        self.assertEqual(self.module.name, "file_mover")
        self.assertEqual(self.module.description, "Movimentação de arquivos")
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
