from setuptools import setup, find_packages

setup(
    name="MyLogger",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # Example: 'requests',
    ],
    entry_points={
        "console_scripts": [
            "my_logger = my_logger:custom_logger",  # Replace 'your_module' and 'main' with your actual module and entry point
        ],
    },
    package_data={"my_logger": ["log_config/*.json", "log_config/*.yaml"]},
    include_package_data=True,
    author="Bart van Woesik",
    author_email="bartwoesik1@gmail.com",
    description="Custom Logger that can be used in private projects for consistency",
    url="https://github.com/BartvanWoesik/MyLogger",
)
