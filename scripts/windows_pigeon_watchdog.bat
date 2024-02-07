@echo off
:Start
cd C:\projects\Pigeon\Pigeon\python
python3 Pigeon.py
:: Wait 30 seconds before restarting.
TIMEOUT /T 30
GOTO:Start