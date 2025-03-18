:: batch script to set up virtual environment on windows 

@echo off

:: if a 'venv' folder does not already exist creates one
IF NOT EXIST "venv" (
	echo Creating virtual environment...
	python -m venv venv
) ELSE (
	echo Virtual environment already exists.
)

:: Activate the virtual environment
echo Activating the virtual environment...
call venv\Scripts\activate.bat

:: Install the dependencies from requirements.txt
echo Installing dependencies...
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete! Virtual environment is ready.