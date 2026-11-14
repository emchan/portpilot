@echo off
setlocal EnableExtensions
title Fooocus on Snapdragon X - setup and launch

rem ===========================================================================
rem  Fooocus + Snapdragon X NPU - self-contained bootstrap
rem
rem  1. clones lllyasviel/Fooocus at the pinned commit
rem  2. applies fooocus_snapdragon_win.diff (must sit next to this script)
rem  3. creates the x64 Fooocus venv (Python 3.10) and the ARM64 QNN venv
rem     (Python 3.12)
rem  4. downloads the precompiled SDXL QNN assets (~4.4 GB, first run only)
rem  5. starts Fooocus with NPU offload and a public Gradio share link
rem
rem  Repeated runs skip completed steps. Keep this file and the .diff together.
rem ===========================================================================

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
set "WORK=%ROOT%\fooocus-snapdragon-npu-experiment"
set "FDIR=%WORK%\Fooocus"
set "DIFF=%ROOT%\fooocus_snapdragon_win.diff"
set "COMMIT=ae05379cc97bc4361ec8b4ec90193dab21be763f"
set "FENV=%FDIR%\fooocus_env"
set "QENV=%WORK%\qnn_env"
set "FPY=%FENV%\Scripts\python.exe"
set "QPY=%QENV%\Scripts\python.exe"

echo.
echo ============================================================
echo   Fooocus + Snapdragon X NPU
echo ============================================================
echo   project folder : "%WORK%"
echo   first run      : envs + ~13 GB of models, then the web UI
echo   later runs     : straight to the web UI
echo.

if not exist "%DIFF%" (
  echo [x] fooocus_snapdragon_win.diff is missing.
  echo     Extract the zip completely and keep the .bat and .diff together.
  goto :fail
)

where git >nul 2>nul
if errorlevel 1 (
  echo [x] Git for Windows is required: https://git-scm.com/download/win
  goto :fail
)

rem ---------------------------------------------------------------------------
rem  Python 3.10 x64 (runs under emulation) and Python 3.12 ARM64 (QNN runtime)
rem ---------------------------------------------------------------------------
set "PYX="
if defined FOOOCUS_X64_PYTHON if exist "%FOOOCUS_X64_PYTHON%" set "PYX=%FOOOCUS_X64_PYTHON%"
if not defined PYX if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" set "PYX=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
if not defined PYX for /f "delims=" %%I in ('py -3.10 -c "import sys;print(sys.executable)" 2^>nul') do if not defined PYX set "PYX=%%I"
call :machine "%PYX%" PYXARCH
if /i not "%PYXARCH%"=="AMD64" (
  echo [x] 64-bit x86 Python 3.10 not found.
  echo     Install the "Windows installer (64-bit)" build of Python 3.10 from
  echo     https://www.python.org/downloads/windows/ and run this script again.
  goto :fail
)

set "PYA="
if defined FOOOCUS_ARM64_PYTHON if exist "%FOOOCUS_ARM64_PYTHON%" set "PYA=%FOOOCUS_ARM64_PYTHON%"
if not defined PYA if exist "%LOCALAPPDATA%\Programs\Python\Python312-arm64\python.exe" set "PYA=%LOCALAPPDATA%\Programs\Python\Python312-arm64\python.exe"
if not defined PYA for /f "delims=" %%I in ('py -3.12 -c "import sys;print(sys.executable)" 2^>nul') do if not defined PYA set "PYA=%%I"
call :machine "%PYA%" PYAARCH
if /i not "%PYAARCH%"=="ARM64" (
  echo [x] Native ARM64 Python 3.12 not found.
  echo     Install the "ARM64 installer" build of Python 3.12 from
  echo     https://www.python.org/downloads/windows/ and run this script again.
  goto :fail
)

echo   x64 Python     : "%PYX%"
echo   ARM64 Python   : "%PYA%"
echo.

rem ---------------------------------------------------------------------------
rem  1. Clone at the pinned commit
rem ---------------------------------------------------------------------------
if not exist "%FDIR%\.git" (
  echo [1/5] Cloning Fooocus ...
  if not exist "%WORK%" mkdir "%WORK%"
  git -c core.autocrlf=false clone https://github.com/lllyasviel/Fooocus.git "%FDIR%"
  if errorlevel 1 goto :fail
) else (
  echo [1/5] Fooocus already cloned.
)

git -C "%FDIR%" config core.autocrlf false
git -C "%FDIR%" rev-parse --verify --quiet "%COMMIT%" >nul 2>nul
if errorlevel 1 (
  echo       Fetching the pinned commit ...
  git -C "%FDIR%" fetch --quiet origin
  if errorlevel 1 goto :fail
)
git -C "%FDIR%" checkout --quiet "%COMMIT%"
if errorlevel 1 (
  echo [x] Could not check out %COMMIT%.
  echo     The folder has conflicting local changes. Move it away and retry.
  goto :fail
)

rem ---------------------------------------------------------------------------
rem  2. Apply the Snapdragon porting diff
rem ---------------------------------------------------------------------------
git -C "%FDIR%" apply --check "%DIFF%" >nul 2>nul
if not errorlevel 1 (
  echo [2/5] Applying the Snapdragon porting diff ...
  git -C "%FDIR%" apply --whitespace=nowarn "%DIFF%"
  if errorlevel 1 goto :fail
) else (
  git -C "%FDIR%" apply --check --reverse "%DIFF%" >nul 2>nul
  if errorlevel 1 (
    echo [x] The diff does not apply to this checkout.
    echo     Delete "%FDIR%" and run this script again.
    goto :fail
  )
  echo [2/5] Porting diff already applied.
)

rem ---------------------------------------------------------------------------
rem  3. x64 Fooocus environment
rem ---------------------------------------------------------------------------
echo [3/5] x64 Fooocus environment ...
if not exist "%FPY%" (
  "%PYX%" -m venv "%FENV%"
  if errorlevel 1 goto :fail
)
if not exist "%WORK%\.fooocus-deps-ok" (
  "%FPY%" -m pip install --disable-pip-version-check --upgrade pip
  "%FPY%" -m pip install --disable-pip-version-check torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cpu
  if errorlevel 1 goto :fail
  "%FPY%" -m pip install --disable-pip-version-check -r "%FDIR%\requirements_versions.txt"
  if errorlevel 1 goto :fail
  "%FPY%" -m pip install --disable-pip-version-check fastapi==0.100.1 starlette==0.27.0 pydantic==2.5.3 jinja2==3.0.3 "setuptools<81"
  if errorlevel 1 goto :fail
  > "%WORK%\.fooocus-deps-ok" echo ok
)

rem Gradio 3.41.2 aborts launch with "When localhost is not accessible ..."
rem behind a proxy. Redefine url_ok at the end of the module (idempotent).
if exist "%FENV%\Lib\site-packages\gradio\networking.py" (
  "%FPY%" -c "import pathlib; p=pathlib.Path(r'%FENV%\Lib\site-packages\gradio\networking.py'); t=p.read_text(encoding='utf-8'); m='# fooocus-snapdragon: url_ok behind proxies'; p.write_text(t if m in t else t+'\n\n'+m+'\ndef url_ok(url):\n    return True\n', encoding='utf-8')"
  if errorlevel 1 echo       note: could not patch gradio networking.py
)

rem ---------------------------------------------------------------------------
rem  4. ARM64 QNN environment
rem ---------------------------------------------------------------------------
echo [4/5] ARM64 QNN environment ...
if not exist "%QPY%" (
  "%PYA%" -m venv "%QENV%"
  if errorlevel 1 goto :fail
)
if not exist "%WORK%\.qnn-deps-ok" (
  "%QPY%" -m pip install --disable-pip-version-check --upgrade pip
  "%QPY%" -m pip install --disable-pip-version-check onnxruntime-qnn==2.7.0 onnxruntime==1.31.1 transformers==4.56.2 onnx pillow numpy huggingface_hub
  if errorlevel 1 goto :fail
  > "%WORK%\.qnn-deps-ok" echo ok
)

rem ---------------------------------------------------------------------------
rem  5. Precompiled SDXL QNN assets (about 4.4 GB)
rem ---------------------------------------------------------------------------
if not exist "%WORK%\sd_xl_npu\unet_w8a16_quantized\part0\model.onnx" (
  echo [5/5] Downloading SDXL QNN assets, about 4.4 GB ...
  "%QPY%" -c "from huggingface_hub import snapshot_download; snapshot_download('Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite', allow_patterns=['text_encoder/*','text_encoder_2/*','tokenizer/*','tokenizer_2/*','unet_w8a16_quantized/*','vae_decoder/1024x1024/*','vae_encoder/1024x1024/*'], local_dir=r'%WORK%\sd_xl_npu')"
  if errorlevel 1 goto :fail
) else (
  echo [5/5] SDXL QNN assets already present.
)

if not exist "%FDIR%\models\inpaint" mkdir "%FDIR%\models\inpaint"

rem ---------------------------------------------------------------------------
rem  Launch
rem ---------------------------------------------------------------------------
echo.
echo Starting Fooocus. The NPU backend is used by default when the assets are
echo present; set FOOOCUS_NPU=0 for the CPU pipeline.
echo The public share link appears below when the UI is up.
echo The first launch also downloads Fooocus's default SDXL preset (~7 GB).
echo Press Ctrl+C to stop.
echo.

set "FOOOCUS_NPU_MODEL=%WORK%\sd_xl_npu"
set "FOOOCUS_NPU_PYTHON=%QPY%"
set "no_proxy=127.0.0.1,localhost"
set "NO_PROXY=127.0.0.1,localhost"
set "U2NET_HOME=%FDIR%\models\inpaint"

cd /d "%FDIR%"
"%FPY%" launch.py --always-cpu --share %*
if errorlevel 1 (
  echo.
  echo [x] Fooocus exited with an error. Check the log above.
  goto :fail
)
echo.
echo Fooocus stopped.
pause
exit /b 0

rem ---------------------------------------------------------------------------
:machine
rem  call :machine "<python.exe>" VAR  ->  VAR = platform.machine()
set "%~2="
if "%~1"=="" exit /b
if not exist "%~1" exit /b
"%~1" -c "import platform;print(platform.machine())" > "%TEMP%\fooocus_machine.txt" 2>nul
if errorlevel 1 exit /b
set /p %~2=<"%TEMP%\fooocus_machine.txt"
exit /b

:fail
echo.
echo Setup stopped. Fix the message above and run this script again;
echo completed steps are skipped.
pause
exit /b 1
