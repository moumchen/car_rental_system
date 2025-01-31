"""
    This file contains some configurations, including:
    db configurations
"""
import importlib
import os

# db configurations
DB_URL = "db/car_rental_system.db"
POOL_SIZE = 100

_language_module = None

def initialize_language(choice):
    global _language_module
    module_name = f"languages.language_{choice}"
    try:
        _language_module = importlib.import_module(module_name)
        print(f"successfully initialize the language package: {choice} ")
    except ImportError:
        print(f"Cannot initialize the langauge package: {choice} ，Please check whether {module_name}.py exists。")
        _language_module = None

def get_language():
    if _language_module:
        return _language_module
    else:
        print("Warning! language model is not initialized.")
        exit(1)


def get_language_choice():
    # get language files in current directory
    files = os.listdir("languages")
    language_files = []
    for file in files:
        if file.startswith("language_") and file.endswith(".py"):
            language_files.append(file)
    if len(language_files) == 0:
        print("No language files found.")
        exit(1)
    # get language choices that current system supports
    language_choices = []
    for file in language_files:
        language_choices.append(file.split("_")[1].split(".")[0])
    # print language choices
    print("Welcome to car rental system! Please choose your language:")
    for i, choice in enumerate(language_choices):
        print(f"{i + 1}. {choice}")
    # get user choice
    while True:
        choice = input("Please input a number: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(language_choices):
                return language_choices[choice - 1]
        print("Invalid input, please input a number.")