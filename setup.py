
from setuptools import find_packages, setup

# Discover packages inside the existing directories
tab_ddpm_packages: list[str] = find_packages(include=['tab_ddpm*'])
scripts_packages: list[str] = find_packages(where='scripts')
lib_packages: list[str] = find_packages(where='lib')

packages: list[str] = (
    tab_ddpm_packages
    + ['tab_ddpm.scripts']
    + ['tab_ddpm.scripts.' + p for p in scripts_packages]
    + ['tab_ddpm.lib']
    + ['tab_ddpm.lib.' + p for p in lib_packages]
)

setup(
    name='tab-ddpm',
    version='1.0',
    description='[ICML 2023] The official implementation of TabDDPM',
    author='yandex-research',
    author_email='yandex-research@yandex.com',
    license='MIT',
    project_urls={
        'Paper': 'https://arxiv.org/abs/2209.15421',
        'Code': 'https://github.com/yandex-research/tab-ddpm'
    },
    packages=packages,
    package_dir={
        'tab_ddpm': 'tab_ddpm',
        'tab_ddpm.scripts': 'scripts',
        'tab_ddpm.lib': 'lib',
    },
)
