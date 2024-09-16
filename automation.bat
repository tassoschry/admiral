@echo off
echo ============================================================
echo Downloading List
echo ============================================================
python download_list.py
cls
echo ============================================================
echo Converting to AdAway 
echo ============================================================
python adaway_conversion.py
cls
echo ============================================================
echo Uploading to GitHub 
echo ============================================================
echo on
git add . 
git commit -m "update lists"
git push origin main
pause
