from setuptools import setup

setup(
    name='coin-bot',
    version='1.0',
    packages=['coin', 'coin.api', 'coin.candle', 'coin.candle.upbit', "coin.tick", "coin.tick.upbit", 'tests',
              'tests.api'],
    url='https://github.com/wjrmffldrhrl/coin-bot',
    license='',
    author='wjrmffldrhrl',
    author_email='wjrmffldrhrl@gmail.com',
    description='coin trading bot'
)
