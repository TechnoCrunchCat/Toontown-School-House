@echo off

taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict) Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict1) Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict2) Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict3) Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict4) Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (NewDistrict5) Server"

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict1.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict2.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict3.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict4.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_newdistrict5.bat

