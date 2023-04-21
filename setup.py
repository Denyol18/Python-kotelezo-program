from setuptools import setup

setup(
    name='python_kotprog_game',
    version='1.0.0',
    packages=['python_kotelezo_program', 'tests', 'reports'],
    package_data={'': ['.pylintrc', 'README.md', 'resources/sounds/*.wav', 'resources/sounds/*.ogg',
                       'resources/sprites/npc/guard/attack/*.png',
                       'resources/sprites/npc/guard/death/*.png',
                       'resources/sprites/npc/guard/idle/*.png',
                       'resources/sprites/npc/guard/pain/*.png',
                       'resources/sprites/npc/guard/walk/*.png',
                       'resources/sprites/npc/guard/*.png',
                       'resources/sprites/static_sprites/*.png',
                       'resources/sprites/weapon/*.png',
                       'resources/textures/*.png',
                       'resources/textures/*.jpg',
                       'resources/textures/digits/*.png',
                       'flake8_reports/*.json',
                       'pylint_reports/*.json',
                       'test_coverage_reports/*.json']},
    install_requires=['setuptools~=65.5.0', 'pygame~=2.3.0'],
    url='',
    license='',
    author='Denyol',
    author_email='',
    description='Python programozás a gyakorlatban kötelező program - Játék'
)
