@echo off
echo ============================================================
echo Downloading List
echo ============================================================
python download_list.py
pause
cls
echo ============================================================
echo Converting to AdAway 
echo ============================================================
python adaway_conversion.py
pause
cls
