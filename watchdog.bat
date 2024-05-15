@echo off
title Partner+ Tracker Watchdog

:top
    echo [%DATE:~4% %TIME%] Starting partner points tracker.
    start /w python app.py
    echo [%DATE:~4% %TIME%] Reopening partner points tracker.
    timeout /t 5 /nobreak >nul
    goto top