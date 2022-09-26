from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyHook(build_py):
    def run(self):
        super().run()
        i = o = "unexceptional.pth"
        base = self.build_lib
        self.copy_file(Path(i), Path(base) / o, preserve_mode=0)


setup(
    name="unexceptional",
    version="0.0.2",
    description="No exceptions",
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    readme='README.md',
    author='Aidan Courtney',
    author_email='aidanfc97@gmail.com',
    url='https://github.com/aidaco/unexceptional',
    license='MIT',
    python_requires=">=3.6",
    packages=["unexceptional"],
    data_files=["unexceptional.pth"],
    install_requires=[],
    tests_require=[],
    cmdclass={
        "build_py": BuildPyHook,
    },
)
