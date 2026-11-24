from setuptools import find_packages, setup

setup(name='tab-ddpm',
      version='1.0',
      description='[ICML 2023] The official implementation of the paper "TabDDPM: Modelling Tabular Data with Diffusion Models"',
      author='yandex-research',
      author_email='yandex-research@yandex.com',
      license='MIT (c) 2022 Akim Kotelnikov',
      project_urls={
        'Paper': 'https://arxiv.org/abs/2209.15421',
        'Code': 'https://github.com/yandex-research/tab-ddpm'
      },
      packages=find_packages(include=['tab_ddpm*', 'scripts*', 'lib*']),
      package_dir={"tab_ddpm": "tab_ddpm","scripts": "scripts"},
      uploader='Michael-Brukson'
     )