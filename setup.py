from distutils.core import setup

setup(name='questgen',
      version='2.1.0',
      description='Question generator from any text',
      author='Nayana Hettiarachchi',
      author_email='nayana.hettiarachchi@hiacuity.com',
      packages=['questgen', 'questgen.encoding', 'questgen.mcq'],
      url="https://github.com/hiacuity/questgen",
      install_requires=[
          'numpy==1.19.5',
          'transformers==4.11.3',
          'flashtext==2.7',
          'nltk==3.6.3',
          'pandas==1.3.3',
          'pytorch_lightning==1.4.9',
          'sense2vec==2.0.0',
          'similarity==0.0.1',
          'spacy==3.1.3',
          'torch==1.9.1'
      ],
      package_data={'questgen': ['questgen.py', 'mcq.py', 'train_gpu.py', 'encoding.py']}
      )
