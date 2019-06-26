@echo off
title Pirates Online Classic - Client

rem Config Settings
set TRIAL_ENDED=NO
set DEVELOPMENT_SERVER=142.44.142.239
SET TEST_SERVER=142.44.142.240
set PRODUCTION_SERVER=142.44.142.241
set GAME_SHOW_ADDS=YES

set GAME_INGAME_UPGRADE=https://www.piratesclassic.com/
set GAME_INGAME_MOREINFO=https:/www.piratesclassic.com/about
set GAME_INGAME_NAMING=https://www.piratesclassic.com/help/nameapprovals
set GAME_INGAME_MANAGE_ACCT=https://www.piratesclassic.com/account

rem Constants
SET LOCALHOST_SERVER=127.0.0.1

rem Start launch operation and questioning
goto :SETUPENVIRONMENT

:SETUPENVIRONMENT
    rem User variables
    set USERPROFILE=%USERPROFILE%

    rem Set Trial State
    if "%TRIAL_ENDED%" == "YES" (
        set GAME_SHOW_FIRSTADD=1
    )

    title Pirates Online Classic - Client (Trial Ended: %TRIAL_ENDED%)
    goto :CHOOSESERVER

:CHOOSESERVER
    rem Server address input selection
    echo Choose your server (Default: Localhost)
    echo    #1 - Localhost
    echo    #2 - Development
    echo    #3 - Public Test Server
    echo    #4 - Production Server
    echo    #5 - Custom

    set INPUT=-1
    set /P INPUT=Selection: 

    set POC_GAMESERVER=%LOCALHOST_SERVER%
    if %INPUT%==1 (
        set POC_GAMESERVER=%LOCALHOST_SERVER%
    ) else if %INPUT%==2 (
        set POC_GAMESERVER=%DEVELOPMENT_SERVER%
    ) else if %INPUT%==3 (
        set POC_GAMESERVER=%TEST_SERVER%
    ) else if %INPUT%==4 (
        set POC_GAMESERVER=%PRODUCTION_SERVER%
    ) else if %INPUT%==5 (
        set /P POC_GAMESERVER=Game Server IP: 
    ) else (
        echo Invalid Option: %INPUT%; Defaulting to Localhost
        set POC_GAMESERVER=%LOCALHOST_SERVER%
    )
    title Pirates Online Classic - Client (Server: %POC_GAMESERVER%)  (Trial Ended: %TRIAL_ENDED%)

    goto :ENVIRONMENTTYPE

:ENVIRONMENTTYPE

    rem Find default environment
    SET DEFAULT_ENV=LIVE
    if %POC_GAMESERVER%==%LOCALHOST_SERVER% (
        set DEFAULT_ENV=DEV
    ) else if %POC_GAMESERVER%==%DEVELOPMENT_SERVER% (
        set DEFAULT_ENV=DEV
    ) else if %POC_GAMESERVER%==%TEST_SERVER% (
        set DEFAULT_ENV=TEST
    ) else if %POC_GAMESERVER%==%PRODUCTION_SERVER% (
        set DEFAULT_ENV=LIVE
    )

    rem Environment input
    set INPUT=%DEFAULT_ENV%
    set /P INPUT=Environment (LIVE, QA, TEST, DEV) (Default: %INPUT%): 

    for %%G in (LIVE QA TEST DEV) do (
        if "%INPUT%"=="%%G" (
            set GAME_ENVIRONMENT=%INPUT%
            goto :SETENVIRONEMNT
        )
    )
    goto :INVALIDENVIRONMENT

:INVALIDENVIRONMENT
    echo %GAME_ENVIRONMENT% is not a valid environment; Default to DEV
    set GAME_ENVIRONMENT=DEV
    goto :SETENVIRONEMNT

:SETENVIRONEMNT
    echo Client environment set to: %GAME_ENVIRONMENT%
    title Pirates Online Classic - Client (Server: %POC_GAMESERVER%) (Environment: %GAME_ENVIRONMENT%) (Trial Ended: %TRIAL_ENDED%)
    goto :PLAYTOKEN

:PLAYTOKEN
    rem PlayToken input
    set POC_TOKEN=dev
    echo Set Account Token (Default: %POC_TOKEN%)
    set /P POC_TOKEN=Token:
    
    goto :FINDPYTHON

:FINDPYTHON
    rem Choose correct python command to execute the game
    ppythona -h >nul 2>&1 && (
        set PYTHON_CMD=ppythona
    ) || (
        set PYTHON_CMD=ppython
    )

    %PYTHON_CMD% -h >nul 2>&1 && (
        goto :LAUNCH
    ) || (
        echo Failed to locate Panda3D python
        pause
        goto :EOF
    )

:LAUNCH
    echo ====================================
    echo Starting Pirates Online Classic...
    echo Token: %POC_TOKEN%
    echo Gameserver: %POC_GAMESERVER%
    echo Environment: %GAME_ENVIRONMENT%
    echo Trial Ended: %TRIAL_ENDED%
    echo PPython: %PYTHON_CMD%
    echo ====================================

    cd ../
    goto :RUN

:RUN
    rem Start the game using the PYTHON_CMD variable
    %PYTHON_CMD% -m pirates.piratesbase.PiratesStart

    pause
    echo Reloading client.
    goto :RUN
