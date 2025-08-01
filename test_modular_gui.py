#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste da Versão Modularizada do BMAD System GUI
Script para verificar se a modularização está funcionando corretamente

Autor: Sistema BMAD - Codex MMORPG
Versão: 1.0.0
Data: 2025-08-01
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os
from pathlib import Path

def test_imports():
    """Testa se todas as importações necessárias estão disponíveis"""
    print("🧪 Testando importações...")
    
    try:
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox
        print("✅ Tkinter: OK")
    except ImportError as e:
        print(f"❌ Tkinter: {e}")
        return False
    
    try:
        from pathlib import Path
        print("✅ Pathlib: OK")
    except ImportError as e:
        print(f"❌ Pathlib: {e}")
        return False
    
    try:
        import json
        print("✅ JSON: OK")
    except ImportError as e:
        print(f"❌ JSON: {e}")
        return False
    
    try:
        import threading
        print("✅ Threading: OK")
    except ImportError as e:
        print(f"❌ Threading: {e}")
        return False
    
    try:
        import subprocess
        print("✅ Subprocess: OK")
    except ImportError as e:
        print(f"❌ Subprocess: {e}")
        return False
    
    return True

def test_modules():
    """Testa se todos os módulos estão disponíveis"""
    print("\n📦 Testando módulos...")
    
    required_modules = [
        "gui_modules/__init__.py",
        "gui_modules/gui_styles.py",
        "gui_modules/gui_interface.py",
        "gui_modules/gui_agents.py",
        "gui_modules/gui_config.py",
        "gui_modules/gui_tests.py",
        "gui_modules/gui_utils.py"
    ]
    
    missing_modules = []
    
    for module in required_modules:
        if Path(module).exists():
            print(f"✅ {module}: OK")
        else:
            print(f"❌ {module}: FALTANDO")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n⚠️ Módulos faltando: {len(missing_modules)}")
        return False
    
    print("✅ Todos os módulos encontrados!")
    return True

def test_module_imports():
    """Testa se os módulos podem ser importados"""
    print("\n🔧 Testando importação dos módulos...")
    
    try:
        from gui_modules.gui_styles import GUIStyles
        print("✅ GUIStyles: OK")
    except ImportError as e:
        print(f"❌ GUIStyles: {e}")
        return False
    
    try:
        from gui_modules.gui_interface import GUIInterface
        print("✅ GUIInterface: OK")
    except ImportError as e:
        print(f"❌ GUIInterface: {e}")
        return False
    
    try:
        from gui_modules.gui_agents import GUIAgents
        print("✅ GUIAgents: OK")
    except ImportError as e:
        print(f"❌ GUIAgents: {e}")
        return False
    
    try:
        from gui_modules.gui_config import GUIConfig
        print("✅ GUIConfig: OK")
    except ImportError as e:
        print(f"❌ GUIConfig: {e}")
        return False
    
    try:
        from gui_modules.gui_tests import GUITests
        print("✅ GUITests: OK")
    except ImportError as e:
        print(f"❌ GUITests: {e}")
        return False
    
    try:
        from gui_modules.gui_utils import GUIUtils
        print("✅ GUIUtils: OK")
    except ImportError as e:
        print(f"❌ GUIUtils: {e}")
        return False
    
    return True

def test_gui_creation():
    """Testa se a GUI pode ser criada"""
    print("\n🎨 Testando criação da GUI...")
    
    try:
        # Criar janela de teste
        root = tk.Tk()
        root.withdraw()  # Esconder janela
        
        # Testar criação de estilos
        from gui_modules.gui_styles import GUIStyles
        styles = GUIStyles()
        print("✅ Estilos criados: OK")
        
        # Testar criação de interface
        from gui_modules.gui_interface import GUIInterface
        interface = GUIInterface(root, Path.cwd())
        print("✅ Interface criada: OK")
        
        # Testar criação de agentes
        from gui_modules.gui_agents import GUIAgents
        agents = GUIAgents(root, Path.cwd())
        print("✅ Agentes criados: OK")
        
        # Testar criação de configurações
        from gui_modules.gui_config import GUIConfig
        config = GUIConfig(root, Path.cwd())
        print("✅ Configurações criadas: OK")
        
        # Testar criação de testes
        from gui_modules.gui_tests import GUITests
        tests = GUITests(root, Path.cwd())
        print("✅ Testes criados: OK")
        
        # Testar criação de utilitários
        from gui_modules.gui_utils import GUIUtils
        utils = GUIUtils()
        print("✅ Utilitários criados: OK")
        
        root.destroy()
        print("✅ GUI testada com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar GUI: {e}")
        return False

def test_paths():
    """Testa se os caminhos necessários existem"""
    print("\n📁 Testando caminhos...")
    
    base_path = Path.cwd()
    print(f"📁 Caminho base: {base_path}")
    
    # Verificar pastas importantes
    important_paths = [
        "wiki",
        "wiki/bmad",
        "wiki/log",
        "wiki/config"
    ]
    
    for path in important_paths:
        full_path = base_path / path
        if full_path.exists():
            print(f"✅ {path}: OK")
        else:
            print(f"⚠️ {path}: Não encontrado (será criado automaticamente)")
    
    return True

def show_test_results():
    """Mostra resultados dos testes em uma janela"""
    root = tk.Tk()
    root.title("🧪 Resultados dos Testes - BMAD System GUI Modular")
    root.geometry("600x400")
    root.configure(bg='#2b2b2b')
    
    # Frame principal
    main_frame = tk.Frame(root, bg='#2b2b2b')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Título
    title_label = tk.Label(
        main_frame,
        text="🧪 Resultados dos Testes",
        font=("Arial", 16, "bold"),
        bg='#2b2b2b',
        fg='#ffffff'
    )
    title_label.pack(pady=(0, 20))
    
    # Área de resultados
    results_text = tk.Text(
        main_frame,
        height=15,
        bg='#1e1e1e',
        fg='#ffffff',
        font=("Consolas", 10)
    )
    results_text.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
    
    # Capturar saída dos testes
    import io
    import sys
    
    # Redirecionar stdout para capturar resultados
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    # Executar testes
    all_tests_passed = True
    
    if not test_imports():
        all_tests_passed = False
    
    if not test_modules():
        all_tests_passed = False
    
    if not test_module_imports():
        all_tests_passed = False
    
    if not test_gui_creation():
        all_tests_passed = False
    
    if not test_paths():
        all_tests_passed = False
    
    # Capturar resultados
    test_output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    # Exibir resultados
    results_text.insert(tk.END, test_output)
    
    # Status final
    if all_tests_passed:
        status_text = "🎉 TODOS OS TESTES PASSARAM!"
        status_color = "#4CAF50"
    else:
        status_text = "❌ ALGUNS TESTES FALHARAM"
        status_color = "#f44336"
    
    status_label = tk.Label(
        main_frame,
        text=status_text,
        font=("Arial", 14, "bold"),
        bg='#2b2b2b',
        fg=status_color
    )
    status_label.pack(pady=(0, 10))
    
    # Botões
    buttons_frame = tk.Frame(main_frame, bg='#2b2b2b')
    buttons_frame.pack(fill=tk.X)
    
    if all_tests_passed:
        launch_btn = tk.Button(
            buttons_frame,
            text="🚀 Lançar Sistema Modular",
            command=lambda: launch_modular_system(root),
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            height=2
        )
        launch_btn.pack(side=tk.LEFT, padx=(0, 10))
    
    close_btn = tk.Button(
        buttons_frame,
        text="❌ Fechar",
        command=root.destroy,
        bg='#f44336',
        fg='white',
        font=("Arial", 12, "bold"),
        height=2
    )
    close_btn.pack(side=tk.RIGHT)
    
    root.mainloop()

def launch_modular_system(test_window):
    """Lança o sistema modular"""
    test_window.destroy()
    
    try:
        # Importar e executar sistema modular
        from bmad_system_gui_modular import main
        main()
    except Exception as e:
        messagebox.showerror(
            "Erro",
            f"Erro ao lançar sistema modular:\n{e}"
        )

def main():
    """Função principal"""
    print("🧪 Iniciando testes da versão modularizada...")
    print("=" * 50)
    
    # Executar testes
    all_tests_passed = True
    
    if not test_imports():
        all_tests_passed = False
    
    if not test_modules():
        all_tests_passed = False
    
    if not test_module_imports():
        all_tests_passed = False
    
    if not test_gui_creation():
        all_tests_passed = False
    
    if not test_paths():
        all_tests_passed = False
    
    # Resultado final
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Sistema modular pronto para uso")
        
        # Perguntar se quer mostrar interface gráfica
        response = input("\nDeseja mostrar os resultados em interface gráfica? (s/n): ")
        if response.lower() in ['s', 'sim', 'y', 'yes']:
            show_test_results()
        else:
            print("✅ Testes concluídos com sucesso!")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        print("⚠️ Verifique os erros acima antes de usar o sistema")

if __name__ == "__main__":
    main() 